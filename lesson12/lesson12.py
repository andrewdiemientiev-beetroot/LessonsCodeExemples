import random

# Polimorfism
class Cat:

    def __init__(self, name):
        self.name = name

    def voice(self):
        print(f'{self.name} said: "Meow!"')

    def mice_hunt(self):
        print(f'Today {self.name} cought {random.randint(1,10)}.')


class Dog:

    def __init__(self, name):
        self.name = name
        self.happiness = 0

    def voice(self):
        print(f'{self.name} said: "Owf!"')

    def feed(self, food):
        if self.happiness != 100:
            print(f'{food} is tasty!')
            self.happiness += 10
        else:
            print('I am full!')


cat = Cat('Vasilii')
dog = Dog('Juchka')

# for animal in (cat, dog):
#     animal.voice()
#     try:
#         animal.mice_hunt()
#     except Exception as ex:
#         print(ex)
#
#     try:
#         animal.feed('Kotleta')
#     except Exception as ex:
#         print(ex)

# s = 'str1' + 'str2'
# num = 1 + 2

# Static typing languages
# class AbstractClass:
#
#     def __init__(self):
#         pass
#
#     def sum(self, num1: int, num2: int):
#         pass
#
#
# class SumNumbers(AbstractClass):
#
#     def sum(self, num1: int, num2: int):
#         return num1 + num2
#
#
# class SumStr(AbstractClass):
#
#     def sum(self, num1: str, num2: str):
#         num1 = int(num1)
#         num2 = int(num2)
#         return num1 + num2


# Encapsulation
# class Bus:
#     limit_of_passengers = 54
#
#     def __init__(self, fuel):
#         self.fuel = fuel
#         self.amount_of_passengers = 0
#         print("Starting!")
#
#     def gather_passengers(self, passengers):
#         self.__stop_at_station()
#         if self.amount_of_passengers <= self.limit_of_passengers:
#             self.amount_of_passengers += passengers
#         self.__moving_to_next_station()
#
#     @staticmethod
#     def _stop_at_station():
#         print('Stoping at station.')
#
#     @staticmethod
#     def _moving_to_next_station():
#         print('All aboard. Moving to next station.')

#
class Whiskey:

    def __init__(self, name, whiskey_type='Single mold'):
        self.name = name
        self.whiskey_type = whiskey_type

    def __add__(self, other):
        if isinstance(other, Whiskey):
            return 'Jameson'
        else:
            return 'Drink vodka!'

    def __str__(self):
        return self.whiskey_type

    def __repr__(self):
        # return {'name': self.name, 'type': self.whiskey_type}
        return f"Name: {self.name}, type: {self.whiskey_type}"

    def __lt__(self, other):
        if isinstance(other, Whiskey):
            return 'Jameson'
        else:
            return 'Drink vodka!'


# print(cocktail)
# cocktail = jim_beam + 'Apple juice'
# print(cocktail)

#
whiskey_obj1 = Whiskey('Jameson')
whiskey_obj2 = Whiskey('Jim Beam')

print(whiskey_obj1 + whiskey_obj2)
print(whiskey_obj1 + 'Jim Beam')
