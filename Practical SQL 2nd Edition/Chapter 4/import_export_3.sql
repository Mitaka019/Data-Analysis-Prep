
-- IMPORTING AND EXPORTING DATA

-- Adding a Default Value to a Column During Import

-- Temporary tables exist only until you end your database session.

-- DELETE FROM supervisor_salaries;

CREATE TEMPORARY TABLE supervisor_salaries_temp(LIKE supervisor_salaries);

COPY supervisor_salaries (town, supervisor, salary)
FROM 'C:\Users\Kevin\Downloads\supervisor_salaries.csv'
WITH (FORMAT CSV, HEADER);

INSERT INTO supervisor_salaries(town, county, supervisor, salary)
SELECT town, 'Some County', supervisor, salary
FROM supervisor_salaries_temp;

DROP TABLE supervisor_salaries_temp;