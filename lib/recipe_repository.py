from lib.recipe import *

class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

# Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipe(row["id"], row["recipe_name"], row["cooking_minutes"], row["rating"])
            recipes.append(item)
        return recipes
    
# Find a single artist by their id
    def find(self, recipe_id):
        rows = self._connection.execute(
            'SELECT * from recipes WHERE id = %s', [recipe_id])
        row = rows[0]
        return Recipe(row["id"], row["recipe_name"], row["cooking_minutes"], row["rating"])
