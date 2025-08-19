# ----------------------
# @Time  : 2025 Mar
# @Author: Yuanhong Lan
# ----------------------
import random
import threading
import time

from NATE.network_injector.injection_data import InjectStrategy, InjectorRecorder
from android_testing_utils.log import my_logger
from android_testing_utils.tool.adb_cmd import ADBNetwork, ADBSystemOperation


class Injector:
    def __init__(self, device_id: str, thread_mode: bool = True, tag=""):
        self._injector_recorder = InjectorRecorder(f"{tag}_{device_id}_{time.strftime('%Y-%m-%d-%H:%M:%S')}")

        self._injector_recorder.add_a_record("Start")
        my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Network Injector Started.")

        self._device_id = device_id
        self._thread_mode = thread_mode

        self._lock = threading.Lock()
        self._is_busy = False

        self.__initialization()

        self._strategy_map = {
            InjectStrategy.STRATEGY_1: self.__disconnect_before_and_reconnect_after,
            InjectStrategy.STRATEGY_2: self.__disconnect_during_and_reconnect_after,
            InjectStrategy.STRATEGY_3: self.__unstable_network_switching,
        }

    def __initialization(self):
        self._injector_recorder.add_a_record("Initialize")
        my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Initializing....")
        if not ADBSystemOperation.is_root(self._device_id):
            ADBSystemOperation.run_adb_as_root(self._device_id)
            time.sleep(1)
        self.__fully_open_network()
        time.sleep(1)

    def __fully_open_network(self):
        ADBNetwork.close_airplane_mode(self._device_id)
        ADBNetwork.open_mobile_data(self._device_id)
        ADBNetwork.open_wifi(self._device_id)

    def __fully_shutdown_network(self):
        ADBNetwork.open_airplane_mode(self._device_id)
        ADBNetwork.close_mobile_data(self._device_id)
        ADBNetwork.close_wifi(self._device_id)

    def is_busy(self) -> bool:
        with self._lock:
            return self._is_busy

    def inject(self, current_inject_strategy: InjectStrategy) -> bool:
        with self._lock:
            if self._is_busy:
                my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Injector is busy now.")
                return False
            self._is_busy = True

        if not self._thread_mode:
            self.__strategy_executor(current_inject_strategy)
            return True

        thread = threading.Thread(target=self.__strategy_executor, args=(current_inject_strategy,))
        thread.start()
        return True

    def __strategy_executor(self, current_inject_strategy: InjectStrategy):
        try:
            self._injector_recorder.add_a_record(f"Injecting {current_inject_strategy}")
            my_logger.auto_hint(
                my_logger.LogLevel.INFO, self, True,
                f"Injecting strategy: {current_inject_strategy}, {current_inject_strategy.value}"
            )
            self._strategy_map[current_inject_strategy]()
            my_logger.auto_hint(
                my_logger.LogLevel.INFO, self, True,
                f"Injection of {current_inject_strategy} finished"
            )
            self._injector_recorder.add_a_record(f"Injection of {current_inject_strategy} finished")
        finally:
            with self._lock:
                self._is_busy = False

    def __disconnect_before_and_reconnect_after(self):
        self.__fully_shutdown_network()
        time.sleep(5)
        self.__fully_open_network()

    def __disconnect_during_and_reconnect_after(self):
        time.sleep(2)
        self.__fully_shutdown_network()
        time.sleep(3)
        self.__fully_open_network()

    def __unstable_network_switching(self):
        ADBNetwork.close_airplane_mode(self._device_id)
        ADBNetwork.close_wifi(self._device_id)
        ADBNetwork.open_mobile_data(self._device_id)

        for i in range(4):
            lose_connection_time = random.random() * 0.2
            normal_connection_time = 1.25 - lose_connection_time

            ADBNetwork.close_mobile_data(self._device_id)
            time.sleep(lose_connection_time)
            ADBNetwork.open_mobile_data(self._device_id)
            time.sleep(normal_connection_time)

        ADBNetwork.open_mobile_data(self._device_id)
        ADBNetwork.open_wifi(self._device_id)

    def persist_history(self):
        self._injector_recorder.persistent_records()
