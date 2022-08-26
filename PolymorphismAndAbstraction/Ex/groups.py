class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __add__(self, other):
        new_person = self.name + other.surname
        return new_person


p = Person('Pesho', 'Peshev')
p1 = Person('Ivan', 'Ivanov')
print(p + p1)
print(p)