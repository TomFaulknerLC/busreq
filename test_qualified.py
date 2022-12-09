import datetime
import json

from .qualified import is_qualified

with open('test_requirements_1.json') as f:
    business_requirements = json.load(f)


def test_is_qualified_exists():
    assert is_qualified is not None


def test_json_loaded():
    assert isinstance(business_requirements, dict)


def test_user_is_qualified():
    user = {
        'income': 50_000,
        'debt': 500_000,
        'employment_start_date': datetime.date(year=2020, month=6, day=7),
        'location': "New York, NY",
    }
    qualified, score = is_qualified(business_requirements, user, 100)

    assert qualified is True
    assert score == 160.0


def test_user_is_not_qualified():
    user = {
        'income': 50_000,
        'debt': 23_000,
        'employment_start_date': datetime.date(year=2020, month=6, day=7),
        'location': "New York, NY",
    }
    qualified, score = is_qualified(business_requirements, user, 200)

    assert qualified is False
    assert score == 160.0
