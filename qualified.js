const godzilla = {
    'location': "Tokyo, Japan",
};


function calculateDistance(user_location, godzilla_location) {
    return 10000;
}


function isQualified(req, user, target_score) {
    throw new Error("Not implemented.");
}


function main() {
    const businessRequirements = {
        'debt_to_income_ratio': {
            'action': 'lte',
            'value': '40%',
            'weight': 0.8,
        },
        'is_employed': {
            'action': 'e',
            'value': 'True',
            'disqualifying': true,
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
    const user = {
        'income': 50000,
        'debt': 500000,
        'employment_start_date': new Date(2020, 5, 7),
        'location': "New York, NY",
    }
    console.log(`Is Qualified: ${isQualified(businessRequirements, user, 200)}`);
};


main();
