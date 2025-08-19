# ----------------------
# @Time  : 2025 Mar
# @Author: Yuanhong Lan
# ----------------------
import os.path
import time
from enum import Enum
from typing import List, NamedTuple


class InjectorRecord(NamedTuple):
    time: str
    detail: str


class InjectorRecorder:
    def __init__(self, tag: str):
        self._tag = tag

        self._record: List[InjectorRecord] = []

    def add_a_record(self, detail: str):
        self._record.append(InjectorRecord(
            time=time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()),
            detail=detail,
        ))

    def persistent_records(self):
        target_dir = os.path.join(os.path.dirname(__file__), "injection_record")
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        target_file = os.path.join(target_dir, f"{self._tag}_injector_record.txt")
        with open(target_file, "w") as f:
            for record in self._record:
                f.write(f"{record.time}  |  {record.detail}\n")


class InjectStrategy(Enum):
    STRATEGY_1 = "Disconnect before and reconnect after"
    STRATEGY_2 = "Disconnect during and reconnect after"
    STRATEGY_3 = "Unstable network"
