# collections

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict


# namedtuple - Order structure
Order = namedtuple("Order", ["customer", "product", "price"])


orders = []


# User input
n = int(input("How many orders do you want to add: "))


for i in range(n):

    print("\nEnter Order", i+1)

    customer = input("Enter customer name: ")

    product = input("Enter product name: ")

    price = int(input("Enter product price: "))

    order = Order(customer, product, price)

    orders.append(order)



# Counter - Product sales count

product_list = []

for order in orders:
    product_list.append(order.product)

sales = Counter(product_list)


print("\nProduct Sales:")
print(sales)


# defaultdict - Customer order count

customer_orders = defaultdict(int)

for order in orders:
    customer_orders[order.customer] += 1


print("\nCustomer Order Count:")
print(customer_orders)



# deque - Delivery Queue

delivery_queue = deque()

for order in orders:
    delivery_queue.append(order.product)


print("\nDelivery Queue:")
print(delivery_queue)


delivered = delivery_queue.popleft()

print("Delivered Product:", delivered)



# OrderedDict - Order Report

report = OrderedDict()

report["Customer"] = orders[0].customer
report["Product"] = orders[0].product
report["Price"] = orders[0].price


print("\nOrder Report:")
print(report)
