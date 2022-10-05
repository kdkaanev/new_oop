from re import L


def cache(func):
    def wrapper(n):
        def log():
            log ={}
            result = func(n)
            if n not in log:
                log[n] = result
        return log
    return wrapper

    

#@cache

def fibonacci(n):

    if n < 2:

        return n

    else:

        return fibonacci(n-1) + fibonacci(n-2)



fibonacci(3)
print(fibonacci.log)
