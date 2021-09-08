# coding: utf-8
"""
Created on 
@author: setu1d

"""

#4-5. Summing a Million: 
#	  Make a list of the numbers from one to one million,
#	  and then use min() and max() to make sure your list actually
#	  starts at one and ends at one million. Also, use the sum() function
#	  to see how quickly Python can add a million numbers

one_million = list(range(1, 1000001))
min_val = min(one_million)
max_val = max(one_million)
sum_val = sum(one_million)

print(f"Min value: {min_val}")
print(f"Max value: {max_val}")
print(f"Sum: {sum_val}")
