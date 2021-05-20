# Example of factory
# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return f'Pizza({self.ingredients!r})'
#
#     @classmethod
#     def margherita(cls):
#         return cls(['mozzarella', 'tomatoes'])
#
#     @classmethod
#     def prosciutto(cls):
#         return cls(['mozzarella', 'tomatoes', 'ham'])

# import math
#
#
# class Pizza:
#     def __init__(self, radius, ingredients):
#         self.radius = radius
#         self.ingredients = ingredients
#
#     def __repr__(self):
#         return (f'Pizza({self.radius!r}, '
#                 f'{self.ingredients!r})')
#
#     def area(self):
#         return self.circle_area(self.radius)
#
#     @staticmethod
#     def circle_area(r):
#         return r ** 2 * math.pi
#
#     def protected_method(self):
#         print('Very securno!')
#
# p = Pizza(25, ['tomato', 'mozarella'])


# class SmartHouse:
#     def __init__(self, area, number_of_rooms, amount_of_flours):
#         self.area = area
#         self.number_of_rooms = number_of_rooms
#         self.amount_of_flours = amount_of_flours
#         self.people = []
#         self.temp_people_in_house = []
#
#     def new_people(self, people):
#         self.people.append(people)
#
#     def enter_the_house(self, person):
#         self._validate_person(person)
#         self.temp_people_in_house.append(person)
#
#     def good_night(self):
#         if self.temp_people_in_house:
#             self.__go_away()
#         else:
#             self.__turn_off_light()
#
#     def __go_away(self):
#         self.temp_people_in_house = []
#
#     def __turn_off_light(self):
#         pass
#
#     @staticmethod
#     def _validate_person(person):
#         if person == 'friend':
#             return True
#         else:
#             return False


# Class with property
# class C:
#     def __init__(self):
#         self._x = None
#
#     def getx(self):
#         return str(self._x)
#
#     def setx(self, value):
#         if value < 0:
#             raise Exception('Only positive numbers.')
#         self._x = value
#
#     def delx(self):
#         del self._x
#
#     x = property(getx, setx, delx, "I'm the 'x' property.")


# class Termometer:
#
#     def __init__(self, degree_system='C'):
#         self._degrees = 0
#         self.system = degree_system
#
#     def get_degrees(self):
#         if self.system == 'C':
#             return self._degrees
#         if self.system == 'K':
#             return self._degrees - 273
#         if self.system == 'F':
#             return self._degrees * 1.8 + 32
#
#     def set_degrees(self, value):
#         self._degrees = value
#
#     degrees = property(get_degrees, set_degrees)


# t = Termometer(degree_system='F')
# t.degrees = 25
# print(t.degrees)

# class C:
#     def __init__(self):
#         self._x = 100
#
#     @property
#     def x(self):
#         """I'm the 'x' property."""
#         print('Get x')
#         return self._x
#
#     @x.deleter
#     def x(self):
#         del self._x
#
#
# c = C()
# print(c.x)
# c.x = 100

# c = C()
# c.x = -10
# print(c.x)


class Square:

    def __init__(self, system='sm'):
        self.system = system
        self._height = 0
        self._wight = 0
        self._area = 0

    @property
    def height(self):
        if self.system == 'sm':
            return self._height
        if self.system == 'mm':
            return self._height * 0.1
        if self.system == 'm':
            return self._height * 10

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def width(self):
        return self._wight

    @width.setter
    def width(self, value):
        self._wight = value

    @property
    def area(self):
        return self._area
