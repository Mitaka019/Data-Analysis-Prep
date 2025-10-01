
-- UNDERSTANDING DATA TYPES

-- Numbers

-- Integers Whole numbers, both positive and negative

-- Fixed-point and floating-point Two formats of fractions of whole
-- numbers.

-- Integers

-- The SQL standard provides three integer types: smallint, integer, and
-- bigint. 

-- Auto-Incrementing Integers

CREATE TABLE people(
    id serial,
    person_name varchar(100)
);

-- Decimal Numbers

-- Fixed-Point Numbers

-- The fixed-point type, also called the arbitrary precision type, is
-- numeric(precision,scale).

-- Floating-Point Types

-- The real type allows precision to six decimal digits, and double precision to 15 decimal points of
-- precision, both of which include the number of digits on both sides of the point. 

CREATE TABLE number_data_types(
    numeric_column numeric(20, 5),
    real_column real,
    double_column double precision
);

INSERT INTO number_data_types
VALUES(.7, .7, .7),
(2.13579, 2.13579, 2.13579),
(2.1357987654, 2.1357987654, 2.1357987654);

SELECT * FROM number_data_types;

-- Trouble with Floating-Point Math

SELECT numeric_column * 1000000 AS "Fixed",
real_column * 1000000 AS "Float"
FROM number_data_types
WHERE numeric_column = .7;

