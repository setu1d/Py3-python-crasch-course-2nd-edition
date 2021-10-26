# coding: utf-8
"""
Created on 26.10.2021 18:21
@author: setu1d

"""

available_toppings = ['mushrooms', 'olives', 'gree pepers',
                        'pepperoni', 'pineapple', 'extra cheese']
                        
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_toppings in requested_toppings:
    if requested_toppings in available_toppings:
        print(f"Adding {requested_toppings}.")
    else:
        print(f"Sorry, we don't have {requested_toppings}.")

print("\nFinished making your pizza!")