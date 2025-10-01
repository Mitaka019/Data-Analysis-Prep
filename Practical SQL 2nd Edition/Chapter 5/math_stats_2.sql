
-- BASIC MATH AND STATS WITH SQL

-- Aggregate Functions for Averages and Sums

SELECT SUM(p0010001) AS "County Sum",
    ROUND(AVG(p0010001), 0) AS "County Average"
FROM us_counties_2010;

-- Finding the Median

-- Average: The sum of all the values divided by the number of values.
-- Median: The “middle” value in an ordered set of values.

-- Finding the Median with Percentile Functions

CREATE TABLE percentile_test(
    numbers integer
);

INSERT INTO percentile_test (numbers)
VALUES
    (1), (2), (3), (4), (5), (6);

SELECT percentile_cont(.5) WITHIN GROUP (ORDER BY numbers),
    percentile_disc(.5) WITHIN GROUP (ORDER BY numbers)
FROM percentile_test;

-- Median and Percentiles with Census Data

SELECT SUM(p0010001) AS "County Sum",
   ROUND(AVG(p0010001), 0) AS "County Average",
   percentile_cont(.5) WITHIN GROUP (ORDER BY p0010001) AS "County Median"
FROM us_counties_2010;

-- Finding Other Quantiles with Percentile Functions

-- Most common are quartiles (four equal groups), quintiles (five groups), and deciles (10 groups).

SELECT percentile_cont(array [.25, .5, .75]) WITHIN GROUP (ORDER BY p0010001) AS "quartiles"
FROM us_counties_2010;

-- unnest(): makes the array easier to read by turning itinto rows.

SELECT unnest(percentile_cont(array [.25, .5, .75]) WITHIN GROUP (ORDER BY p0010001)) AS "quartiles"
FROM us_counties_2010;


