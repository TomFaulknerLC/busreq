# This is a sample Python script.
import datetime

godzilla = {
    'location': "Tokyo, Japan",
}


def calculate_distance(user_location, godzilla_location):
    return 10_000


def is_qualified(req: dict, user: dict, target_score: float) -> (bool, int):
    raise NotImplementedError


def main():
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
    user = {
        'income': 50_000,
        'debt': 500_000,
        'employment_start_date': datetime.date(year=2020, month=6, day=7),
        'location': "New York, NY",
    }
    print(f"Is Qualified: {is_qualified(business_requirements, user, 200)}")


if __name__ == '__main__':
    main()

