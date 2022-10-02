from functools import wraps


def even_parameters(func):
    @wraps(func)
    def wrapper(*args):
        for x in args:
            if not isinstance(x, int) or x % 2 != 0:
                return 'Please use only even numbers!'
        result = func(*args)
        return result
    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


# 6
# Please use only even numbers!


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
# 384
# Please use only even numbers!
print(add)