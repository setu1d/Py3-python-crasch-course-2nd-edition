# coding: utf-8
"""
Created on 8.9.2021 15:36
@author: setu1d

"""
# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.

cubes = []
for number in range(1,11):
    cube = number**3        #1*1*1, 2*2*2, 3*3*3 .....
    cubes.append(cube)

        
for cube in cubes:
    print(cube)
    