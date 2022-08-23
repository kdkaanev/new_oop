class Cat:
    def sound(self):
        print('sss')


class Dog:
    def sound(self):
        print('saa')


for any_type in Cat(), Dog():
    any_type.sound()


print(any_type.sound())
