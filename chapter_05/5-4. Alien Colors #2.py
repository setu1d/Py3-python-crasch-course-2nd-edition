# coding: utf-8
"""
Created on 17.9.2021 9:44
@author: setu1d

"""

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain.

# • If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
alien_color = 'green'

if alien_color == 'green':
    print('zasah, ziskavas 5 bodov')
else:
    print('ziskavas 10 bodov')


# • Write one version of this program that runs the if block and another that
# runs the else block.
alien_color = 'red'

if alien_color == 'green':
    print('zasah, ziskavas 5 bodov')
else:
    print('ziskavas 10 bodov')