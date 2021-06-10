# def factorial(n):
#     if n == 0 or n == 1:
#         return n
#     return n*factorial(n-1)
#


# def factorial(n):
#     result = 1
#     while n > 0:
#         result *= n
#         n -= 1
#     return result


# print(factorial(4))


#1*2*3*4*...*n = n!


def to_str(number, base):
    convert_dict = {
        2: "01",
        10: "0123456789",
        16: "0123456789ABCDEF",
        8: "01234567"
    }
    convert_str = convert_dict[base]
    if number < base:
        return convert_str[number]
    else:
        return to_str(number // base, base) + convert_str[number % base]


print(to_str(77, 16))
