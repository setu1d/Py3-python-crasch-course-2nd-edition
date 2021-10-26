# coding: utf-8
"""
Created on 16.9.2021 9:59
@author: setu1d

"""

age = 72

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
    
print(f"Your admission cost is {price}.")