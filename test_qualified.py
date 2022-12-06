import datetime

from .qualified import is_qualified

business_requirements = {
    'debt_to_income_ratio': {
        'action': 'lte',
        'value': '40%',
        'weight': 0.8,
    },
    'is_employed': {
        'action': 'e',
        'value': 'True',
        'disqualifying': True,
        'weight': 1,
    },
    'employment_duration': {
        'action': 'gt',
        'value': '36 months',
        'weight': 0.4,
    },
    'distance_from_godzilla': {
        'action': 'gte',
        'value': '100 miles',
        'weight': 0.6,
    },
}


def test_is_qualified_exists():
    assert is_qualified is not None


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
