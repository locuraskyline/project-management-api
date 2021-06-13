from typing import Optional

from scope.domain.model import Feature
from scope.application.unit_of_work import AbstractUnitOfWork

def get_all_features():
    NotImplementedError

def get_feature(id: str, uow: AbstractUnitOfWork) -> Feature:
    with uow:
        feature = uow.features.get(id)
    
    return feature

def add_feature(title: str, link: Optional[str], uow: AbstractUnitOfWork):
    with uow:
        uow.features.add(Feature(title, link))
        uow.commit()