from functools import wraps
def multiply(times):
    @wraps(times)
    def decorator(*args, **kwargs):
        result = times(*args, **kwargs)

        return result * times

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))
