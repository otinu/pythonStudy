from dataclasses import dataclass


@dataclass
class User2:
    name: str
    age: int = 4
    address: str = "秋田県"
