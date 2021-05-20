def logger(f):
    def func_logger(*args, **kwargs):
        print(f"{f.__name__}, called with {args, kwargs} parameters")
        return f(*args, **kwargs)
    return func_logger


@logger
def add_nums(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg**2 for arg in args[0]]


@logger
def print_some_shit(some_shit='Ginger'):
    print(some_shit)


print_some_shit(some_shit='Ninja')

list = [1, 2, 3, 4, 5]
add_nums(4, 5)
square_all(list)
