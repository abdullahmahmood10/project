import unittest
from unittest.mock import patch
from RecipeManagementSystem import RecipeManagementSystem, Recipe

class TestRecipeManagementSystem(unittest.TestCase):

    def setUp(self):
        self.testing = RecipeManagementSystem()

    def test_add_recipe(self):
        with patch('builtins.input', side_effect=["Lasagna", "Beef, Tomato Sauce, Pasta, Cheese", "Layer everything", "Italian", 4]):
            self.testing.add_recipe()
            self.assertEqual(len(self.testing.recipes), 1)

    def test_delete_recipe(self):
        test_recipe = Recipe("Spaghetti", ["Pasta", "Tomato Sauce", "Meatballs"], "Boil pasta, cook sauce, add meatballs", "Italian", 5)
        self.testing.recipes.append(test_recipe)
        
        with patch('builtins.input', side_effect=[test_recipe.id]):
            self.testing.delete_recipe()
            self.assertEqual(len(self.testing.recipes), 0)

    def test_edit_recipe(self):
        test_recipe = Recipe("Burger", ["Beef Patty", "Bun", "Lettuce", "Tomato"], "1. Cook patty 2. Assemble ingredients", "Fast Food", 4)
        self.testing.recipes.append(test_recipe)
        with patch('builtins.input', side_effect=[test_recipe.id, "Cheeseburger", "Beef Patty, Bun, Lettuce, Tomato, Cheese", "1. Cook patty 2. Assemble ingredients with cheese", "Fast Food", 5]):
            self.testing.edit_recipe()
            edited_recipe = self.testing.recipes[0]
            expected_ingredients = ["Beef Patty", "Bun", "Lettuce", "Tomato", "Cheese"]
            self.assertEqual(edited_recipe.name, "Cheeseburger")
            self.assertEqual([ingredient.strip() for ingredient in edited_recipe.ingredients], expected_ingredients)
            self.assertEqual(edited_recipe.instructions, "1. Cook patty 2. Assemble ingredients with cheese")
            self.assertEqual(edited_recipe.category, "Fast Food")
            self.assertEqual(edited_recipe.rating, 5)

    def test_search_by_keyword(self):
        test_recipe = Recipe("Chocolate Cake", ["Flour", "Sugar", "Cocoa Powder"], "1. Mix dry ingredients 2. Add wet ingredients 3. Bake", "Dessert", 4)
        self.testing.recipes.append(test_recipe)

        with patch('builtins.input', side_effect=["Chocolate"]):
            self.testing.search_by_keyword("Chocolate")

    def test_filter_by_category(self):
        test_recipe = Recipe("Caesar Salad", ["Lettuce", "Croutons", "Chicken", "Caesar Dressing"], "1. Mix all ingredients", "Salad", 5)
        self.testing.recipes.append(test_recipe)

        with patch('builtins.input', side_effect=["Salad"]):
            self.testing.filter_by_category("Salad")

    def test_filter_by_rating(self):
        test_recipe = Recipe("Smoothie", ["Banana", "Berries", "Yogurt", "Milk"], "1. Blend all ingredients", "Beverage", 3)
        self.testing.recipes.append(test_recipe)

        with patch('builtins.input', side_effect=[3]):
            self.testing.filter_by_rating(3)

    def test_export_recipes(self):
        with patch('builtins.input', side_effect=["Lasagna", "Beef, Tomato Sauce, Pasta, Cheese", "Layer everything", "Italian", 4]):
            self.testing.add_recipe()

        self.testing.export_recipes()
        
    def test_import_recipes(self):
        with patch('builtins.input', side_effect=["Lasagna", "Beef, Tomato Sauce, Pasta, Cheese", "Layer everything", "Italian", 4]):
            self.testing.add_recipe()

        self.testing.export_recipes()
        self.testing.import_recipes()
           

if __name__ == '__main__':
    unittest.main()


