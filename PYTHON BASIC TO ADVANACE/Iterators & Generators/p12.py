# Real-World Use Cases 

# Use Case	     	    Generator Benefit
# Large Files    		Line-by-line processing
# Database	    		Record-by-record fetching
# ML Pipeline	    	Dataset streaming
# API Pagination	 	Page-by-page loading
# Video Processing		Frame-by-frame processing
# Web Scraping			One URL at a time
# Logs					Real-time monitoring
# Big Data				Less memory usage

import random 
import time

def temperature_sensor():

	while True:
		temperature = random.randint(15, 45)
		yield temperature
		time.sleep(1)

hot_limit = int(input("Enter hot temperature limit: "))
cool_limit = int(input("Enter cool temperature limit: "))
readings = int(input("How many readings you want: "))

sensor = temperature_sensor()
0
for i in range(readings):

	temp = next(sensor)

	print("\nCurrent Temperature:", temp)

	if temp > hot_limit:
		print("Warning: Temperature is too high!")

	elif temp < cool_limit:
		print("Warning: Temperature is too cool!")

	else:
		print("Temperature is normal")
