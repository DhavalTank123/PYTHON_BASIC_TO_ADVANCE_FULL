# datetime

import datetime

name = input("Enter your Name: ")

tickets = int(input("Enter number of tickets: "))

price = 200

total = tickets * price 

booking_time = datetime.datetime.now()

print("\n -------- Booking Details ---------")
print("Customer Name :", name)
print("Tickets: ", tickets)
print("Total Amount: ", total)
print("Booking Time:", booking_time)