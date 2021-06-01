from typing import Sequence, Generator  # type: ignore

some_var: int = 10


# Class type annotation
class Person:

    def __init__(self, name: str, age: int = None):
        self.name = name
        self.age = age


class Granny(Person):
    def __init__(self, name: str, diseases: Sequence[str], age: int = None):
        super().__init__(name, age)
        self.diseases = diseases


def test(people: Sequence[Person]) -> Generator:
    # """
    # This is for test
    # :param names_list: This parameter is for name of user
    # :type names_list: str
    # :param age: This parameter is for age of user
    # :type age: int
    # :return: str value. Example "Hello, Andrew!"
    # """
    for person in people:
        msg = ''
        if isinstance(person, Granny):
            msg = 'Doctor doctor! '
        if person.age:
            yield msg + f'Hello, {person.name} and I am {person.age} old.'
        else:
            yield msg + f'Hello, {person.name}!'


generator_obj = test((
    Granny('Andrew', ['Skleros', 'Artrit', 'Alts gamer'], 96),
    Granny('Jessica', ['Tripper', 'Gonorea', 'Diarea'], 85)
))
for result in generator_obj:
    print(result)


# Sample of code for lesson 19
def open_file(file_name):
    with open(file_name, mode='w') as file_obj:
        test(file_obj)


def test(file_obj):
    file_obj.write()


@pytest.fixture
def test_open_file(file_name):
    return file_obj


def test_test(test_open_file):
    test(test_open_file)