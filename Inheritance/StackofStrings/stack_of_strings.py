class Stack:
    def __init__(self):
        self.data = []

    def validate_string(self, value):
        if not isinstance(value, str):
            raise TypeError('Only string add in Stack')

    def push(self, element):
        self.validate_string(element)
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return print( [str(self.data)])





stack = Stack()
stack.push("apple")
stack.push("carrot")






