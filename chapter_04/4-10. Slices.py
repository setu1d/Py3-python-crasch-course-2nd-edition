# coding: utf-8
"""
Created on 12.9.2021 18:57
@author: setu1d

"""

# 4-10. Slices: Using one of the programs you wrote in this chapter, add several 
# lines to the end of the program that do the following:
# •	 Print the message The first three items in the list are:. Then use a slice to 
# print the first three items from that program’s list.
# •	 Print the message Three items from the middle of the list are:. Use a slice to 
# print three items from the middle of the list.
# •	 Print the message The last three items in the list are:. Use a slice to print the 
# last three items in the list.

capely = ['prodigy', 'slipknot', 'sepultura', 'soul fly', 'metallica']
print("Toto je zoznam mojich prvych troch oblubenych skupin: \n",(capely[0:3]))
print("Toto su skupiny zo stredu mojho zoznamu: \n",(capely[1:4]))
print("Toto je zoznam mojich poslednych troch oblubenych skupin: \n",(capely[2:]))