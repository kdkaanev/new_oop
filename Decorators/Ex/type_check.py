def type_check(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for el in args:
                if isinstance(el, type):
                    try:
                        return func(*args)
                    except:'Bad Type'



        return wrapper





@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
