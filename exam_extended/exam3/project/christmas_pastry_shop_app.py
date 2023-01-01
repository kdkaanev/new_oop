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
        self.__validate_name_delicacy_exist(name, delcacy)

        delcacy = dd[delicacy_type](name, Delicacy.portion, price)
        self.delicacies.append(delcacy)
        return f"Added delicacy {name} - {delicacy_type} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        """
        *The method creates a booth of the given type and adds it to the booths' collection.*
                        *All booth numbers should be unique.*
            •


•	                Valid types of delicacies are: "Open Booth" and "Private Booth"

        :param type_booth:
            If a booth with that number exists:
                -raise an Exception with the following message: "Booth number {booth number} already exists!"
            If the booth type is not valid:
                -raise an Exception with the following message: "{type of booth} is not a valid booth!"
        :param booth_number:
             pass
        :param capacity:
            pass
        :return:
            Otherwise, create the booth, add it to the booths' list .
            return the following message: "Added booth number {booth number} in the pastry shop."

        """


    def reserve_booth(self, number_of_people: int):
        pass

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        pass

    def leave_booth(self, booth_number: int):
        pass

    def get_income(self):
        pass

    def __find_delcacy_by_name(self, name) -> Delicacy:
        for delcacy in self.delicacies:
            if delcacy.name == name:
                return delcacy

    def __validate_type_delicacy(self, type,dd):
            if type not  in dd:
                raise Exception(f"{type} is not on our delicacy menu!")

    @staticmethod
    def __validate_name_delicacy_exist(name, delcacy):
        if delcacy:
            raise Exception(f"{name} already exists!")


