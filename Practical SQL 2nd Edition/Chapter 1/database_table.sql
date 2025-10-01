
-- CREATING YOUR FIRST DATABASE AND TABLE

-- Creating a Table

--  When you create a table, you assign a name to each column
-- (sometimes referred to as a field or attribute) and assign it a data type.

-- The CREATE TABLE Statement

CREATE TABLE teachers(
    id bigserial,
    first_name varchar(25),
    last_name varchar(50),
    school varchar(50),
    hire_date date,
    salary numeric
);

-- Inserting Rows into a Table

-- The INSERT Statement

INSERT INTO teachers(first_name, last_name, school, hire_date, salary)
VALUES ('Janet', 'Smith', 'F.D. Roosevelt HS', '2011-10-30', 36200),
('Lee', 'Reynolds', 'F.D. Roosevelt HS', '1993-05-22', 65000),
('Samuel', 'Cole', 'Myers Middle School', '2005-08-01', 43500),
('Samantha', 'Bush', 'Myers Middle School', '2011-10-30', 36200),
('Betty', 'Diaz', 'Myers Middle School', '2005-08-30', 43500),
('Kathleen', 'Roush', 'F.D. Roosevelt HS', '2010-10-22', 38500);

-- Formatting SQL for Readability

-- Uppercase SQL keywords, such as SELECT. 
-- Avoid camel case and instead use lowercase_and_underscores for object
-- names, such as tables and column names.
-- Indent clauses and code blocks for readability using either two or four spaces.