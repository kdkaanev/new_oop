import math


def is_prime(number):
    if number <= 1:
        return False
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    return is_prime


def get_primes(number):
    for num in number:
        if is_prime(number):
            yield num





print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))