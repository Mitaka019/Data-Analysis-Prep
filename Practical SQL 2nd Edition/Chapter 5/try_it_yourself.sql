
-- BASIC MATH AND STATS WITH SQL

-- Try It Yourself

-- 1

SELECT 3.14159 * (5 ^ 2);
-- Parentheses makes it easier to read.

-- 2

SELECT geo_name, state_us_abbreviation AS "st",
    (CAST(p0010004 AS numeric(8, 1)) / p0010001) * 100 AS "American Indian/Alaska Native Alone_percent"
FROM us_counties_2010
WHERE state_us_abbreviation = 'NY'
ORDER BY "American Indian/Alaska Native Alone_percent" DESC;

-- 3

SELECT 
    percentile_cont(.5) WITHIN GROUP (ORDER BY p0010001) 
FROM us_counties_2010
WHERE state_us_abbreviation = 'NY';

SELECT  
    percentile_cont(.5) WITHIN GROUP (ORDER BY p0010001) 
FROM us_counties_2010
WHERE state_us_abbreviation = 'CA'