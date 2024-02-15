from lib.recipe import *

"""
Recipe constructs with an id, name, cooking time, rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test Recipe", 10, 5)
    assert recipe.id == 1
    assert recipe.recipe_name == "Test Recipe"
    assert recipe.cooking_minutes == 10
    assert recipe.rating == 5