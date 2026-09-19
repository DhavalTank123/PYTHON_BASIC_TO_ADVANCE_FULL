# itertools Using combinations, product, count

# Example: Online Shopping Product Combo Generator

from itertools import combinations, product, count

products = []

n = int(input("How Many Products: "))

for i in range(n):

	print("\nProduct", i+1)

	name = input("Enter Product Name: ")
	price = int(input("Enter Original Price: "))

	products.append({
		"name": name,
		"price": price
	})

colors = ["Black", "White"]

offer_id = count(1001)

discount = 20

print("\n======== Available Offers ===========")

for combo in combinations(products, 2):

	product_names = []

	total_price = 0

	for item in combo:
		product_names.append(item["name"])
		total_price += item["price"]

	offer_price = total_price - (total_price * discount / 100)

	for color in product(colors, repeat=1):

		print("-------------------------")
		print("Offer ID :", next(offer_id))
		print("Products: ",
			" + ".join(product_names))
		print("Color: ", color[0])
		print("Original Price: ₹", total_price)
		print("Discount: ", discount, "%")
		print("Offer Price: ₹", int(offer_price))