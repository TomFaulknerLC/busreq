const fs = require('fs');
const business_requirements = JSON.parse(fs.readFileSync('./test_requirements_1.json', 'utf8'))

import {isQualified, calculateDistance} from './';


test('calculateDistance', function() {
  expect(calculateDistance('Somewhere', 'Elsewhere')).toEqual(10000);
});

test('is_qualified runs', function() {
    expect(isQualified(businessRequirements, user, 200)).toBe(9);
});
