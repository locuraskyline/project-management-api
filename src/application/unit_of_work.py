from typing import Protocol
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import src.config
from src.infrastructure import repository

import os

#TO_DO: parche temporal, la funcion esta en config.py pero esta mal la importacion
def get_postgres_uri():
    host = os.environ.get('DB_HOST', 'localhost')
    port = 54321 if host == 'localhost' else 5432
    password = os.environ.get('DB_PASSWORD', 'example')
    user, db_name = 'postgres', 'postgres'
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

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
    get_postgres_uri(),
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
    
    def __exit__(self):
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()