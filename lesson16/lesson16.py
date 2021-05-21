class CustomRange:

    def __init__(self, begin, end):
        self.counter = begin
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        return_value = self.counter
        if self.counter < self.end:
            self.counter += 1
        else:
            raise StopIteration
        return return_value

    # С помощью этого метода тоже можно создать генератор
    # def __getitem__(self):
    #     pass


c = CustomRange(0, 10)

print(list(c))


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


# def fibonacci():
#     prev, cur = 0, 1
#     while True:
#         yield prev
#         prev, cur = cur, prev + cur

import requests
import re


def get_pages(link):
    links_to_visit = []
    links_to_visit.append(link)
    while links_to_visit:
        current_link = links_to_visit.pop(0)
        page = requests.get(current_link)
        for url in re.findall('<a href="([^"]+)">', str(page.content)):
            if url[0] == '/':
                url = current_link + url[1:]
            pattern = re.compile('https?')
            if pattern.match(url):
                links_to_visit.append(url)
        yield current_link

webpage = get_pages('http://sample.com')
for result in webpage:
    print(result)


def summary(stock, prices):
    return sum(prices[k] * stock[k] for k in prices)


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