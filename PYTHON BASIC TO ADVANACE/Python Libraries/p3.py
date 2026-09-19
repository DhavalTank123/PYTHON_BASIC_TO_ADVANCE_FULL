# CSV

import csv
import requests
from io import StringIO

# Online CSV URL
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"

# CSV download
response = requests.get(url)

# CSV reader માટે data તૈયાર કરવું
csv_file = StringIO(response.text, newline="")

reader = csv.DictReader(csv_file)

# User input
country_name = input("Enter country name: ")

found = False

for row in reader:
    if row["Country"].lower() == country_name.lower():
        print("Country:", row["Country"])
        print("Region:", row["Region"])
        found = True
        break

if not found:
    print("Country not found")

