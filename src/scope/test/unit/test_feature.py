import pytest

from scope.domain import model

def test_add_new_feature():
    feature = model.Feature("New Feature", "https://my-feature.com")

    assert feature.state == model.FeatureState.PENDING

def test_start_feature():
    feature = model.Feature("New Feature", "https://my-feature.com")
    feature.start()

    assert feature.state == model.FeatureState.IN_PROGRESS

def test_is_epic_feature():
    feature = model.Feature("New Feaure", "https://my-feature.com", 22)

    assert feature.is_epic == False