# ----------------------
# @Time  : 2025 Mar
# @Author: Yuanhong Lan
# ----------------------
import random
import time

from NATE.network_injector.injection_data import InjectStrategy
from NATE.network_injector.injector import Injector
from NATE.android_testing_utils.log import my_logger


class InjectorHandler:
    def __init__(
            self,
            device_id: str,
            thread_mode: bool = True,
            tag: str = ""
    ):
        self._injector = Injector(device_id, thread_mode, tag)

    def random_inject(self) -> bool:
        chosen_strategy = random.choice(list(InjectStrategy))
        my_logger.auto_hint(
            my_logger.LogLevel.INFO, self, True,
            f"Randomly chosen strategy: {chosen_strategy}, {chosen_strategy.value}"
        )
        return self._injector.inject(chosen_strategy)

    def is_injecting(self) -> bool:
        return self._injector.is_busy()

    def targeted_inject(self, current_inject_strategy: InjectStrategy) -> bool:
        return self._injector.inject(current_inject_strategy)

    def persistent_history(self):
        my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Persisting records...")
        self._injector.persist_history()


if __name__ == '__main__':
    injector_handler = InjectorHandler("emulator-5560")
    injector_handler.targeted_inject(InjectStrategy.STRATEGY_3)
    time.sleep(10)
    injector_handler.persistent_history()
