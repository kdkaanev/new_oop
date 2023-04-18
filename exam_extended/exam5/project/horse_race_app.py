from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    valid_horse_type = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def __validate_horse_name_exist(self, name):
        for horse in self.horses:
            if horse.name == name:
                raise Exception(f"Horse {name} has been already added!")

    def __validate_jokey_exist(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                raise Exception(f"Jockey {name} is added.")

    def __validate_horse_race_exist(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")

    def __find_jockey_by_name(self, name):
        for jockey in self.jockeys:
            if jockey.name == name:
                return jockey

    def __find_race_by_type(self,race_type) -> HorseRace:
        for race in self.horse_races:
            if race.race_type == race_type:
                return race

    def __winner(self, race)-> Jockey:
        winner_speed = 0
        winner = None
        for jockey in race.jockeys:
            if jockey.horse.speed > winner_speed:
                winner_speed = jockey.horse.speed
                winner = jockey
        return winner


    def __find_horce_by_type(self, horse_type)-> Horse:
        for i in range(len(self.horses) - 1, -1, -1):
            if self.horses[i].__class__.__name__ == horse_type:
                return self.horses[i]

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.valid_horse_type.keys():
            return
        self.__validate_horse_name_exist(horse_name)

        new_horse = self.valid_horse_type[horse_type](horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."
    """
    def add_jockey(self, jockey_name: str, age: int):
        self.__validate_jokey_exist(jockey_name)

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):

        self.__validate_horse_race_exist(race_type)

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        horse = self.__find_horce_by_type(horse_type)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        self.horses.remove(horse)
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race_by_type(race_type)
        jockey = self.__find_jockey_by_name(jockey_name)

        if race not in self.horse_races:
            raise Exception(f"Race {race_type} could not be found!")
        if jockey not in self.jockeys:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)

        if race not  in self.horse_races:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner = self.__winner(race)
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
    """

