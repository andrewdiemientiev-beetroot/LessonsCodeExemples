#task 1
# text = input("Enter the sting: ")
# words = text.split()
# dict_text = dict()
#
# for word in words:
#     if word in dict_text:
#         dict_text[word] += 1
#     else:
#         dict_text[word] = 1
# print(dict_text)


# task 2.1
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15}
#
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3}
#
#
# total = dict()
# for key in stock:
#     total[key] = stock[key] * prices.get(key, 0)
# total_prices = sum(total.values())
# print(total_prices)

# task 3
# list_1 = []
# list_2 = []
# new_tuple = (list_1, list_2)
#
# for i in range(11):
#     list_1.append(i)
#     list_2.append(i * i)
#
# print(new_tuple)
#
# new_list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = [n * n for n in new_list_1]
# print(new_list_1, squares, sep="\n")
#
#
# print([(number, number ** 2) for number in range(11)])


# import numpy as np
# from pprint import pprint
# list_1 = list(range(11))
# list_2 = np.array(list_1) ** 2
# need_tuple = (list_1, list_2)
# print(need_tuple)

# task 2.2
# from colorama import Fore, Back, Style
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15}
#
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3}
#
# price_banana = stock["banana"] * prices["banana"]
# price_apple = stock["apple"] * prices["apple"]
# price_orange = stock["orange"] * prices["orange"]
# price_pear = stock["pear"] * prices["pear"]
# total = price_pear + price_apple + price_orange + price_banana
# stock_keys = list(stock.keys())
# stock_values = list(stock.values())
#
# print(Back.LIGHTBLACK_EX, Fore.CYAN, Style.DIM)
# print(f'The cheque consists of:'
#       f'\n\tTitle:\t\tAmount:\t\tPrice for one piece:\t\tCost:'
#       f'\n\t\t  {([key for key in stock.keys()][0]).title()}\t   {[value for value in stock.values()][0]}'
#       f'\t\t\t\t\t\t{float([value for value in prices.values()][0])}$'
#       f'\t\t\t {float(price_banana)}$')
# print(f'\t\t  {([key for key in stock.keys()][1]).title()}\t\t   {[value for value in stock.values()][1]}'
#       f'\t\t\t\t\t\t{float([value for value in prices.values()][1])}$'
#       f'\t\t\t {float(price_apple)}$')
# print(f'\t\t  {([key for key in stock.keys()][2]).title()}\t   {[value for value in stock.values()][2]}'
#       f'\t\t\t\t\t\t{float([value for value in prices.values()][2])}$'
#       f'\t\t\t {float(price_orange)}$')
# print(f'\t\t  {([key for key in stock.keys()][3]).title()}\t\t   {[value for value in stock.values()][3]}'
#       f'\t\t\t\t\t\t{float([value for value in prices.values()][3])}$'
#       f'\t\t\t {float(price_pear)}$')
#
# print(Fore.BLACK, Back.LIGHTRED_EX, Style.DIM)
# print(f'The total price of all fruits is {total}$')
#
# # task 2.3
# from prettytable import PrettyTable
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15}
#
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3}
#
# price_banana = stock["banana"] * prices["banana"]
# price_apple = stock["apple"] * prices["apple"]
# price_orange = stock["orange"] * prices["orange"]
# price_pear = stock["pear"] * prices["pear"]
# total = price_pear + price_apple + price_orange + price_banana
# table = PrettyTable()
#
# table.title = "The cheque consists of: "
#
# table.field_names = ["Title", "Amount", "Price for one piece", "Total cost"]
#
# table.add_row([([key for key in stock.keys()][0]).title(), [value for value in stock.values()][0],
#                float([value for value in prices.values()][0]), float(price_banana)])
# table.add_row([([key for key in stock.keys()][1]).title(), [value for value in stock.values()][1],
#                float([value for value in prices.values()][1]), float(price_apple)])
# table.add_row([([key for key in stock.keys()][2]).title(), [value for value in stock.values()][2],
#                float([value for value in prices.values()][2]), float(price_orange)])
# table.add_row([([key for key in stock.keys()][3]).title(), [value for value in stock.values()][3],
#                float([value for value in prices.values()][3]), float(price_pear)])
#
# print(table)

#task 1
# your_string = input("input your string\n")
# words_list = your_string.split(' ')
# num_of_words_dict = {i: words_list.count(i) for i in words_list if i != ''}
# print(num_of_words_dict)

#task 2
from prettytable import PrettyTable

# stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
# prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
# stocknames = list(stock.keys())
# pricesnames = list(prices.keys())
# stocknum = list(stock.values())
# pricesnum = list(prices.values())
# total = 0
# table = PrettyTable()
# table.field_names = ["Title:", "Amount:", "Price for one piece:", "Cost:"]
# for i in range(len(stocknames)):
#     table.add_row([stocknames[i], stocknum[i], pricesnum[i], stocknum[i] * pricesnum[i]])
#     total += stocknum[i] * pricesnum[i]
# print(table)
# print("Total price:", total)

# task 3
# print([(i, i ** 2) for i in range(1, 11)])

#task 1
# my_string = input("Insert a string: ").split()
# print({i: my_string.count(i) for i in my_string})

#task 2
# def summary(stock, prices):
#     return sum(prices[k] * stock[k] for k in prices)

# print(summary({
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }, {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }))

#task 3
# print([(i, i ** 2) for i in range(1, 11)])