# ----------------------
# @Time  : 2025 May
# @Author: Yuanhong Lan
# ----------------------
import datetime


def float_time_to_str_time_with_millisecond(float_time: float) -> str:
    timestamp = int(float_time)

    # Convert timestamp to datetime object
    dt = datetime.datetime.fromtimestamp(timestamp)

    # Format datetime object to string with millisecond precision
    str_time = dt.strftime("%Y-%m-%d-%H-%M-%S") + f".{int((float_time - timestamp) * 1000):03d}"

    return str_time