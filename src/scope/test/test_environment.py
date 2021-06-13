from sqlalchemy import create_engine
from sqlalchemy.engine.base import Connection

import scope.config
from scope.infrastructure.orm import metadata

def test_database_connection():
    engine = create_engine(scope.config.get_postgres_uri(), isolation_level='SERIALIZABLE')

    assert isinstance(engine.connect(), Connection)


def test_create_database():
    engine = create_engine(scope.config.get_postgres_uri(), isolation_level='SERIALIZABLE')
    metadata.create_all(engine)

    assert engine==engine