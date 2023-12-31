import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        """
        Retorna o cardápio principal com base em uma restrição alimentar,
        se especificada.

        Args:
            restriction (str):
            Restrição alimentar a ser considerada no cardápio.
            Se não for especificada, retorna o cardápio completo.

        Returns:
            pd.DataFrame:
            DataFrame contendo as informações do cardápio, incluindo as colunas
            'dish_name', 'ingredients', 'price' e 'restrictions'.
        """
        if restriction:
            filtered_dishes = [
                dish
                for dish in self.menu_data.dishes
                if restriction not in dish.get_restrictions()
            ]
        else:
            filtered_dishes = self.menu_data.dishes

        dish_names = []
        ingredients = []
        prices = []
        restrictions = []

        for dish in filtered_dishes:
            dish_names.append(dish.name)
            ingredients.append(dish.get_ingredients())
            prices.append(dish.price)
            restrictions.append(dish.get_restrictions())

        menu_data = {
            "dish_name": dish_names,
            "ingredients": ingredients,
            "price": prices,
            "restrictions": restrictions,
        }

        return pd.DataFrame(menu_data)
