#!/usr/bin/python

# This file takes an IP address input, splits it, converts the values to binary and prints them

ipaddress = raw_input("Enter your IP address: ")

ipcomponents = ipaddress.split(".")
print(ipcomponents)

elements = []

for component in ipcomponents:
    componentint = int(component)
    componentbin = bin(componentint)
    elements.append(componentbin)

print elements
