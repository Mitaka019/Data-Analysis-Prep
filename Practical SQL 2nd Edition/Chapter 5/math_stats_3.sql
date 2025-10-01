
-- BASIC MATH AND STATS WITH SQL

-- Creating a median() Function

SELECT sum(p0010001) AS "County Sum",
    round(AVG(p0010001), 0) AS "County Average",
    median(p0010001) AS "County Median",
    percentile_cont(.5)
WITHIN GROUP (ORDER BY p0010001) AS "50th Percentile"
FROM us_counties_2010;

-- Finding the Mode

SELECT MODE() WITHIN GROUP (ORDER BY p0010001)
FROM us_counties_2010;

