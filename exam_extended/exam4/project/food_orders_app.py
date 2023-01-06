from meals.meal import Meal
from client import Client


class FoodOrdersApp:
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
        pass

    def show_menu(self):
        pass

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        pass

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
