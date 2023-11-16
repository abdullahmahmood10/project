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