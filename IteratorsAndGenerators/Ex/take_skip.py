class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.result = - self.step
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.counter < self.count:
            self.result += self.step
            self.counter += 1
            return self.result

        else:
            raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
