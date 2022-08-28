from project.cat import Cat

class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age,gender='Female')


k = Kitten('a',2, 'ww')
print(k)