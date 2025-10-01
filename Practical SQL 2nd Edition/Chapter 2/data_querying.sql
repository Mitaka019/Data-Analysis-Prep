
-- BEGINNING DATA EXPLORATION WITH SELECT

-- Basic SELECT Syntax

SELECT * FROM teachers;

-- Querying a Subset of Columns

SELECT last_name, first_name, salary FROM teachers;

-- Using DISTINCT to Find Unique Values

SELECT DISTINCT school
FROM teachers;

SELECT DISTINCT school, salary
FROM teachers;

-- Sorting Data with ORDER BY

SELECT first_name, last_name, salary
FROM teachers
ORDER BY salary DESC;

SELECT last_name, school, hire_date
FROM teachers
ORDER BY school ASC, hire_date DESC;

-- Filtering Rows with WHERE

SELECT last_name, school, hire_date
FROM teachers
WHERE school = 'Myers Middle School';

-- First, we use the equals operator to find teachers whose first name is Janet

SELECT first_name, last_name, school
FROM teachers
WHERE first_name = 'Janet';

-- We list all school names in the table but exclude F.D. Roosevelt
-- HS using the not equal operator.

SELECT school
FROM teachers
WHERE school <> 'F.D. Roosevelt HS';

-- Here we use the less than operator to list teachers hired before January
-- 1, 2000.

SELECT first_name, last_name, hire_date
FROM teachers
WHERE hire_date < '2000-01-01';

-- We find teachers who earn $43,500 or more using the >= operator.

SELECT first_name, last_name, salary
FROM teachers
WHERE salary >= 43500;

-- The next query uses the BETWEEN operator to find teachers who earn
-- between $40,000 and $65,000.

SELECT first_name, last_name, school, salary
FROM teachers
WHERE salary BETWEEN 40000 AND 65000;

-- Using LIKE and ILIKE with WHERE

-- Percent sign (%) A wildcard matching one or more characters
-- Underscore (_) A wildcard matching just one character

SELECT first_name
FROM teachers
WHERE first_name LIKE 'sam%';

SELECT first_name
FROM teachers
WHERE first_name ILIKE 'sam%';

-- Combining Operators with AND and OR

SELECT *
FROM teachers
WHERE school = 'Myers Middle School' AND salary < 40000;

SELECT * 
FROM teachers
WHERE last_name = 'Cole' OR last_name = 'Bush';

SELECT *
FROM teachers
WHERE school = 'F.D. Roosevelt HS' AND
(salary < 38000 OR salary > 40000);

-- Putting It All Together

SELECT first_name, last_name, school, hire_date, salary
FROM teachers
WHERE school LIKE '%Roos%'
ORDER BY hire_date DESC;