# ----------------------
# @Time  : 2025 Apr
# @Author: Yuanhong Lan
# ----------------------
import bisect
import os
import re
import subprocess
import threading
import time
from typing import List

from NATE.network_monitor.monitor_data import NetFlowItem, NetFlowStrategy, GetCurrentNetworkStats
from NATE.util import time_util
from NATE.android_testing_utils.log import my_logger


class NetworkMonitor:
    def __init__(self, device_id: str, package_name: str, interval: int = 0.98, tag = "", netflow_strategy = NetFlowStrategy.mAppUidStatsMap):
        self._device_id = device_id
        self._package_name = package_name
        self._interval = interval
        self._tag = tag
        self._netflow_strategy = netflow_strategy

        self._app_uids = None
        self.__get_app_uids()
        if self._app_uids is None:
            my_logger.auto_hint(my_logger.LogLevel.WARNING, self, True, f"Failed to get app UIDs for {self._package_name} on {self._device_id}, trying again...")
            self.__get_app_uids()
        if self._app_uids is None:
            my_logger.auto_hint(my_logger.LogLevel.ERROR, self, True, f"Failed to get app UIDs for {self._package_name} on {self._device_id}")
            raise RuntimeError(f"Failed to get app UIDs for {self._package_name} on {self._device_id}")

        self._cumulative_network_flow_buffer: List[NetFlowItem] = []
        self._step_network_flow_buffer: List[NetFlowItem] = []

        self._network_flow_judge_history = []

        self._is_running = False
        self._thread = threading.Thread(target=self.__run, daemon=True)
        self._lock = threading.Lock()

    def list_all_data(self):
        with self._lock:
            my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Cumulative Data:")
            for item in self._cumulative_network_flow_buffer:
                my_logger.auto_hint(my_logger.LogLevel.INFO, self, False, f"Time: {item.float_time}, RX: {item.rx_bytes}, TX: {item.tx_bytes}")
            my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Step Data:")
            for item in self._step_network_flow_buffer:
                my_logger.auto_hint(my_logger.LogLevel.INFO, self, False, f"Time: {item.float_time}, RX: {item.rx_bytes}, TX: {item.tx_bytes}")

    def start(self):
        if not self._is_running:
            self._is_running = True
            self._thread.start()
        else:
            my_logger.auto_hint(my_logger.LogLevel.WARNING, self, True, "Monitor is already running.")

    def stop(self):
        self._is_running = False
        if self._thread.is_alive():
            self._thread.join()

    def __run(self):
        while self._is_running:
            self.__get_current_network_stats()
            time.sleep(self._interval)

    def __get_app_uids(self):
        try:
            output = subprocess.check_output(
                ["adb", "-s", self._device_id, "shell", "dumpsys", "package", self._package_name],
                text=True,
            )
            uids = re.findall(r"uid=(\d+)", output)
            self._app_uids = list(set(uids))
        except subprocess.CalledProcessError as e:
            my_logger.auto_hint(my_logger.LogLevel.EXCEPTION, self, True, f"Error getting app UIDs: {e}")

    def __persist_network_flow(self, rx_bytes: int, tx_bytes: int):
        with self._lock:
            current_time = time.time()
            if self._cumulative_network_flow_buffer:
                last_item = self._cumulative_network_flow_buffer[-1]
                assert last_item.float_time < current_time
                if (last_item.rx_bytes < rx_bytes) and (last_item.tx_bytes < tx_bytes):
                    self._step_network_flow_buffer.append(NetFlowItem(
                        current_time, rx_bytes - last_item.rx_bytes, tx_bytes - last_item.tx_bytes
                    ))
                else:
                    self._step_network_flow_buffer.append(NetFlowItem(current_time, 0, 0))
            else:
                self._step_network_flow_buffer.append(NetFlowItem(current_time, 0, 0))
            self._cumulative_network_flow_buffer.append(NetFlowItem(current_time, rx_bytes, tx_bytes))

    def __get_current_network_stats(self):
        total_rx_bytes, total_tx_bytes = GetCurrentNetworkStats.get_current_network_stats(
            self._netflow_strategy, self._app_uids, self._device_id
        )
        self.__persist_network_flow(total_rx_bytes, total_tx_bytes)

    def __get_last_network_usage(self, section_length: int = 3.2, hint_details: bool = False) -> List[NetFlowItem]:
        with self._lock:
            target_time_point = time.time() - section_length
            target_pos = bisect.bisect_left([item.float_time for item in self._step_network_flow_buffer], target_time_point)
            section_data = list(self._step_network_flow_buffer[target_pos:])

            if hint_details:
                my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Required Section Data:")
                for item in section_data:
                    my_logger.auto_hint(my_logger.LogLevel.INFO, self, False, f"Time: {item.float_time}, RX: {item.rx_bytes}, TX: {item.tx_bytes}")

        return section_data

    def is_new_network_flow_generated(self, section_length: int = 3.2, hint_details: bool = False) -> bool:
        section_data = self.__get_last_network_usage(section_length, hint_details)

        current_float_time = time.time()
        log_str = (f"{time_util.float_time_to_str_time_with_millisecond(current_float_time)} | "
                   f"{'   '.join([f'{round(item.float_time - current_float_time, 2)}, {item.rx_bytes}, {item.tx_bytes}' for item in section_data])}")

        if len(section_data) < 3:
            my_logger.auto_hint(my_logger.LogLevel.WARNING, self, True, "Not enough data to determine new network flow.")
            res = False
            log_str += " | (Not enough data)"
        else:
            last_1 = section_data[-1]
            last_2 = section_data[-2]
            base_point = section_data[-3]

            if last_1.rx_bytes > base_point.rx_bytes or last_1.tx_bytes > base_point.tx_bytes:
                my_logger.auto_hint(
                    my_logger.LogLevel.INFO, self, True,
                    f"New network flow generated by {last_1.float_time}, {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(last_1.float_time))}."
                )
                res = True
                log_str += f" | (last_1 > base_point)"

            elif last_2.rx_bytes > base_point.rx_bytes or last_2.tx_bytes > base_point.tx_bytes:
                my_logger.auto_hint(
                    my_logger.LogLevel.INFO, self, True,
                    f"New network flow generated by {last_2.float_time}, {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(last_2.float_time))}."
                )
                res = True
                log_str += f" | (last_2 > base_point)"

            else:
                my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "No new network flow generated.")
                res = False
                log_str += " | (No new network flow generated)"
        log_str += f" | {res}"
        self._network_flow_judge_history.append(log_str)
        return res

    def persist_network_monitor_data(self):
        my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Persisting network monitor data...")
        target_dir = os.path.join(os.path.dirname(__file__), "network_monitor_record", f"{self._tag}_network_monitor_record")
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        target_file = os.path.join(target_dir, f"cumulative_record.txt")
        with open(target_file, "w") as f:
            for record in self._cumulative_network_flow_buffer:
                f.write(f"{time_util.float_time_to_str_time_with_millisecond(record.float_time)}  |  {record.rx_bytes}  |  {record.tx_bytes}\n")
        target_file = os.path.join(target_dir, f"step_record.txt")
        with open(target_file, "w") as f:
            for record in self._step_network_flow_buffer:
                f.write(f"{time_util.float_time_to_str_time_with_millisecond(record.float_time)}  |  {record.rx_bytes}  |  {record.tx_bytes}\n")
        target_file = os.path.join(target_dir, f"judge_history.txt")
        with open(target_file, "w") as f:
            for record in self._network_flow_judge_history:
                f.write(f"{record}\n")


if __name__ == '__main__':
    m = NetworkMonitor("emulator-5576", "org.thoughtcrime.securesms")
    m.start()

    time.sleep(10)
    print()
    m.is_new_network_flow_generated(hint_details=True)
    print()
    m.list_all_data()

    time.sleep(5)
    print()
    m.is_new_network_flow_generated(hint_details=True)
    print()
    m.stop()

    time.sleep(5)
    print()
    m.is_new_network_flow_generated(hint_details=True)
    print()
    m.list_all_data()

    # targets = [
    #     "org.thoughtcrime.securesms",
    #     "org.mozilla.fenix.debug",
    #     "com.jetpack.android",
    #     "com.duckduckgo.mobile.android.debug",
    #     "net.thunderbird.android.debug",
    #     "org.wikipedia.alpha",
    #     "com.forrestguice.suntimeswidget",
    #     "com.ichi2.anki.debug",
    #     "org.schabi.newpipe.debug",
    #     "com.amaze.filemanager.debug",
    #     "de.danoeh.antennapod.debug",
    #     "org.connectbot.debug",
    # ]
    # for target in targets:
    #     m = Monitor("emulator-5576", target)
    #     m.__get_current_network_stats()
