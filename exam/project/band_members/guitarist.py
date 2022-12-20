from project.band_members.musician import Musician


class Guitarist(Musician):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.can_learn = ["play metal", "play rock", "play jazz"]

    def learn_new_skill(self, new_skill: str):
        if new_skill not in self.can_learn:
            raise ValueError(f"{new_skill} is not a needed skill!")
        Musician.learn_new_skill(new_skill)
    @property
    def type(self):
        return "Guitarist"

