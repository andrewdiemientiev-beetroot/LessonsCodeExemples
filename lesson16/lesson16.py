import os

class CustomRange:

    def __init__(self, begin=0, end=None, step=1):
        if not end:
            raise Exception()
        self.counter = begin
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        return_value = self.counter
        if self.counter < self.end:
            self.counter += self.step
        else:
            raise StopIteration
        return return_value

    # С помощью этого метода тоже можно создать генератор
    # def __getitem__(self):
    #     pass

# c = CustomRange(0, 10)
#
# print(list(c))


# class CustomGetItemClass:
#     def __init__(self):
#         self.counter = 0
#
#     def __getitem__(self, l_item):
#         return (self.counter+1) * l_item
#
#
# c = CustomGetItemClass()
# for item in c:
#     print(item)

# class FibonacciGenerator:
#     def __init__(self):
#         self.prev = 0
#         self.cur = 1
#
#     def __next__(self):
#         result = self.prev
#         self.prev, self.cur = self.cur, self.prev + self.cur
#         return result
#
#     def __iter__(self):
#         return self

# import time
#
# f = FibonacciGenerator()
# for fib_number in f:
#     print(fib_number)
#     time.sleep(2)


def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur

import time
#
# for fib_number in fibonacci():
#     print(fib_number)
#     time.sleep(2)

# print(fibonacci())

# import requests
# import re
#
#
# def get_pages(link):
#     links_to_visit = []
#     links_to_visit.append(link)
#     while links_to_visit:
#         current_link = links_to_visit.pop(0)
#         page = requests.get(current_link)
#         for url in re.findall('<a href="([^"]+)">', str(page.content)):
#             if url[0] == '/':
#                 url = current_link + url[1:]
#             pattern = re.compile('https?')
#             if pattern.match(url):
#                 links_to_visit.append(url)
#         yield current_link
#
#
# webpage = get_pages('https://habr.com/ru/')
# for result in webpage:
#     print(result)
#     time.sleep(1)
#


def price_of_item(prices, stock):
    for key in prices:
        yield prices[key]*stock[key]


def summary(stock, prices):
    generator_exp = (prices[k] * stock[k] for k in prices)
    print(generator_exp)
    return sum(price_of_item(prices, stock))


print(summary({
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}, {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}))