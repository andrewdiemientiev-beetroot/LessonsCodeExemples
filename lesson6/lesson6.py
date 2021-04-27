# while True:
#     i += 1
#     print(i)
#
#     a = max(list_num
#     print(b)
#     if a != b:
#         print("Search...")
#     else:
#         print("The largest number in list_num is %s" % (b))
#         break


# import random
#
# list_num1 = [2, 5, 3, 6, 4, 1, 9, 7, 10, 8]
# random.shuffle(list_num1)
# random.shuffle(list_num1)
# print("list_num3 =", (list_num1))


# import random
# random_list_number = random.sample(range(1, 100), 10)
# print(f'The random list = {random_list_number}\nThe largest number form the list is {max(random_list_number)}!'
#       f'\nThe lower number from the list is {min(random_list_number)}')

# import random
# random_list1 = random.sample(range(1, 100), 10)
# random_list2 = random.sample(range(1, 100), 10)
# common_list = list(set(random_list1).intersection(random_list2))
# print(random_list1)
# print(random_list2)
# print(common_list)



# list1 = []
# for i in range(0, 100):
#     if i % 7 == 0 and i % 5 != 0:
#         list1.append(i)
# print(list1)


#lesson 5
# a = 4
# b = 4
# while a == b:
#     print(a, b)
#     a += 1

# s = iter(range(10, 1, -2))

# while True:
#     a = next(s)
#     print(a)

# s = list(range(10))
#
# for i in s:
#     i += 1
#     s.append(19)
#     print(i)

recipe = {'corn': 10, 'tomato': 2, 'rice': '6 cups', 'cheese': True, 'flour': ['1', 'cup'],
          'souse': {'milk': '1 cup', 'cream': '2 cups'}}


students = {'db': [{'name': 'Stas', 'points': 50}, {'name': 'Dima', 'points': 50}, {'name': 'Maks', 'points': 50}]}

a = {'key': 'value'}
# print(a['key'])
a['key'] = 'value2'
# print(a['key'])

a = {'key': 'value'}

from pprint import pprint

# pprint(dir(students))

# print(students.keys())


# for key in recipe:
#     print(key)

# print(list(recipe.keys()))
# print(recipe.items())
#
# for key, value in recipe.items():
#     print(key)
#     print(value)

# recipe_new = recipe.copy()
# recipe_new_2 = recipe.copy()
# print(id(recipe))
# print(id(recipe_new))
# pprint(recipe_new)
# recipe_new['corn'] = 2
# recipe_new['tomato'] = 10
# pprint(recipe_new)
# pprint(recipe)

# a = {}.fromkeys(['a', 'b', 'c'], 1)
# print(a)

# print(recipe.get('corn'))
# print(recipe['corn'])
# print(recipe.get('steak'))
# print(recipe['steak'])
#
# if not recipe.get('steak'):
#     answer = False
# cats = {'mainkun': 1}

# c = {'cat': 1}
# print(c)
# dogs = c.setdefault('dog', 2)
# print(dogs)
# print(c)

# apple = recipe.pop('apple', 3)
# print(apple)
# pprint(recipe)

# pprint(help(recipe.popitem))
# pprint(recipe)

# list1 = []
# for x in range(10):
#     list1.append(x**2)
#
# list2 = [x ** 2 for x in range(10)]
#
# print(list1)
# print(list2)

# list2 = [x ** 2 for x in range(10) if x % 2 == 0]
#
# print(list2)
#
# list3 = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
#
# print(list3)

keys = ['cat', 'dog']

c = {key: 'pet' for key in keys if key != 'dog'}
print(c)
# c = {key: 'pet' if key != 'dog' else for key in keys}
