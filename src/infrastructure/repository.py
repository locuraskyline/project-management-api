from typing import Protocol, TypeVar

from src.domain import model

T = TypeVar('T')

class AbstractRepository(Protocol):
    def get(self, id) -> T:
        ...
    
    def add(self, item: T):
        ...

    def update(self, item: T):
        ...

class SqlAlchemyRepository:
    def __init__(self, session):
        self.session = session

    def get(self, id) -> model.Feature:
        return self.session.query(model.Feature).filter(id=id).first()

    def add(self, feature: model.Feature):
        self.session.add(feature)