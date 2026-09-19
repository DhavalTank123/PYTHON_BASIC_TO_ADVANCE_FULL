# functools Using reduce, partial, lru_cache

from functools import reduce, partial, lru_cache

@lru_cache()
def calculate_price(price):
	print("Calculating Price ...")
	return price

products = []

n = int(input("How many products do you want to add: "))

for i in range(n):

	print("\nProduct", i+1)
	name = input("Enter Product Name: ")
	price = int(input("Enter Product Price: "))

	products.append({
		"name": name,
		"price": price
	})

prices = []

for product in products:
	prices.append(
		calculate_price(product["price"])
	)

total_price = reduce(
	lambda x, y: x + y,
	prices
)

print("\nProduct List: ")

for product in products:
	print(
		product["name"],
		"₹",
		product["price"]
	)

print("\nOriginal Total Price: ₹", total_price)

def apply_discount(price, discount):
	return price - (price * discount / 100)

customer_offer = partial(
	apply_discount,
	discount=10
)

final_price = customer_offer(total_price)

print("Discount: 10%")

print("Final Price: ₹", int(final_price))