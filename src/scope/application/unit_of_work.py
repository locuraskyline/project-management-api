from typing import Protocol
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import scope.config
from scope.infrastructure import repository

class AbstractUnitOfWork(Protocol):
    
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._rollback()

    def commit(self):
        self._commit()

    def _commit(self):
        raise NotImplementedError

    def _rollback(self):
        raise NotImplementedError

DEFAULT_SESSION_FACTORY = sessionmaker(bind=create_engine(
    scope.config.get_postgres_uri(),
    isolation_level="SERIALIZABLE"
))

class SqlAlchemyUnitOfWork:
    
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.features = repository.SqlAlchemyRepository(self.session)

        #return super().__enter__()
        return self
    
    def __exit__(self, *args):
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()