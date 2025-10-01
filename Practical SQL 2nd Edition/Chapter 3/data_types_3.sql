
-- UNDERSTANDING DATA TYPES

-- Dates and Times

-- timestamp: Records date and time, which are useful for a range of
-- situations you might track.

-- date: Records just the date.

-- time: Records just the time.

-- interval: Holds a value representing a unit of time expressed in the
-- format quantity unit.

CREATE TABLE date_time_types(
    timestamp_column TIMESTAMP with time zone,
    interval_column interval
);

INSERT INTO date_time_types
VALUES ('2018-12-31 01:00 EST','2 days'),
    ('2018-12-31 01:00 -8','1 month'),
    ('2018-12-31 01:00 Australia/Melbourne','1 century'),
    (now(),'1 week');

SELECT * FROM date_time_types;

-- Using the interval Data Type in Calculations

SELECT timestamp_column, interval_column,
timestamp_column - interval_column AS new_date
FROM date_time_types;

-- Miscellaneous Types

-- A Boolean type that stores a value of true or false.
-- Geometric types that include points, lines, circles, and other twodimensional objects.
-- Network address types, such as IP or MAC addresses.
-- A Universally Unique Identifier (UUID) type, sometimes used as a
-- unique key value in tables.
-- XML and JSON data types that store information in those
-- structured formats.

-- Transforming Values from One Type to Another with CAST

SELECT timestamp_column, CAST(timestamp_column AS varchar(10))
FROM date_time_types;

SELECT numeric_column, CAST(numeric_column AS integer),
CAST(numeric_column AS varchar(6))
FROM number_data_types;

-- SELECT CAST(char_column AS integer) FROM char_data_types;

-- CAST Shortcut Notation

SELECT timestamp_column::varchar(10)
FROM date_time_types;