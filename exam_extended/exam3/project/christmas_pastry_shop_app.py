from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def add_delicacy(self, delicacy_type: str, name: str, price: float):
        """
            *The method creates a delicacy of the given type and adds it to the delicacies' collection.*
            *All delicacy names should be unique.*
            *Valid types of delicacies are: "Gingerbread" and "Stolen"*

        :param delicacy_type:  • If 'type_delicacy' is not valid:
                    -raise an Exception with the following message: "{type_delicacy} is not on our delicacy menu!"
        :param name: • If a delicacy with that 'name' exists:
                    -raise an Exception with the following message: "{name} already exists!"
        :param price:
         Otherwise, create the delicacy, add it to the delicacies' list, and return the following message:
        :return: "Added delicacy {delicacy name} - {type of delicacy} to the pastry shop."

        """
        dd = {
            "Gingerbread": Gingerbread,
            "Stolen": Stolen
        }

        delcacy = self.__find_delcacy_by_name(name)

        self.__validate_type_delicacy(delicacy_type, dd)
        self.__validate_name_delicacy_exist(delcacy, f"{name} already exists!")

        delcacy = dd[delicacy_type](name, Delicacy.portion, price)
        self.delicacies.append(delcacy)
        return f"Added delicacy {name} - {delicacy_type} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        """
        *The method creates a booth of the given type and adds it to the booths' collection.*
                        *All booth numbers should be unique.            •
•	                Valid types of booth are: "Open Booth" and "Private Booth"
        :param type_booth:

            If the booth type is not valid:
                -raise an Exception with the following message: "{type of booth} is not a valid booth!"
        :param booth_number:
             If a booth with that number exists:
                -raise an Exception with the following message: "Booth number {booth number} already exists!"
        :param capacity:
            pass
        :return:
            Otherwise, create the booth, add it to the booths' list .
            return the following message: "Added booth number {booth number} in the pastry shop."

        """
        valid_booth = {
            "Open Booth": OpenBooth,
            "Private Booth": PrivateBooth
        }
        booth = self.__find_booth_by_number(booth_number)

        self.__validate_boath_type(type_booth, valid_booth)
        self.__validate_boath_number_exist(booth,f"Booth number {booth_number} already exists!")

        booth = valid_booth[type_booth](booth_number, capacity)
        self.booths.append(booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        """
        Finds the first booth that is not reserved and whose capacity is enough for the number of people provided.
    	    If there is no such booth:
    	        -raise an Exception with the following message: "No available booth for {number of people} people!"
•	        else:
                -reserves the booth and return: "Booth {booth number} has been reserved for {number of people} people."
        """

        for i in range(len(self.booths)):
            if self.booths[i].is_reserved or self.booths[i].capacity < number_of_people:
                continue
            else:

                self.booths[i].reserve(number_of_people)
                return f"Booth {self.booths[i].booth_number} has been reserved for {number_of_people} people."
        else:
            raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        """
        :param booth_number: Finds the booth with the provided number
        :param delicacy_name: Finds delicacy with the provided name
            Orders the delicacy for that booth.
	        If there is no such booth:
	            -raise an Exception with the following message: "Could not find booth {booth_number}!"
            If there is no such delicacy:
                -raise an Exception with the following message: "No {delicacy_name} in the pastry shop!"
            else:
                -order the delicacy for that booth
                :return: "Booth {booth_number} ordered {delicacy_name}."
        """
        booth = self.__find_booth_by_number(booth_number)
        delicacy = self.__find_delcacy_by_name(delicacy_name)
        self.__validate_boath_number_not_exist(booth, booth_number, f"Could not find booth {booth_number}!")
        self.__validate_name_delicacy_not_exist(delicacy, delicacy_name, f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        """
            :param booth_number:
                -Finds the booth with the same booth's number (the booth's number will always be valid)
            Calculates the bill for that booth taking the price for reservation and all the price of all orders.
                -The bill is added to the pastry shop's total income.
            Removes all the ordered delicacies, frees the booth, and sets the price for reservation to 0.

            :return: "Booth {booth_number}:"
                    "Bill: {bill - formatted to the second decimal}lv."
        """
        booth = self.__find_booth_by_number(booth_number)
        bill = booth.price_for_reservation
        for delicacy in booth.delicacy_orders:
            bill += delicacy.price
        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0.0

        return f"Booth {booth_number}:" + '\n' + f"Bill: {bill:.2f}lv."


    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def __find_delcacy_by_name(self, name) -> Delicacy:
        for delcacy in self.delicacies:
            if delcacy.name == name:
                return delcacy

    @staticmethod
    def __validate_type_delicacy(type, dd):
        if type not in dd:
            raise Exception(f"{type} is not on our delicacy menu!")

    @staticmethod
    def __validate_name_delicacy_exist(delcacy, err_message):
        if delcacy:
            raise Exception(err_message)

    @staticmethod
    def __validate_name_delicacy_not_exist(delicacy, delicacy_name, err_message):
        if delicacy.name != delicacy_name:
            raise Exception(err_message)


    """
        booth metods
    """
    def __find_booth_by_number(self, booth_number) -> Booth:
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth

    @staticmethod
    def __validate_boath_type(type_booth, valid_boath):
        if type_booth not in valid_boath:
            raise Exception(f"{type_booth} is not a valid booth!")

    @staticmethod
    def __validate_boath_number_not_exist(booth, number, err_message):
        if number != booth.booth_number:
            raise Exception(err_message)

    @staticmethod
    def __validate_boath_number_exist(booth, err_message):
        if booth:
            raise Exception(err_message)

