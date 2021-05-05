from sqlalchemy import ( MetaData, Table, Column, Integer, String, ForeignKey )
from sqlalchemy.orm import mapper

from src.domain import model

metadata = MetaData()

features = Table(
    'features', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255)),
    # Column('state_id', ForeignKey('feature_states.id')),
    Column('state_id', Integer),
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