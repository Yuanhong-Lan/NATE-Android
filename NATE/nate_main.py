# ----------------------
# @Time  : 2025 May
# @Author: Yuanhong Lan
# ----------------------
import datetime
import random
from typing import Optional, Union

from NATE.guidance.guidance_model import QLearningWithKnownActionNum, QLearningWithAutoAction
from NATE.network_injector.injector_wrapper import InjectorHandler
from NATE.network_monitor.monitor import NetworkMonitor
from NATE.network_monitor.monitor_data import NetFlowStrategy
from android_testing_utils.log import my_logger


class NATE_MAIN:
    def __init__(self, device_id: str, package_name: str, use_pure_random: bool = False, auto_action: bool = False, netflow_strategy = NetFlowStrategy.mAppUidStatsMap):
        self._device_id = device_id
        self._package_name = package_name
        self._use_pure_random = use_pure_random
        self._auto_action = auto_action
        self._netflow_strategy = netflow_strategy

        self._tag = f"{self._package_name}_{datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')}"

        if use_pure_random:
            my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Using pure random injection strategy.")
        else:
            my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Using model guiding injection strategy.")
            self._network_monitor = NetworkMonitor(self._device_id, self._package_name, tag=self._tag, netflow_strategy=self._netflow_strategy)
            self._network_monitor.start()

            if not auto_action:
                my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Using known action number.")
                self._guidance_model = QLearningWithKnownActionNum(tag=self._tag)
            else:
                my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Using auto action.")
                self._guidance_model = QLearningWithAutoAction(tag=self._tag)

        self._injector_handler = InjectorHandler(self._device_id, thread_mode=True, tag=self._tag)

    def persist_history(self):
        my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Persisting history...")
        if self._use_pure_random:
            pass
        else:
            self._guidance_model.persist_q_table()
            self._network_monitor.persist_network_monitor_data()
        self._injector_handler.persistent_history()

    def nate_step(
            self,
            raw_app_state: str,
            selected_action: Union[int, str],

            target_app_state: Optional[str],
            target_selected_action: Optional[Union[int, str]],

            raw_action_count: Optional[int] = None,
            target_action_count: Optional[int] = None,
    ):
        """
        Step function for NATE should be executed before the event execution of the testing tool.
        """
        if not self._auto_action:
            assert raw_action_count is not None
            assert target_action_count is not None if target_app_state is not None else True

        my_logger.auto_hint(
            my_logger.LogLevel.INFO, self, True,
            f"Current NATE Step: "
            f"From ({raw_app_state}, {raw_action_count}, {selected_action})"
            f"To ({target_app_state}, {target_action_count}, {target_selected_action})"
        )

        if self._use_pure_random:
            if random.random() < 0.1:
                my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Random injection triggered by pure random.")
                self._injector_handler.random_inject()
        else:
            is_injecting = self._injector_handler.is_injecting()
            is_network_related = None
            if not is_injecting:
                is_network_related = self._network_monitor.is_new_network_flow_generated()

            self._guidance_model.add_state(raw_app_state, raw_action_count)
            reward = self._guidance_model.analyze_reward(target_app_state, is_network_related)
            self._guidance_model.add_state(target_app_state, target_action_count)
            self._guidance_model.update(raw_app_state, selected_action, target_app_state, reward)

            if not is_injecting and target_app_state is not None:
                if self._guidance_model.is_predicted_to_need_network_injection(target_app_state, target_selected_action):
                    my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Network injection triggered by guidance.")
                    self._injector_handler.random_inject()
