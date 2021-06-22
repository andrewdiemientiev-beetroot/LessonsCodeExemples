import timeit
#O(n)
def unsorted_sequential_search(some_list, value):
    pos = 0
    flag = False

    while pos < len(some_list) and not flag:
        if some_list[pos] == value:
            flag = True
        else:
            pos += 1

    return flag

# def poisk(some_list, value):
#     pos = 0
#     pos_list = []
#     while pos < len(some_list):
#         if some_list[pos] == value:
#             pos_list.append(pos)
#             pos += 1
#         else:
#             pos += 1
#     return pos_list, bool(pos_list)


def sorted_sequential_search(some_list, value):
    pos = 0
    flag = False
    stop = False

    while pos < len(some_list) and not flag and not stop:
        if some_list[pos] == value:
            flag = True
        else:
            if some_list[pos] > value:
                stop = True
            else:
                pos += 1

    return flag

#O(log n)
def binary_search(some_list, value):
    first = 0
    last = len(some_list) - 1
    flag = False

    while first <= last and not flag:
        midpoint = (first + last) // 2
        if some_list[midpoint] == value:
            flag = True
        else:
            if value < some_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return flag


print(timeit.timeit('sorted_sequential_search(list(range(3, 100000000, 4)), 500004)', number=100, setup='from __main__ import sorted_sequential_search'))
print(timeit.timeit('binary_search(list(range(3, 100000000, 4)), 5000000)', number=100, setup='from __main__ import binary_search'))


class Test:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __hash__(self):
        return hash((self.name, self.password))
