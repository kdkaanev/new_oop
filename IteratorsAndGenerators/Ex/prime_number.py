def is_prime(num):
    if num <= 1:
        return False
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    return is_prime


def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num





print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))