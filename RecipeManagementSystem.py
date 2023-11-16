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
        
    def display_all_recipes(self):
        print("All Recipes:")
        for recipe in self.recipes:
            print(f"{recipe.id}. {recipe.name} - Category: {recipe.category}, Rating: {recipe.rating}")
            
    def search_by_keyword(self, keyword):
        matching_recipes = [recipe for recipe in self.recipes if keyword.lower() in recipe.name.lower()]
        if matching_recipes:
            print(f"Recipes containing '{keyword}':")
            for recipe in matching_recipes:
                print(f"{recipe.id}. {recipe.name} - Category: {recipe.category}, Rating: {recipe.rating}")
        else:
            print(f"No recipes found containing '{keyword}'.")            
    