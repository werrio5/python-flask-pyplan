from dataclasses import dataclass

@dataclass
class Day:
    weekday: int
    number: int

    def __init__(self, weekday, number):
        self.weekday = weekday
        self.number = number