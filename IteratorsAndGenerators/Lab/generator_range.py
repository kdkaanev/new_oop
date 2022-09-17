def genrange(start, end):
    index = start
    while index < end + 1:
        yield index
        index += 1


print(list(genrange(1, 10)))
