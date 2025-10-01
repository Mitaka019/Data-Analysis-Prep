
-- IMPORTING AND EXPORTING DATA

-- Performing the Census Import with COPY

SELECT * FROM us_counties_2010;

SELECT geo_name, state_us_abbreviation, area_land
FROM us_counties_2010
ORDER BY area_land DESC
LIMIT 3;

SELECT geo_name, state_us_abbreviation, internal_point_lon
FROM us_counties_2010
ORDER BY internal_point_lon DESC
LIMIT 5;

-- Importing a Subset of Columns with COPY

CREATE TABLE supervisor_salaries(
    town varchar(30),
    county varchar(30),
    supervisor varchar(30),
    start_date date,
    salary money,
    benefits money
);

COPY supervisor_salaries (town, supervisor, salary)
FROM 'C:\Users\Kevin\Downloads\supervisor_salaries.csv'
WITH (FORMAT CSV, HEADER);

-- By noting in parentheses the three present columns after the table
-- name, we tell PostgreSQL to only look for data to fill those columns
-- when it reads the CSV.