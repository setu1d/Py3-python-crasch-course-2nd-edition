# coding: utf-8
"""
Created on 17.9.2021 9:13
@author: setu1d

"""

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

# • Write an if statement to test whether the alien’s color is green. If it is, print
#   a message that the player just earned 5 points.
alien_color = 'green'

if alien_color == 'green':
    print('zasah, ziskavas 5 bodov')
else:
    print('minul si')
        
# • Write one version of this program that passes the if test and another that
#   fails. (The version that fails will have no output.)
alien_colors = 'yellow'
if alien_color == 'red':
    print('zasah, ziskavas 5 bodov')
else:
    print('minul si')