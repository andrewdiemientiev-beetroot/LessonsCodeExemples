import time


# def get_third_item(some_list):
#     return some_list[2]  # 1
#
#
# a = list(range(1100, 1200))  # 1
# big_list = list(range(1000, 10**6))  # 1
#
# begin = time.time()
# print(get_third_item(a))
# end = time.time() - begin
#
# begin1 = time.time()
# print(get_third_item(big_list))
# end1 = time.time() - begin1
#
# print(f"With a: {end}\nWith big_list: {end1}")

## Efficionsy O(n)
#
# # n
# def multiply(some_list, n):
#     result_list = []
#     # n
#     for item in some_list:
#         item *= n  # 1
#         result_list.append(item)
#     return result_list
#
#
# a = list(range(100))  # 1
# big_list = list(range(10**5))  # 1
#
#
# begin = time.time()
# print(multiply(a, 15))
# end = time.time() - begin
#
# begin1 = time.time()
# print(multiply(big_list, 15))
# end1 = time.time() - begin1
#
# print(f"With a: {end}\nWith big_list: {end1}")

# T(n) = n + 2

# T(n) = 1005 + 3*n + n^2
# O(n^2)



## Efficionsy O(n^2)

# n

def multiply(some_list, another_list):
    result_list = []
    # n
    for item in some_list:
        # n
        for item2 in another_list:
            item2 *= item  # 1
            result_list.append(item2)
    return result_list
    # n*n


a = list(range(100))  # 1
small_list = list(range(100))
big_list = list(range(10**6))  # 1


begin = time.time()
multiply(small_list, a)
end = time.time() - begin

begin1 = time.time()
multiply(big_list, a)
end1 = time.time() - begin1

print(f"With small_list: {end}\nWith big_list: {end1}")
