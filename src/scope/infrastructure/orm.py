from sqlalchemy import ( MetaData, Table, Column, Integer, String, ForeignKey, create_engine )
from sqlalchemy.orm import mapper
from sqlalchemy.sql.sqltypes import Enum

from scope.domain import model

import scope.config

metadata = MetaData()

features = Table(
    'features', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255)),
    # Column('state_id', ForeignKey('feature_states.id')),
    Column('state', Enum(model.FeatureState)),
    Column('link', String(255))
)

# feature_states = Table(
#     'feature_states', metadata,
#     Column('id', Integer, primary_key=True, autoincrement=True),
#     Column('description', Integer)
# )

def start_mappers():
    # feature_states_mapper = mapper(model.FeatureState, feature_states)
    features_mapper = mapper(model.Feature, features)

# def init_database():
#     metadata.create_all(create_engine(
#     scope.config.get_postgres_uri(),
#     isolation_level="SERIALIZABLE"
# ))