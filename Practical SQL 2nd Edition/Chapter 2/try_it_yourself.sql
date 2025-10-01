
-- BEGINNING DATA EXPLORATION WITH SELECT

-- Try It Yourself

-- 1

SELECT last_name, first_name, school
FROM teachers
ORDER BY school ASC, last_name ASC;

-- 2

SELECT first_name, salary
FROM teachers
WHERE first_name ILIKE 'S%'
AND salary > 40000;

-- 3

SELECT last_name, first_name, salary, hire_date
FROM teachers
WHERE hire_date > '2010-01-01'
ORDER BY salary DESC;