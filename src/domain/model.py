from enum import Enum

class FeatureState(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    TO_VERIFY = 3
    BLOCKED = 4
    DONE = 5

class Feature:
    id: int

    def __init__(self, title, link):
        self.state = FeatureState.PENDING
        self.title = title
        self.link = link

    def start(self):
        self.state = FeatureState.IN_PROGRESS
