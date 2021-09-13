# coding: utf-8
"""
Created on 02.09.2021 12:36:44
@author: setu1d

"""

squares = []
for value in range(1, 11):
	squares.append(value**2)
	
print(squares)

####################################################

squares = [value**2 for value in range(1, 11)]
print(squares)
