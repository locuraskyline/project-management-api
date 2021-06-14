from typing import Protocol, TypeVar

from scope.domain import model

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

    def get_all(self):
        return self.session.query(model.Feature).all()

    def get(self, id) -> model.Feature:
        return self.session.query(model.Feature).get(id)
        #.filter(id=id).first()

    def add(self, feature: model.Feature):
        self.session.add(feature)