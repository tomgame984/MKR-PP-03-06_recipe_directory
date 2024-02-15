from lib.recipe_repository import *
from lib.recipe import *

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_recipes(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/recipes.sql") # Seed our database with some test data
    repository = RecipeRepository(db_connection) # Create a new ArtistRepository

    recipes = repository.all() # Get all artists

    # Assert on the results
    assert recipes == [
            Recipe(1, 'Lasagne', 40, 5),
            Recipe(2, 'Lamb Biryani', 30, 5),
            Recipe(3, 'Quiche Lorraine', 15, 1),
            Recipe(4, 'Fried Egg on Toast', 5, 3),
            Recipe(5, 'Roast Lamb & ALL the trimmings', 150, 5),
    ]

"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""
def test_get_single_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(5)
    assert recipe == Recipe(5, 'Roast Lamb & ALL the trimmings', 150, 5)

