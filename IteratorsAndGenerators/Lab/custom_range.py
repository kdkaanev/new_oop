class custom_range_iterator:
    def __init__(self,cr):
        self.cr = cr
        self.next_value = self.cr.start


    def __next__(self):
        if self.next_value > self.cr.end:
            raise StopIteration()

        i = self.next_value
        self.next_value += 1
        return i


class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return custom_range_iterator(self)



one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
