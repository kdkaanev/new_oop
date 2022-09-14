class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


    def animal_sound(animals: list):
        for animal in animals:
            if animal.species == 'cat':
                print('meow')
            elif animal.species == 'dog':
                print('woof-woof')

class AddAnimal(Animal):
    def animal_sound(animals: list):
        pass



animals = [Animal('cat'), Animal('dog')]
an = Animal(animals)
print(an.animal_sound(animals))

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
