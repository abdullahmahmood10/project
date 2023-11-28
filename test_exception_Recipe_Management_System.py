import unittest
from unittest.mock import patch
from RecipeManagementSystem import RecipeManagementSystem, Recipe

class TestRecipeManagementSystem(unittest.TestCase):
    
    def setUp(self):
        self.testing = RecipeManagementSystem()

    def test_view_recipes(self):
        # It should raise an exception because there are no recipes to view
        with self.assertRaises(Exception):
            self.testing.view_recipes()

    @patch('builtins.input', side_effect=["Cake", "Flour, Egg, Milk", "Mix it well and bake", "Dessert", 8])
    def test_add_recipe(self, mock_input):
        # We put the rating more than 5 which should raise exception
        print("Testing Adding a Recipe")
        with self.assertRaises(Exception):
            self.testing.add_recipe()
    
    def test_delete_recipe(self):
        test_recipe = Recipe("Spaghetti", ["Pasta", "Tomato Sauce", "Meatballs"], "Boil pasta, cook sauce, add meatballs", "Italian", 5)
        self.testing.recipes.append(test_recipe)
        # We put wrong id, which should raise exception
        with patch('builtins.input', side_effect=[23]):
            with self.assertRaises(Exception):
                self.testing.delete_recipe() 
                

                
if __name__ == '__main__':
    unittest.main()
