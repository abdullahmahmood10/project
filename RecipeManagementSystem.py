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
             
    def filter_by_category(self, category):
        matching_recipes = [recipe for recipe in self.recipes if category.lower() == recipe.category.lower()]
        if matching_recipes:
            print(f"Recipes in category '{category}':")
            for recipe in matching_recipes:
                print(f"{recipe.id}. {recipe.name} - Rating: {recipe.rating}")
        else:
            print(f"No recipes found in category '{category}'.")      

    def filter_by_rating(self, rating):
        try:
            rating = int(rating)
            if 1 <= rating <= 5:
                matching_recipes = [recipe for recipe in self.recipes if recipe.rating == rating]
                if matching_recipes:
                    print(f"Recipes with rating {rating}:")
                    for recipe in matching_recipes:
                        print(f"{recipe.id}. {recipe.name} - Category: {recipe.category}")
                else:
                    print(f"No recipes found with rating {rating}.")
            else:
                print("Invalid rating. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Rating must be a number between 1 and 5.")  
            
            
    def view_recipes(self):
        if not self.recipes:
            print("No recipes found.")
        else:
            print("View Recipes\n")
            print("1. Display all recipes")
            print("2. Search by keyword")
            print("3. Filter by category")
            print("4. Filter by rating")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_all_recipes()
            elif choice == '2':
                keyword = input("Enter a keyword to search for: ")
                self.search_by_keyword(keyword)
            elif choice == '3':
                category = input("Enter a category to filter by: ")
                self.filter_by_category(category)
            elif choice == '4':
                rating = input("Enter a rating to filter by (1-5): ")
                self.filter_by_rating(rating)
            else:
                print("Invalid choice.")


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

    def export_recipes(self):
        if not self.recipes:
            print("No recipes found. There is nothing to export")
            return
        with open('recipes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Ingredients', 'Instructions', 'Category', 'Rating'])
            for recipe in self.recipes:
                writer.writerow([recipe.id, recipe.name, ', '.join(recipe.ingredients), recipe.instructions, recipe.category, recipe.rating])
        print("Recipes exported to recipes.csv")
        
    def import_recipes(self):
        with open('recipes.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                recipe_name = row[1]
                existing_recipe = next((r for r in self.recipes if r.name == recipe_name), None)

                if existing_recipe:
                    print(f"Recipe with name {recipe_name} already exists. Skipping import.")
                else:
                    imported_recipe = Recipe(row[1], row[2].split(', '), row[3], row[4], row[5])
                    self.recipes.append(imported_recipe)
                    print(f"Imported recipe '{imported_recipe.name}' with ID {imported_recipe.id}.")

        print("Recipes imported successfully!")