from dataclasses import dataclass


@dataclass
class Message:
    mg_time: str
    t_num: str
    to_t_num: str
    txt: str
