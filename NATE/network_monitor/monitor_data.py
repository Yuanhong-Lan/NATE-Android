# ----------------------
# @Time  : 2025 May
# @Author: Yuanhong Lan
# ----------------------
import re
import subprocess
from enum import Enum
from typing import NamedTuple

from NATE.android_testing_utils.log import my_logger


class NetFlowItem(NamedTuple):
    float_time: float
    rx_bytes: int
    tx_bytes: int


class NetFlowStrategy(Enum):
    mAppUidStatsMap = "mAppUidStatsMap"
    xt_qtaguid = "xt_qtaguid"


class GetCurrentNetworkStats:
    @classmethod
    def get_current_network_stats(cls, netflow_strategy: NetFlowStrategy, app_uids, device_id: str):
        func_map = {
            NetFlowStrategy.mAppUidStatsMap: cls.__get_current_network_stats_by_mAppUidStatsMap,
            NetFlowStrategy.xt_qtaguid: cls.__get_current_network_stats_by_xt_qtaguid,
        }
        if netflow_strategy not in func_map:
            raise ValueError(f"Unsupported netflow strategy: {netflow_strategy}")
        return func_map[netflow_strategy](app_uids, device_id)

    @classmethod
    def __get_current_network_stats_by_mAppUidStatsMap(cls, app_uids, device_id: str):
        total_rx_bytes = 0
        total_tx_bytes = 0

        try:
            output = subprocess.check_output(
                ["adb", "-s", device_id, "shell", "dumpsys", "netstats"],
                text=True,
            )

            for uid in app_uids:
                match_res = re.search(rf"{uid} (\d+) \d+ (\d+) \d+", output)

                if match_res:
                    rx_bytes = match_res.group(1)
                    tx_bytes = match_res.group(2)
                    if rx_bytes and tx_bytes:
                        my_logger.auto_hint(my_logger.LogLevel.DEBUG, cls, True, f"UID: {uid}, RX: {rx_bytes}, TX: {tx_bytes}")
                        total_rx_bytes += int(rx_bytes)
                        total_tx_bytes += int(tx_bytes)
                    else:
                        my_logger.auto_hint(my_logger.LogLevel.WARNING, cls, True, f"Missing RX or TX bytes for UID: {uid}")
                else:
                    my_logger.auto_hint(my_logger.LogLevel.WARNING, cls, True,
                                        f"No match found for UID: {uid} in network stats")

            my_logger.auto_hint(my_logger.LogLevel.DEBUG, cls, True,
                                f"Total RX bytes: {total_rx_bytes}, Total TX bytes: {total_tx_bytes}")

        except subprocess.CalledProcessError as e:
            my_logger.auto_hint(my_logger.LogLevel.EXCEPTION, cls, True, f"Error getting network stats: {e}")

        return total_rx_bytes, total_tx_bytes

    @classmethod
    def __get_current_network_stats_by_xt_qtaguid(cls, app_uids, device_id: str):
        total_rx_bytes = 0
        total_tx_bytes = 0

        try:
            for uid in app_uids:
                cmd = f"adb -s {device_id} shell cat /proc/net/xt_qtaguid/stats | grep {uid}"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if not result.stdout:
                    my_logger.auto_hint(my_logger.LogLevel.WARNING, cls, True, f"No match found for UID: {uid} in network stats")
                    continue
                lines = result.stdout.strip().split('\n')
                rx_bytes = 0
                tx_bytes = 0
                for line in lines:
                    parts = line.split()
                    rx_bytes += int(parts[5])
                    tx_bytes += int(parts[7])
                if rx_bytes and tx_bytes:
                    my_logger.auto_hint(my_logger.LogLevel.DEBUG, cls, True, f"UID: {uid}, RX: {rx_bytes}, TX: {tx_bytes}")
                    total_rx_bytes += int(rx_bytes)
                    total_tx_bytes += int(tx_bytes)
                else:
                    my_logger.auto_hint(my_logger.LogLevel.WARNING, cls, True, f"Missing RX or TX bytes for UID: {uid}")

            my_logger.auto_hint(my_logger.LogLevel.DEBUG, cls, True, f"Total RX bytes: {total_rx_bytes}, Total TX bytes: {total_tx_bytes}")

        except subprocess.CalledProcessError as e:
            my_logger.auto_hint(my_logger.LogLevel.EXCEPTION, cls, True, f"Error getting network stats: {e}")

        return total_rx_bytes, total_tx_bytes


if __name__ == '__main__':
    # print(GetCurrentNetworkStats.get_current_network_stats(
    #     netflow_strategy=NetFlowStrategy.mAppUidStatsMap,
    #     app_uids=[10192],
    #     device_id="emulator-5576"
    # ))
    print(GetCurrentNetworkStats.get_current_network_stats(
        netflow_strategy=NetFlowStrategy.xt_qtaguid,
        app_uids=[10087],
        device_id="emulator-5566"
    ))
