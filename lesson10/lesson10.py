from pprint import pprint
# this_variable = 0
# print(this_variable)
#
# def func3():
#     nonlocal this_variable
#     this_variable = 4
#
#     def func():
#         this_variable = 1
#
#         def func1():
#             nonlocal this_variable
#             this_variable = 3
#             print(this_variable)
#
#         func1()
#         print(this_variable)
#         # print(this_variable)
#     func()
#     print(this_variable)
#
# func3()
#
# def func4():
#     global this_variable
#     this_variable = 10
#     print(this_variable)
#     # print(this_variable)
#
# func4()
#
# def func3():
#     global this_variable
#     this_variable = 14
#     print(this_variable)
#     # print(this_variable)
#
# func3()
#


# def func2():
#     this_variable = 30
#     print(this_variable)
#     # print(this_variable)
#
#
# def func1():
#     this_variable = 25
#     print(this_variable)
#     # print(this_variable)
#
# func1()

# print(this_variable)

# func()



# class TestClass1:
#     this_variable = 1
#
#
# class TestClass2:
#     this_variable = 2
#
#     @staticmethod
#     def print_locals():
#         that_variable = 3
#         print(locals())


# pprint(globals())
# pprint(TestClass2.print_locals())

import time


class Student:
    name = "John Doe"
    age = None
    gender = None
    ICQ = None

    def __init__(self, name, age, gender, icq):
        self.name = name
        self.age = age
        self.gender = gender
        self.ICQ = icq

    def learning(self):
        print(f"{self.name} receiving knowledge...")
        time.sleep(5)
        print(f"Knowledge received.")
        print(self)
        self.multiply_to_2(1231)
        self.get_lenght([1, 2, 3, 4])

    @classmethod
    def send_to_list(cls):
        print(cls.name)
        print(cls.get_lenght([1, 2, 3, 4, 45]))

    @staticmethod
    def get_lenght(some_list):
        length = len(some_list)
        print(Student.multiply_to_2(length))

    @staticmethod
    def multiply_to_2(some_int):
        return 2*some_int


# print(Student.get_lenght([1, 2, 43, 4, 5, 6]))


student_obj = Student('Taras', 25, 'male', 111)
# print(student_obj.name)
# print(student_obj.age)
# print(student_obj.gender)
# print(student_obj.ICQ)
student_obj.learning()


class Physics:
    fall_acceleration = 9.81

    @classmethod
    def speed_of_fall(cls, weight):
        return weight*(cls.fall_acceleration**2)

    @classmethod
    def time_of_fall(cls, distance, weight):
        speed = cls.speed_of_fall(weight)
        return distance/speed
