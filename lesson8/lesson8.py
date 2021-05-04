from pprint import pprint


def total_price():
	print("This program will calculate prices of items which u gonna enter next!\n")
	items = {}
	item_price = {}

	for i in range(4):
		keys1 = input("Enter an item: ")
		value = int(input("Enter a quantity of items: "))
		items[keys1] = value

	print("\nU have to enter the same items!\n")

	for keys2 in items:
		# keys2 = input("Enter an item: ")
		price = int(input(f"Enter a price for an item {keys2} $: "))
		item_price[keys2] = price

	stock_price = []

	for key in items:
		items_value = items[key]
		price_value = item_price[key]
		stock_price.append(items_value * price_value)
	total = sum(stock_price)

	print("*******************************")
	pprint(items, width = 20)
	pprint(item_price, width = 20)
	print("U have to pay : " + str(stock_price) + "$")
	print("********************************")

b = 0
c = ''
d = {'a': 10, 'b': 100, 'c': 20, 'd': 30, 'f': 50}
for key, value in d.items():
	if value > b:
		b = value
		c = key

