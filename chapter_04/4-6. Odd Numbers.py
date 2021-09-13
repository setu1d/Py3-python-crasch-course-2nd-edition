# coding: utf-8
"""
Created on 8.9.2021 14:53
@author: setu1d

"""


# 4-6. Odd Numbers: Use the third argument of the range() function to make a
# list of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = []
for value in range(-1,21,2):
    odd = value + 2
    odd_numbers.append(odd)
    
print(odd_numbers)
                       
    
