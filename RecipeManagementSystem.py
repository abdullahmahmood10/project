import random 

class Recipe:
    def __init__ (self,recipe_id, name, ingredients, instructions, category, rating):
        self.id = recipe_id
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.category = category
        self.rating = rating

class RecipeManagementSystem:
    def __init__(self):
        self.recipes=[]

    def delete_recipe(self):
        if not self.recipes:
            print("No recipes found.")
            return
        self.display_all_recipes()
        recipe_id = int(input("Enter the ID of the recipe to delete: "))
        recipe = next((r for r in self.recipes if r.id == recipe_id), None)

        if recipe:
            self.recipes.remove(recipe)
            print(f"Deleted recipe: {recipe.name}")
        else:
            print("Recipe not found.")