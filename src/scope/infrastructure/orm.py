from sqlalchemy import ( MetaData, Table, Column, Integer, String, ForeignKey, create_engine )
from sqlalchemy.orm import mapper
from sqlalchemy.sql.sqltypes import Enum

from scope.domain import model

metadata = MetaData()

features = Table(
    'features', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(255)),
    Column('state', Enum(model.FeatureState)),
    Column('link', String(255)),
    __parent_id = Column('parent_id', Integer)
)

def start_mappers():
    features_mapper = mapper(model.Feature, features)