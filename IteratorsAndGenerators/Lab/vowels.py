class vowels:
    vowels_colection = ['e', 'y', 'u', 'i', 'o', 'a']

    def __init__(self, text):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            if self.text[self.index].lower() not in self.vowels_colection:
                self.index += 1
                continue
            char_to_return = self.text[self.index]
            self.index += 1
            return char_to_return
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
