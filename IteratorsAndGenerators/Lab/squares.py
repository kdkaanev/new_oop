def squares(n):
    start = 1
    while start < n + 1:
        yield start * start
        start += 1






print(list(squares(5)))
