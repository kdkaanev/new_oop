def type_check(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for el in args:
                if isinstance(el, type):
                        return func(*args)
                else:
                        return 'Bad Type'



        return wrapper
    return decorator





@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
