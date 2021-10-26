# coding: utf-8
"""
Created on 26.10.2021 15:47
@author: setu1d

"""

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")

# ak je prazdny zoznam opytame sa ci naozaj chce pizze bez..
else:
    print("Are you sure you want a plain pizza?")
