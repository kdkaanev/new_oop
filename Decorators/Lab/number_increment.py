def number_increment(numbers):
    def increase():
        a = [x + 1 for x in numbers]
        return a

    return increase()


