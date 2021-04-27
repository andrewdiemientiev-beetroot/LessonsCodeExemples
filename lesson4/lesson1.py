from colorama import Fore, Back, Style
from prettytable import PrettyTable

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3}

price_banana = stock["banana"] * prices["banana"]
price_apple = stock["apple"] * prices["apple"]
price_orange = stock["orange"] * prices["orange"]
price_pear = stock["pear"] * prices["pear"]
total = price_pear + price_apple + price_orange + price_banana
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
table = PrettyTable()

table.title = "The cheque consists of: "

table.field_names = ["Title", "Amount", "Price for one piece", "Total cost"]

table.add_row([([key for key in stock.keys()][0]).title(), [value for value in stock.values()][0],
               float([value for value in prices.values()][0]), float(price_banana)])
table.add_row([([key for key in stock.keys()][1]).title(), [value for value in stock.values()][1],
               float([value for value in prices.values()][1]), float(price_apple)])
table.add_row([([key for key in stock.keys()][2]).title(), [value for value in stock.values()][2],
               float([value for value in prices.values()][2]), float(price_orange)])
table.add_row([([key for key in stock.keys()][3]).title(), [value for value in stock.values()][3],
               float([value for value in prices.values()][3]), float(price_pear)])

print(table)


# {[key for key in stock.keys()][0]}
# # from pprint import pprint
# # pprint(dir(dict))
# # print(help(dict))