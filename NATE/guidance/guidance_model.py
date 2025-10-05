# ----------------------
# @Time  : 2025 May
# @Author: Yuanhong Lan
# ----------------------
import os
from abc import ABC, abstractmethod
from typing import Optional, Dict, List

from NATE.android_testing_utils.log import my_logger


class QLearning(ABC):
    ALPHA = 0.1
    GAMMA = 0.99
    DEFAULT_Q_VALUE = 0.0
    REWARD_BASE = 1
    THRESHOLD = 0.05

    def __init__(self, tag = ""):
        self._tag = tag
        self._q_table = {}

    def persist_q_table(self):
        my_logger.auto_hint(my_logger.LogLevel.INFO, self, True, "Persisting Q-table...")
        target_dir = os.path.join(os.path.dirname(__file__), "q_table")
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        target_file = os.path.join(target_dir, f"{self._tag}_q_table.txt")
        with open(target_file, "w") as f:
            for state, q_values in self._q_table.items():
                f.write(f"{state}: {q_values}\n")

    def analyze_reward(
            self,
            target_app_state: Optional[str],
            is_network_related: Optional[bool] = None,
    ):
        # No network check
        if is_network_related is None:
            return 0

        # Not related to network
        if not is_network_related:
            return -self.REWARD_BASE * 1

        # Related to network but exit or no new state
        if target_app_state is None or target_app_state in self._q_table:
            return -self.REWARD_BASE * 0.5
        # Related to network and new state
        else:
            return self.REWARD_BASE * 2

    @abstractmethod
    def is_predicted_to_need_network_injection(self, app_state, selected_action):
        pass

    @abstractmethod
    def add_state(self, state: Optional[str], action_count: Optional[int]):
        pass

    @abstractmethod
    def update(self, raw_app_state, selected_action, target_app_state, reward: float):
        pass


class QLearningWithKnownActionNum(QLearning):
    def __init__(self, tag=""):
        super().__init__(tag)
        self._q_table: Dict[str, List[float]]

    def is_predicted_to_need_network_injection(self, app_state, selected_action_index):
        return self._q_table[app_state][selected_action_index] >= self.THRESHOLD

    def add_state(self, state: Optional[str], action_count: Optional[int]):
        if state is None or action_count is None:
            return
        if state not in self._q_table:
            self._q_table[state] = [self.DEFAULT_Q_VALUE] * action_count

    def update(self, raw_app_state, selected_action_index: int, target_app_state, reward: float):
        q_current = self._q_table[raw_app_state][selected_action_index]
        if target_app_state is None:
            q_next_max = 0
        else:
            q_next_max = max(self._q_table[target_app_state])
        q_target = q_current + self.ALPHA * (reward + self.GAMMA * q_next_max - q_current)
        self._q_table[raw_app_state][selected_action_index] = q_target


class QLearningWithAutoAction(QLearning):
    def __init__(self, tag=""):
        super().__init__(tag)
        self._q_table: Dict[str, Dict[str, float]]

    def is_predicted_to_need_network_injection(self, app_state, selected_action_str):
        if selected_action_str not in self._q_table[app_state]:
            self._q_table[app_state][selected_action_str] = self.DEFAULT_Q_VALUE
        return self._q_table[app_state][selected_action_str] >= self.THRESHOLD

    def add_state(self, state: Optional[str], action_count: None =None):
        if state is None:
            return
        if state not in self._q_table:
            self._q_table[state] = {}

    def update(self, raw_app_state, selected_action_str: str, target_app_state, reward: float):
        if selected_action_str not in self._q_table[raw_app_state]:
            self._q_table[raw_app_state][selected_action_str] = self.DEFAULT_Q_VALUE
        q_current = self._q_table[raw_app_state][selected_action_str]
        if target_app_state is None:
            q_next_max = 0
        else:
            if len(self._q_table[target_app_state]) == 0:
                q_next_max = 0
            else:
                q_next_max = max(self._q_table[target_app_state].values())
        q_target = q_current + self.ALPHA * (reward + self.GAMMA * q_next_max - q_current)
        self._q_table[raw_app_state][selected_action_str] = q_target
