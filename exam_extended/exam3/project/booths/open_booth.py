from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.50
    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)
        self.booth_number = booth_number
        self.capacity = capacity

    def reserve(self, number_of_people: int):
        reservation_price = self.booth_number *self.PRICE_PER_PERSON
        self.price_for_reservation += reservation_price
        self.is_reserved = True
