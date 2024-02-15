-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    recipe_name VARCHAR(255),
    cooking_minutes INT,
    rating INT
    );

-- Finally, we add any records that are needed for the tests to run
INSERT INTO recipes (recipe_name, cooking_minutes, rating) VALUES ('Lasagne', 40, 5);
INSERT INTO recipes (recipe_name, cooking_minutes, rating) VALUES ('Lamb Biryani', 30, 5);
INSERT INTO recipes (recipe_name, cooking_minutes, rating) VALUES ('Quiche Lorraine', 15, 1);
INSERT INTO recipes (recipe_name, cooking_minutes, rating) VALUES ('Fried Egg on Toast', 5, 3);
INSERT INTO recipes (recipe_name, cooking_minutes, rating) VALUES ('Roast Lamb & ALL the trimmings', 150, 5);
