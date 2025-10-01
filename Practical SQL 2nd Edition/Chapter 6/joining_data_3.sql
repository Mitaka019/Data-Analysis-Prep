
-- JOINING TABLES IN A RELATIONAL DATABASE

-- LEFT JOIN and RIGHT JOIN

SELECT *
FROM schools_left LEFT JOIN schools_right
ON schools_left.id = schools_right.id;

SELECT *
FROM schools_left RIGHT JOIN schools_right
ON schools_left.id = schools_right.id;

-- You want your query results to contain all the rows from one of the tables.

-- You want to look for missing values in one of the tables.

-- When you know some rows in a joined table won’t have matching values.

-- FULL OUTER JOIN

SELECT *
FROM schools_left FULL OUTER JOIN schools_right
ON schools_left.id = schools_right.id;

-- CROSS JOIN

-- In a CROSS JOIN query, the result (also known as a Cartesian product) lines up
-- each row in the left table with each row in the right table to present all
-- possible combinations of rows.

SELECT *
FROM schools_left CROSS JOIN schools_right;

-- Using NULL to Find Rows with Missing Values

SELECT * 
FROM schools_left LEFT JOIN schools_right
ON schools_left.id = schools_right.id
WHERE schools_right.id IS NULL;

-- Three Types of Table Relationships

-- One-to-One Relationship

-- One-to-Many Relationship

-- Many-to-Many Relationship

-- Selecting Specific Columns in a Join

SELECT schools_left.id,
    schools_left.left_school,
    schools_right.right_school
FROM schools_left LEFT JOIN schools_right
ON schools_left.id = schools_right.id;

-- Simplifying JOIN Syntax with Table Aliases

SELECT lt.id, lt.left_school, rt.right_school
FROM schools_left AS lt LEFT JOIN schools_right AS rt
ON lt.id = rt.id;

-- Joining Multiple Tables

CREATE TABLE schools_enrollment (
    id integer,
    enrollment integer
);

CREATE TABLE schools_grades (
    id integer,
    grades varchar(10)
);

INSERT INTO schools_enrollment (id, enrollment)
VALUES
    (1, 360),
    (2, 1001),
    (5, 450),
    (6, 927);

INSERT INTO schools_grades (id, grades)
VALUES
    (1, 'K-3'),
    (2, '9-12'),
    (5, '6-8'),
    (6, '9-12');

SELECT lt.id, lt.left_school, en.enrollment, gr.grades
FROM schools_left AS lt LEFT JOIN schools_enrollment AS en
    ON lt.id = en.id
LEFT JOIN schools_grades AS gr
    ON lt.id = gr.id;