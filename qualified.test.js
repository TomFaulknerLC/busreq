const fs = require('fs');
const businessRequirements = JSON.parse(fs.readFileSync('./test_requirements_1.json', 'utf8'))

import {isQualified, calculateDistance} from './';


test('calculateDistance', function() {
  expect(calculateDistance('Somewhere', 'Elsewhere')).toEqual(10000);
});

test('isQualified runs', function() {
    const user = {
        'income': 50000,
        'debt': 500000,
        'employment_start_date': new Date(2020, 5, 7),
        'location': "New York, NY"
    }
    expect(isQualified(businessRequirements, user, 200)).toBe(9);
});
