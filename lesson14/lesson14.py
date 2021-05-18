import time
from retry import retry
import random

from functools import lru_cache

@lru_cache
def count_vowels(sentence):
    sentence = sentence.casefold()
    return sum(sentence.count(vowel) for vowel in 'aeiou')


# class User:
#     def __init__(self, paid):
#         self.is_paid = paid
#
# user = User(True)
# user_not_paid = User(False)
#
#
# def paid_user(func):
#     def wrap_func(local_user):
#         if not local_user.is_paid:
#             raise Exception('Ny kupi Skyrim!')
#         return func(local_user)
#     return wrap_func
#
#
# @paid_user
# def get_paid_article(local_user):
#     return 'Paid article'
#
#
# @paid_user
# def get_paid_podcast(local_user):
#     return 'Paid podcast'


# result = get_paid_article(user)
# print(result)
# result2 = get_paid_article(user_not_paid)
#
# podcast = get_paid_podcast(user)
# no_podcast = get_paid_podcast(user_not_paid)

# now = time.time()
# print(count_vowels('Heeelo world asfksa;lksja;dlghsadngsdlfasd sdafkjhasdkdjfhs wekjfhskjfhdskjfh skfhafahkjsdhakjf kjshfsjfhskdjfhs kjasdhakjfhskdjfhskj asfkjhgkjs'))
# print(time.time() - now)
#
# print(count_vowels.cache_info())
#
# now = time.time()
# print(count_vowels('Heeelo world asfksa;lksja;dlghsadngsdlfasd sdafkjhasdkdjfhs wekjfhskjfhdskjfh skfhafahkjsdhakjf kjshfsjfhskdjfhs kjasdhakjfhskdjfhskj asfkjhgkjs'))
# print(time.time() - now)

# print(count_vowels.cache_info())


from functools import wraps

#

#
#
# @decorator_name
# def hello_world():
#     return 'Hello world'


# print(hello_world())
# print(hello_world)

# def repeat_capitalized_name(times):
#     def capitalize_names(func):
#         def func_wrapper(*args):
#             return (func(*args).upper() + '; ')*times
#         return func_wrapper
#     return capitalize_names


# from functools import wraps
#
#




# @repeat_capitalized_name(times=3)
# def get_fullname(firstname, lastname):
#     """
#     some docstrings
#     :param firstname:
#     :param lastname:
#     :return:
#     """
#     return "{}, {}".format(lastname, firstname)
#
# print(get_fullname('narko', 'man'))
#
# print(get_fullname)
# print(get_fullname.__name__)
# print(get_fullname.__doc__)


# @retry(IndexError, 3, delay=10)
# def hello_world():
#     if random.randint(0,2) == 1:
#         print('Index error')
#         raise IndexError
#     return 'Hello world'


# def repeat_capitalized_name(times):
#     def capitalize_names(func):
#         @wraps(func)
#         def func_wrapper(*args):
#             '''
#             Decorator doc string
#             '''
#             return (func(*args).upper() + '; ')*times
#         return func_wrapper
#     return capitalize_names

# def decorator_name(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         return f(*args, **kwargs)
#     return decorated

import time

begin = time.time()
end = time.time()
print(end - begin)