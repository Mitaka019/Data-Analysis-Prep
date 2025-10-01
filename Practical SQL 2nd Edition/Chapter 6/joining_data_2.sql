
-- JOINING TABLES IN A RELATIONAL DATABASE

-- JOIN Types

-- JOIN Returns rows from both tables where matching values are found
-- in the joined columns of both tables.

-- LEFT JOIN Returns every row from the left table plus rows that match
-- values in the joined column from the right table.

-- RIGHT JOIN Returns every row from the right table plus rows that match
-- the key values in the key column from the left table. 

-- FULL OUTER JOIN Returns every row from both tables and matches rows.

-- CROSS JOIN Returns every possible combination of rows from both tables.

CREATE TABLE schools_left (
    id integer CONSTRAINT left_id_key PRIMARY KEY,
    left_school varchar(30)
);

CREATE TABLE schools_right (
    id integer CONSTRAINT right_id_key PRIMARY KEY,
    right_school varchar(30)
);

INSERT INTO schools_left (id, left_school) VALUES
    (1, 'Oak Street School'),
    (2, 'Roosevelt High School'),
    (5, 'Washington Middle School'),
    (6, 'Jefferson High School');

INSERT INTO schools_right (id, right_school) VALUES
    (1, 'Oak Street School'),
    (2, 'Roosevelt High School'),
    (3, 'Morrison Elementary'),
    (4, 'Chase Magnet Academy'),
    (6, 'Jefferson High School');

-- JOIN

SELECT * 
FROM schools_left JOIN schools_right
ON schools_left.id = schools_right.id;

