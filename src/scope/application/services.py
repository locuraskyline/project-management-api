from typing import Optional

from sqlalchemy.sql.sqltypes import Integer

from scope.domain.model import Feature
from scope.application.unit_of_work import AbstractUnitOfWork

def get_all_features(uow: AbstractUnitOfWork):
    with uow:
        features = uow.features.get_all()

    return features

def get_feature(id: Integer, uow: AbstractUnitOfWork) -> Feature:
    with uow:
        feature = uow.features.get(id)
    
    return feature

def get_feature_childs(id: str, uow: AbstractUnitOfWork):
    with uow:
        features = uow.features.get_childs(id)

    return features

def add_feature(title: str, link: Optional[str], parent_id: Optional[Integer], uow: AbstractUnitOfWork):
    with uow:
        #TODO se podria pasar el objeto Feature padre como parametro para esta validacion tenerla en feature?
        if parent_id is not None and not uow.features.get(parent_id).is_epic:
            raise "Parent especified is not a epic."

        uow.features.add(Feature(title, link, parent_id))
        uow.commit()

def update_feature(title: str, link: Optional[str], state: str, uow: AbstractUnitOfWork):
    with uow:
        uow.feature.update(Feature(title,link))