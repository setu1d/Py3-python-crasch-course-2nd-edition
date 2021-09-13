# coding: utf-8
"""
Created on 8.9.2021 15:50
@author: setu1d

"""


# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.

cubes = [number**3 for number in range(1,11)]

for cube in cubes:
    print(cube)