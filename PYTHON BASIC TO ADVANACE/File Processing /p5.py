# XML Parsing & Generation

import xml.etree.ElementTree as ET

name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")

student = ET.Element("student")

n = ET.SubElement(student, "name")
n.text = name

a = ET.SubElement(student, "age")
a.text = age

c = ET.SubElement(student, "city")
c.text = city

tree = ET.ElementTree(student)

tree.write("student.xml")

print("XML file created successfully!")
