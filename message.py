import dataclasses


@dataclasses
class message:
    date_time: str
    author: str
    text: str
