
-- JOINING TABLES IN A RELATIONAL DATABASE

-- Try It Yourself

-- 1

SELECT c2010.geo_name AS "geo_name 2010",
    c2010.state_us_abbreviation AS state_2010,
    c2000.geo_name AS "geo_name 2000",
    c2000.state_us_abbreviation AS state_2000
FROM us_counties_2010 AS c2010 FULL OUTER JOIN us_counties_2000 AS c2000
    ON c2010.county_fips = c2000.county_fips
    AND c2010.state_fips = c2000.state_fips
WHERE c2010.geo_name IS NULL OR c2000.geo_name IS NULL;

-- 2

CREATE TEMPORARY TABLE us_pop_temp AS
SELECT c2010.geo_name,
    c2010.state_us_abbreviation AS state,
    c2010.p0010001 AS pop_2010,
    c2000.p0010001 AS pop_2000,
    c2010.p0010001 - c2000.p0010001 AS raw_change,
    ROUND((CAST(c2010.p0010001 AS numeric(8, 1)) - c2000.p0010001) /
    c2000.p0010001 * 100, 1) AS pct_change
FROM us_counties_2010 AS c2010 INNER JOIN us_counties_2000 AS c2000
    ON c2010.county_fips = c2000.county_fips
WHERE c2010.p0010001 <> c2000.p0010001
ORDER BY pct_change DESC;

SELECT percentile_cont(.5) WITHIN GROUP (ORDER BY pct_change)
FROM us_pop_temp;

-- 3

SELECT * FROM us_pop_temp
ORDER BY pct_change ASC
LIMIT 1;