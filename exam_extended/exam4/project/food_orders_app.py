from meals.dessert import Dessert
from meals.main_dish import MainDish
from meals.meal import Meal
from client import Client
from meals.starter import Starter


class FoodOrdersApp:
    type_meal = {
        "Starter": Starter,
        "MainDish": MainDish,
        "Dessert": Dessert
    }

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)
        if client.phone_number == client_phone_number:
            raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.clients_list.append(client)

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.type_meal.keys():
                self.menu.append(meal)

    def show_menu(self):
        result = ''
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        for meal in self.menu:
            result += meal.details() + '\n'
        return result.strip()


    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        meal_names = []
        client = self.__find_client_by_phone_number(client_phone_number)
        for name, quantiti in meal_names_and_quantities.items():
            meal = self.__find_meal_by_name(name)
            if meal not in self.menu:
                raise Exception(f"{name} is not on the menu!")
            client.shopping_cart.append(meal)
            client.bill += meal.price * quantiti
            meal.quantity -= quantiti
            meal_names.append(name)
        
        return f"Client {client_phone_number} successfully ordered {','.join(*meal_names)} for {client.bill}lv."


    def cancel_order(self, client_phone_number: str):
        pass

    def finish_order(self, client_phone_number: str):
        pass

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __find_client_by_phone_number(self, phone) -> Client:
        for client in self.clients_list:
            if client.phone_number == phone:
                return client

    def __find_meal_by_name(self, name) -> Meal:
        for meal in self.menu:
            if meal.name == name:
                return meal

