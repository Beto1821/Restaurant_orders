import csv
from models.ingredient import Ingredient
from models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path) as csv_file:
            csv_reader = csv.reader(csv_file)
            header, *data = csv_reader
            dishes = {}  # Dictionary to store dishes

            for item in data:
                dish_name = item[0]
                price = float(item[1])
                ingredient_name = item[2]
                quantity = int(item[3])

                if dish_name not in dishes:
                    # Create a new Dish object if it doesn't exist
                    dishes[dish_name] = Dish(dish_name, price)

                # Get the Dish object from the dictionary
                dish = dishes[dish_name]
                # Create an Ingredient object
                ingredient = Ingredient(ingredient_name)
                # Add ingredient and quantity as a dependency to the dish
                dish.add_ingredient_dependency(ingredient, quantity)

            # Convert the dictionary values to a set
            # and assign it to self.dishes
            self.dishes = set(dishes.values())
