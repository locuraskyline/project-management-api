from typing import Optional

from src.domain.model import Feature
from src.application.unit_of_work import AbstractUnitOfWork

def get_all_features():
    NotImplementedError

def add_feature(title: str, link: Optional[str], uow: AbstractUnitOfWork):
    with uow:
        uow.features.add(Feature(title, link))
        uow.commit()