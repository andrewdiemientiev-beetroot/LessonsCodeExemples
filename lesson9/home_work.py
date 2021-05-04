def oops():
    a = [1, 2]
    return print(a[3])


def some_func():
    try:
        oops()
    except IndexError:
        print(f'oops() Ooops has an index error')
    return


some_func()

##############################################################################################


def oops():
    a = {'key': 'value'}
    return print(a['key2'])


def some_func():
    try:
        oops()
    except IndexError:
        print(f'oops() Ooops has an index error')
    return


some_func()

##############################################################################################

# task 2
def sum_two_nums(num1, num2):  # call the function
    try:  # try except construction
        num1 = int(num1)
        num2 = int(num2)
        result = num1 ** 2 / num2
        print(f'Result of ({num1} power 2) divided by {num2} is {result}')  # print result if our user correctly input variables
    except ValueError:  # use value error exception for pull out all non digits elements
        print('Value error, use digits')  # print type of except for user
    except ZeroDivisionError:  # use zero division error exception because we can not divide by zero
        print('ZeroDivision Error, you can`t divide by zero')  # print type of except for user


def main():
    num1 = input('Input first number\na= ')  # user input number called a
    num2 = input('Input second number\nb= ')  # user input number called b
    sum_two_nums(num1, num2)


if __name__ == '__main__':
    main()











