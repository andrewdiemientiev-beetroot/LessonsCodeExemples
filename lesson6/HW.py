#task 1
input_string = input("input your string\n")
list_of_words = input_string.split()
num_of_words_dict = {i: list_of_words.count(i) for i in list_of_words if i != ''}
print(num_of_words_dict)

#task 2
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock_sum = sum([stock[key]*prices[key] for key in stock])
print("Total price:", stock_sum)

# task 3
print([(i, i ** 2) for i in range(1, 11)])
