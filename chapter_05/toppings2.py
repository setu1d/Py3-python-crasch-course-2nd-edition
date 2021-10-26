# coding: utf-8
"""
Created on 26.10.2021 15:35
@author: setu1d

"""

request_toppings = ['mushrooms', 'green peppers', 'extra chesse']

for request_toppings in request_toppings:
    if request_toppings == 'green peppers': #ak bude v zozname zelene korenie tak informujeme ze nemame
        print('Sorry, we are out of green pappers right now. ')
    else:
        print(f"Adding {request_toppings}.")

print("\nFinished making your Pizza!")