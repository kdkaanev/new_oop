import sys

from project.band import Band
from project.band_members.musician import Musician
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):

        self.bands = []
        self.musicians = []
        self.concerts = []
        self.musician_by_name = {}
        self.band_by_name = {}

    def create_musician(self, musician_type: str, name: str, age: int):
        musicians = self.__valid_type(musician_type)(name, age)
        self.musicians.append(musicians)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        self.__band_name_exist(name)
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        self.__concert_exist(place, genre)
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__search_musician_by_name(musician_name)
        band = self.__search_band_by_name(band_name)


        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        pass

    def start_concert(self, concert_place: str, band_name: str):
        pass

    @staticmethod
    def __valid_type(mode):
        if mode != Musician.type(mode):
            raise ValueError("Invalid musician type!")
        return getattr(sys.modules[__name__], mode)

    def __musician_name_exist(self, name):
        if name is getattr(self.musicians, name):
            raise Exception(f"{name} is already a musician!")

    def __band_name_exist(self, name):
        if name is getattr(self.bands, name):
            raise Exception(f"{name} band is already created!")

    def __concert_exist(self, name, gen):
        if name is getattr(self.concerts, name):
            raise Exception(f"{name} is already registered for {gen} concert!")

    def __search_musician_by_name(self, name):
        return self.musician_by_name[name]

    def __search_band_by_name(self, name):
        return self.band_by_name[name]

