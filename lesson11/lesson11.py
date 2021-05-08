
class AbstractClassA:
    ABSTRACT_CLASS_VAR = 'TOO MANY ABSTRACTIONS'

    def __init__(self, outer_abstract_variable):
        self.abstract_variable = outer_abstract_variable

    def abstract_method(self):
        print(f'Abstract text with {self.abstract_variable}')

    @classmethod
    def abstract_class_method(cls):
        print(f'Class method {cls.ABSTRACT_CLASS_VAR}')

    @staticmethod
    def abstract_static_method():
        print('I am static method')


# abstract_object = AbstractClassA('Hatfield rules!')
# abstract_object.abstract_method()
# AbstractClassA.abstract_class_method()
# AbstractClassA.abstract_static_method()



# class Car:
#     name = None
#     engine_value = None
#     vin_code = None
#     transmission = None

    # _instance = None

    # def __new__(cls, *args, **kwargs):
    #     print(cls)
    #     print(cls._instance)
    #     print(isinstance(cls._instance, cls))
    #     if not isinstance(cls._instance, cls):
    #         cls._instance = object.__new__(cls)
    #     return cls._instance

    # def __init__(self, l_name, engine_value, l_vin_code, l_transmission):
    #     self.name = l_name
    #     self.engine = engine_value
    #     self.transmission = l_transmission
    #     self.vin_code = l_vin_code

    # def start_engine(self):
    #     if self.engine_value == '4.2':
    #         print('Viviviviviv')
    #     elif self.engine_value == '5.5':
    #         print('Drrrrrrrrrr')
    #     else:
    #         print('Pukpukpuk')

# class FreightCar(Car):
#     weight = None
#     type = None
#
#     def __init__(self, l_weight, l_type, l_name, l_engine, l_vin_code, l_transmission):
#         super().__init__(l_name, l_engine, l_vin_code, l_transmission)
#         self.weight = l_weight
#         self.type = l_type
#
#     def is_too_heavy(self, items_weight):
#         if self.weight < items_weight:
#             print('Too heavy, can not move.')
#             return True
#         return False
#
#
# class PassengerCar(Car):
#     type_of_carcass = None
#
#     def __init__(self, l_name, l_engine, l_vin_code, l_transmission, l_type_of_carcass):
#         super().__init__(l_name, l_engine, l_vin_code, l_transmission)
#         self.type_of_carcass = l_type_of_carcass
#
#     def too_many_passengers(self, passengers_amount):
#         if self.type_of_carcass == 'hachback':
#             return 7 > passengers_amount
#         elif self.type_of_carcass == 'sedan':
#             return 5 > passengers_amount
#         elif self.type_of_carcass == 'sportcar':
#             return 3 > passengers_amount
#         return False


# car1 = Car('ads', 'asd', 'asd', 'asd')
# f_car = FreightCar(50, 'Fura', 'Name', '5.5', '123123', 'manual')
#
# print(f_car.is_too_heavy(60))
# # print(car1.is_too_heavy(60))
# p_car = PassengerCar('Name', '5.5', '123123', 'auto', 'sportcar')
# print(p_car.too_many_passengers(2))
# print(p_car.too_many_passengers(3))

# class WaterCreature:
#     def __init__(self):
#         pass
#
#     def swimming(self):
#         print('i can swim.')
#
#     def breathing(self):
#         print('I can breath under water.')
#
#
# class GroundCreature:
#     def __init__(self):
#         pass
#
#     def crawling(self):
#         print('I can crawl')
#
#     def breathing(self):
#         print('I can breath on earth.')
#
#
# class Amphibian(GroundCreature, WaterCreature):
#
#     def breathing(self):
#         super(GroundCreature, self).breathing()
#
#
# amphibian_obj = Amphibian()
# amphibian_obj.crawling()
# amphibian_obj.swimming()
# amphibian_obj.breathing()


# class Parent(object):
#     def __init__(self):
#         print("parent")
#         super(Parent, self).__init__()
#
#
# class Left(Parent):
#     def __init__(self):
#         print("left")
#         super(Left, self).__init__()
#
#
# class Right(Parent):
#     def __init__(self):
#         print("right")
#         super(Right, self).__init__()
#
#
# class Child(Left, Right):
#     def __init__(self):
#         print("child")
#         super(Child, self).__init__()
#
#
# Child()


# Composition and agregation
class Engine:
    def __init__(self, engine_value):
        self.engine_value = engine_value

    def start_engine(self):
        if self.engine_value == '4.2':
            print('Viviviviviv')
        elif self.engine_value == '5.5':
            print('Drrrrrrrrrr')
        else:
            print('Pukpukpuk')


class ElectricEngine(Engine):
    def start_engine(self):
        print('........')


class DVS(Engine):
    pass


class Car:
    name = None
    engine = None
    vin_code = None
    transmission = None

    # Aggregation
    def __init__(self, l_name: str, engine_obj: Engine, l_vin_code: str, l_transmission: str):
        self.name = l_name
        self.engine = engine_obj
        self.transmission = l_transmission
        self.vin_code = l_vin_code

    def start_car(self):
        print('Turning key.')
        self.engine.start_engine()
        print('Engine started.')

    # Composition
    # def __init__(self, l_name, engine_value, l_vin_code, l_transmission):
    #     self.name = l_name
    #     self.engine = Engine(engine_value)
    #     self.transmission = l_transmission
    #     self.vin_code = l_vin_code


engine = DVS('2.2')
el_engine = ElectricEngine('100KW')
car = Car('Audi', engine, '121212', 'auto')
car1 = Car('Audi', el_engine, '121212', 'auto')
car.start_car()
