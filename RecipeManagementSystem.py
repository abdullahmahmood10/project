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


    def add_recipe(self):
        name = input("Enter recipe name: ")
        
        existing_recipe = next((r for r in self.recipes if r.name.lower() == name.lower()), None)

        if existing_recipe:
            print(f"A recipe with the name '{name}' already exists. Please choose a different name.")
        else:
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = input("Enter instructions: ")
            category = input("Enter category: ")

            while True:
                try:
                    rating = int(input("Enter rating (1-5): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Rating must be between 1 and 5. Please try again.")
                except ValueError:
                    print("Invalid input. Rating must be a number between 1 and 5.")

            recipe = Recipe(name, ingredients, instructions, category, rating)
            self.recipes.append(recipe)
            print(f"Recipe '{recipe.name}' with ID {recipe.id} added successfully!")