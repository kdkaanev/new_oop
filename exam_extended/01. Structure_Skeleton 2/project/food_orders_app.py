from project.meals.meal import Meal
from project.client import Client


class FoodOrdersApp:
    MIN_NUMBERS_IN_MENU = 5
    CLIENT_EXIST_ERROR_MESSAGE = "The client has already been registered!"
    MENU_ERROR_MESSAGE = "The menu is not ready!"

    def __init__(self):
        self.menu = []
        self.meal_dict = {}
        self.clients_list = []
        self.client_dict = {}

    def register_client(self, client_phone_number: str):
        '''
        Creates a client (object) and :
          - Adds it to the client list and returns the message "Client {phone_number} registered successfully."
          -If a client with the same phone number is already registered, raise an Exception with the message "The client has already been registered!"

        '''

        client = self.__client_by_phone_number(client_phone_number)

        if client:
            raise Exception(self.CLIENT_EXIST_ERROR_MESSAGE)
        client = Client(client_phone_number)
        self.clients_list.append(client)
        self.client_dict[client.phone_number] = client

    def add_meals_to_menu(self, *meals: Meal):
        '''
            This method adds all the meals (objects) given to the menu list.
                -If one or more of the provided objects are NOT meals (not a "Starter", a "MainDish", or a "Dessert")
                 ignore them and keep adding only the meals.

                Note: you will always be given meals with different names.
        '''
        for item in meals:
            if item == Meal.name:
                self.menu.append(item)
                self.meal_dict= item

    def show_menu(self):
        '''
            It should return the details() for each meal on the menu on separate lines
                -If there are less than 5 meals on the menu:
                    raise an Exception with the message "The menu is not ready!"
        '''
        self.__validate_menu_full()
        for meal in self.menu:
            return meal.details()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        client = self.__client_by_phone_number(client_phone_number)
        self.__validate_menu_full()
        self.__validate_client_exist(client, client_phone_number)
        self.__validate_meal_in_menu(**meal_names_and_quantities)
        for name, quantities in meal_names_and_quantities.items():
            meal = self.__meal_by_name(name)
            if quantities < meal.quantities:
                raise Exception(f"Not enough quantity of {meal.__name__}: {meal.name}!")

    def cancel_order(self, client_phone_number: str):
        pass

    def finish_order(self, client_phone_number: str):
        pass

    def __str__(self):
        pass

    def __client_by_phone_number(self, client_phone_number):
        return self.client_dict.get(client_phone_number, None)

    def __validate_menu_full(self):
        if len(self.menu) < self.MIN_NUMBERS_IN_MENU:
            raise Exception(self.MENU_ERROR_MESSAGE)

    def __validate_client_exist(self, client, number):
        if client not in self.clients_list:
            client = Client(number)
            self.clients_list.append(client)
            self.client_dict[client.phone_number] = client

    def __validate_meal_in_menu(self, **kwargs):
        for meal_name, meal_quantity in kwargs.items():
            if meal_name not in self.menu:
                raise f"{meal_name} is not on the menu!"
            elif meal_quantity > self.menu[meal_quantity]:
                raise f"Not enough quantity of {self.menu.__class__}: {meal_name}!"

    def __meal_by_name(self, name):
        return self.meal_dict.get(name, None)
