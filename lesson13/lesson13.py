def hello_world():
    return 'Hello world'


# hello = 'Hello'
# hw_value = hello_world()
# print(hw)
# print(id(hello_world))
# print(id(hello))
# print(type(hello_world))
# print(type(hello))
# hw_function = hello_world
# print(id(hw_function))
# print(id(hello_world))
# print(id(hw_value))
# print(hw_function())


def kitty():
    return 'Hello kitty!'


# def get_hello_world_upper(hw_f):
#     return hw_f().upper()
#
#
# print(get_hello_world_upper(hello_world))
# print(get_hello_world_upper(kitty))


# some_list = [hello_world, kitty]
#
# for func in some_list:
#     print(func())


# some_dict = {'world': hello_world, 'kitty': kitty}
# print(some_dict['world']())

# def get_speak_func(text, volume):
#     def whisper():
#         return text.lower()
#
#     def yell():
#         return text.upper()
#
#     if volume < 0.5:
#         return whisper
#     else:
#         return yell


# speak_func = get_speak_func('I want vacation!', 1)
# print(speak_func())

l1 = []
for i in range(10):
    l1.append(i**2)
print(l1)

l2 = list(map(lambda x: x**2, range(10)))
print(l2)


def even_nums(x):
    return x % 2 == 0


input_values = [123, 32, 22, 5, 10, 3]

# for i in map(even_nums, input_values):
#     print(i)


filtered_list = list(filter(even_nums, input_values))

print(filtered_list)


from functools import reduce


a = reduce(lambda x, y: x-y, input_values)
print(a)