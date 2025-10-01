
-- UNDERSTANDING DATA TYPES

-- Characters

-- char(n): A fixed-length column where the character length is specified by n.

-- varchar(n): A variable-length column where the maximum length is specified by n. 

-- text: A variable-length column of unlimited length.

CREATE TABLE char_data_types(
    varchar_column varchar(10),
    char_column char(10),
    text_column text
);

INSERT INTO char_data_types
VALUES
('abc', 'abc', 'abc'),
('defghi', 'defghi', 'defghi');

