import itertools


def possible_permutations(elements):
    for result in itertools.permutations(elements):
        yield list(result)





[print(n) for n in possible_permutations([1, 2, 3])]