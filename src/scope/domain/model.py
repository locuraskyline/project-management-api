from enum import Enum
from typing import Optional

from sqlalchemy.sql.sqltypes import Integer

class FeatureState(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    TO_VERIFY = 3
    BLOCKED = 4
    DONE = 5

class Feature:
    id: int

    def __init__(self, title: str, link: str, parent_id: Optional[Integer] = None):
        self.state = FeatureState.PENDING
        self.title = title
        self.link = link
        self.__parent_id = parent_id

    def start(self):
        self.state = FeatureState.IN_PROGRESS

    @property
    def is_epic(self):
        return self.__parent_id == None