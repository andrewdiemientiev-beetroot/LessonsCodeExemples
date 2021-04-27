




def add_3_numbers(a_local, b_local, c_local, d_local=0):
    return a_local + b_local + c_local + d_local


a = 5
b = 4
c = 3
d = 10
# print(add_3_numbers(c, b, a, d_local=d))


def combine():
    pass


def cook_meat():
    pass


def slice_product():
    pass


def create_burger(bread, meat, onion, tomato, cheese=None, souse=None):
    burger = None
    slice_product()
    cook_meat()
    burger = combine()
    return burger

# bread = 'Ginger bread'
bread = ['White', 'Ginger']
meat = None
onion = None
# cheese = None
tomato = None
big_tasty = create_burger(bread, meat, onion, tomato)


def func(*args, **kwargs):
    print(type(args))
    for arg in args:
        print(arg)

    print(type(kwargs))
    print(kwargs)
    print(kwargs['one'])
    return None


def combine_car(*args, **kwargs):
    pass


def create_belaz(kuzov, wheels_100):
    combine_car(kuzov, wheels_100)


func(1, 2, 3, 4, 5, 6, one=1, two=2, three=3)


l1 = lambda x, y: x + y
print(l1(10, 11))

# map()
# filter()

def myfunc(n):
  return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))