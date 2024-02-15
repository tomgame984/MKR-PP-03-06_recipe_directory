class Recipe:
    def __init__(self, id, recipe_name, cooking_minutes, rating):
        self.id = id
        self.recipe_name = recipe_name
        self.cooking_minutes = cooking_minutes
        self.rating = rating
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Recipe({self.id}, {self.recipe_name}, {self.cooking_minutes}, {self.rating})"