
-- CREATING YOUR FIRST DATABASE AND TABLE

-- Try It Yourself

-- 1

CREATE TABLE animals(
    id bigserial,
    animal_name varchar(50),
    scientific_name varchar(75),
    age numeric(3, 0),
    date_obtained date
);

-- 2

INSERT INTO animals(animal_name, scientific_name, age, date_obtained)
VALUES
('African Elephant', 'Loxodonta africana', 12.5, '2018-06-14'),
('Bengal Tiger', 'Panthera tigris tigris', 7.2, '2020-03-09'),
('Komodo Dragon', 'Varanus komodoensis', 4.8, '2021-11-25'),
('Scarlet Macaw', 'Ara macao', 2.1, '2023-01-30'),
('Giant Panda', 'Ailuropoda melanoleuca', 5.7, '2019-08-19'),
('King Cobra', 'Ophiophagus hannah', 3.4, '2022-05-02'),
('Green Sea Turtle', 'Chelonia mydas', 15.6, '2017-12-11'),
('Snow Leopard', 'Panthera uncia', 9.3, '2020-09-05'),
('Koala', 'Phascolarctos cinereus', 6.8, '2021-07-14'),
('Golden Eagle', 'Aquila chrysaetos', 11.0, '2019-04-21');