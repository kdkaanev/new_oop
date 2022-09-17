class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.text = ''
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):

        while len(self.text) < self.number:

                self.text += self.sequence[self.idx]
                self.idx += 1
                return self.text
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
