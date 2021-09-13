# coding: utf-8
"""
Created on 12.9.2021 19:29
@author: setu1d

"""

# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]

my_foods.append('cannoli')
friend_food.append('ice cream')

print("My favorite foods are: ")
for food in my_foods:
    print(f"- {food.title()}")

print("\nMy friend's favorite foods are: ")
for food in friend_food:
    print(f"- {food.title()}")