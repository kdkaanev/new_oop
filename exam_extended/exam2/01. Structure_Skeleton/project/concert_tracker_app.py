from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    def __init__(self):

        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        musician_types = {

            "Guitarist": Guitarist,
            "Drummer": Drummer,
            "Singer": Singer
        }
        if musician_type not in musician_types:
            raise ValueError("Invalid musician type!")
        musician = self.__find_musician_by_name(name)
        if musician in self.musicians:
            raise Exception(f"{name} is already a musician!")

        musician = musician_types[musician_type](name, age)
        self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self.__find_band_by_name(name)
        if band in self.bands:
            raise ValueError(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.__find_concert_by_place(place)
        if concert in self.concerts:
            raise Exception(f"{place} is already registered for {genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician_by_name(musician_name)
        band = self.__find_band_by_name(band_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician_by_name(musician_name)
        band = self.__find_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        if musician not in band.members:
            raise Exception(f"{musician_name} isn't a musician!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        concert = self.__find_concert_by_place(concert_place)
        self.__validate_band_members(band)
        self.__validate_needed_skils(concert, band)
        profit = self.__calculate_profit(concert)
        return f"{band_name} gained {profit}$ from the {concert.genre} concert in {concert.place}."

    def __find_musician_by_name(self, name) -> Musician:
        for musician in self.musicians:
            if musician.name == name:
                return musician


    def __find_band_by_name(self, name) -> Band:
        for band in self.bands:
            if band.name == name:
                return band


    def __find_concert_by_place(self, place) -> Concert:
        for concert in self.concerts:
            if concert.place == place:
                return concert

    def __validate_band_members(self, band):
        members = set()
        for musician in band.members:
            members.add(musician.__class__.__name__)
        if len(members) < 3:
            raise f"{band.name} can't start the concert because it doesn't have enough members!"

    def __validate_needed_skils(self, concert, band):
        skilled_memmbers = True

        if concert.genre == "Rock":
            skills = {
                Drummer: 'play the drums with drumsticks',
                Singer: 'sing high pitch notes',
                Guitarist: 'play rock'

            }
            for musician in band.members:
                for skill in musician.learned_skills:
                    if skill not in skills.values():
                        skilled_memmbers = False
        elif concert.genre == "Metal":
            skills = {
                Drummer: 'play the drums with drumsticks',
                Singer: 'sing high pitch notes',
                Guitarist: 'play metal'

            }
            for musician in band.members:
                for skill in musician.learned_skills:
                    if skill not in skills.values():
                        skilled_memmbers = False
        elif concert.genre == "Jazz":
            skills = {
                Drummer: 'play the drums with drum brushes',
                Singer: ['sing high pitch notes', 'sing low pitch notes'],
                Guitarist: 'play jazz'

            }
            for musician in band.members:
                for skill in musician.learned_skills:
                    if skill not in skills.values():
                        skilled_memmbers = False
        if not skilled_memmbers:
            raise Exception(f"The {band.name} band is not ready to play at the concert!")

    def __calculate_profit(self, concert):
        return f'{(concert.audience * concert.ticket_price) - concert.expenses:.2f}'

