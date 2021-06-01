# class Student:
#     def __init__(self, name: str, neighbor: "Student" = None):
#         self.name = name
#         if neighbor:
#             self.neighbor = neighbor
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.neighbor:
#             return self.neighbor
#         else:
#             raise StopIteration
#
#
# student1 = Student('Petia')
# student2 = Student('Vasia', neighbor=student1)
# student3 = Student('Kolia', neighbor=student2)


# def create_slogan(name: str) -> str:
#     if type(name) != str:
#         print(f'name is not type of str. Type of name: {type(name)}, data: {name}')
#     else:
#         return f"{name} drinks pepsi in his brand new BMW"
#
# #positive
# assert create_slogan("S@SH05") == "* drinks pepsi in his brand new *"
#
# # negative
# assert create_slogan([1, [2, 3]]) == None
import random


class Battery:
    def __init__(self):
        self.charge_level = 100

    def discharge(self):
        new_charge_level = random.randint(self.charge_level - 10, self.charge_level - 1)
        if new_charge_level > 0:
            self.charge_level = new_charge_level
        else:
            raise Exception('Battery has run out of charge. Please put new one.')


import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.battery = Battery()
        self.battery.discharge()

    def test_upper(self):
        self.assertTrue(self.battery.charge_level in range(90, 100))  # assert 'foo'.upper() == 'FOO'

    def test_negative(self):
        self.battery.charge_level = 'some sting'
        with self.assertRaises(TypeError):
            self.battery.discharge()

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())  # assert True
        self.assertFalse('Foo'.isupper())  # assert (not False)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()


