from animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    @property
    def alowed_feed(self):
        return ['vegetables', 'fruits']


    @property
    def weight_incrace(self):
        return 0.10


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    @property
    def alowed_feed(self):
        return ['meat']


    @property
    def weight_incrace(self):
        return 0.40


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    @property
    def alowed_feed(self):
        return ['meat','vegetables']


    @property
    def weight_incrace(self):
        return 0.30


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!"

    @property
    def alowed_feed(self):
        return ['meat']


    @property
    def weight_incrace(self):
        return 1.00
