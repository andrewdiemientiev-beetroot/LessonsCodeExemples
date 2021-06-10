# class Stack:
#     def __init__(self):
#         self.items = []
#
#     # O(1)
#     def is_empty(self):
#         return self.items == []
#
#     # O(1)
#     def push(self, item):
#         self.items.append(item)
#
#     # O(1)
#     def pop(self):
#         return self.items.pop()
#
#     # O(1)
#     def peek(self):
#         return self.items[-1]
#
#     # O(n)
#     def size(self):
#         return len(self.items)
#
#
# def convert_to_bin(dec_number):
#     remstack = Stack()
#
#     while dec_number > 0:
#         rem = dec_number % 2
#         remstack.push(rem)
#         dec_number = dec_number // 2
#
#     bin_str = ""
#     while not remstack.is_empty():
#         bin_str = bin_str + str(remstack.pop())
#
#     return bin_str


# cn*2^n+...+c2*2^2+c1*2^1+c0*2^0 cn=[0,1]
# 8 = 0 * 2^0 + 0 * 2^1 + 0 * 2^2 + 1 * 2 ^ 3
# 8 = 1000
# 5 4 3 2 = 5 * 10 ^ 3 + 4 * 10 ^ 2 + 3 * 10 ^ 1 + 2 * 10 ^ 0
# 15 = 1 * 2 ^ 0 + 1 * 2 ^ 1 + 1 * 2 ^ 2 + 1 * 2 ^ 3
# 15 = 1111

# print(convert_to_bin(42))


# class Queue:
#     def __init__(self):
#         self.items = []
#
#     # O(1)
#     def is_empty(self):
#         return self.items == []
#
#     # O(n)
#     def enqueue(self, item):
#         self.items.insert(0, item)
#
#     # O(1)
#     def dequeue(self):
#         return self.items.pop()
#
#     # O(n)
#     def size(self):
#         return len(self.items)
#
#
# def hot_potato(namelist, num):
#     simqueue = Queue()
#     for name in namelist:
#         simqueue.enqueue(name)
#
#     # O(n * k)
#     while simqueue.size() > 1:
#         for i in range(num):
#             simqueue.enqueue(simqueue.dequeue())
#
#         simqueue.dequeue()
#
#     return simqueue.dequeue()
#
#
# print(hot_potato(["Susan", "Kent", "Brad", "Bill"], 3))


class Deque:
    def __init__(self):
        self.items = []

    # O(1)
    def is_empty(self):
        return self.items == []

    # O(1)
    def add_front(self, item):
        self.items.append(item)

    # O(n)
    def add_rear(self, item):
        self.items.insert(0, item)

    # O(1)
    def remove_front(self):
        return self.items.pop()

    # O(n)
    def remove_rear(self):
        return self.items.pop(0)

    # O(n)
    def size(self):
        return len(self.items)


def palchecker(some_str):
    chardeque = Deque()

    for ch in some_str:
        chardeque.add_rear(ch)

    still_equal = True

    while chardeque.size() > 1 and still_equal:
        first = chardeque.remove_front()
        last = chardeque.remove_rear()
        if first != last:
            still_equal = False

    return still_equal


print(palchecker("lsdkjfskf"))
print(palchecker("radar"))