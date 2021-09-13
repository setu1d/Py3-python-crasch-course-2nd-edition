# coding: utf-8
"""
Created on 13.9.2021 7:49
@author: setu1d

"""

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
# simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.
# • Try to modify one of the items, and make sure that Python rejects the change.
# • The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

menu = ('segedin', 'rizoto', 'svieckova', 'kapustnica', 'francuzske zemiaky')
print("V nasej restauracii ponukame z tychto jedal: ")
i=1
for jedlo in menu:
    print("menu",i,f" {jedlo.title()}")
    i=i+1
    
    
# Try to modify one of the items, and make sure that Python rejects the change
'''
menu = ('segedin', 'rizoto', 'svieckova', 'kapustnica', 'francuzske zemiaky')
menu[0] = 'kacafrc'
print(menu)
'''

# change menu
menu = ('segedin', 'rizoto', 'svieckova', 'kapustnica', 'francuzske zemiaky')
print("V nasej restauracii ponukame z tychto jedal: ")
i=1
for jedlo in menu:
    print("menu",i,f" {jedlo.title()}")
    i=i+1
    
menu = ('kacafrc', 'studeno', 'svieckova', 'kapustnica', 'francuzske zemiaky')
print("\nV nasej restauracii ponukame upravene menu: ")
i=1
for jedlo in menu:
    print(f"menu",i,f" {jedlo.title()}")
    i=i+1
