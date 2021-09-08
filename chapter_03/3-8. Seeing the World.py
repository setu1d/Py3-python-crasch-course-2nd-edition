# coding: utf-8
"""
Created on 01.09.2021 20:10:20
@author: setu1d

"""

# 3-8. Seeing the World:
# Think of at least five places in the world you’d like to visit.

# •	 Store the locations in a list.
#	 Make sure the list is not in alphabetical order
miesta = ['japonsko', 'himalaje', 'kanada', 'aljaska', 'thajsko']

# •	 Print your list in its original order.
#	 Don’t worry about printing the list neatly,
#	 just print it as a raw Python list
print(miesta)

# •	 Use sorted() to print your list in alphabetical 
#	 order without modifying the actual list.
print(sorted(miesta)) #abecedne poradie

# •	 Show that your list is still in its original order by printing it.
print(miesta)

# •	 Use sorted() to print your list in reverse alphabetical 
#	 order without changing the order of the original list.
print(sorted(miesta, reverse=True))

# •	 Show that your list is still in its original
#	 order by printing it again
print(miesta)

# •	 Use reverse() to change the order of your list.
#	 Print the list to show that its order has changed.
miesta.reverse()
print(miesta)

# •	 Use reverse() to change the order of your list again. 
#	 Print the list to show it’s back to its original order.
miesta.reverse()
print(miesta)

# •	 Use sort() to change your list so it’s stored in alphabetical order.
#	 Print the list to show that its order has been changed.
miesta.sort()
print(miesta)

# •	 Use sort() to change your list so it’s stored in reverse 
#	 alphabetical order. Print the list to show that its order has changed.
miesta.sort(reverse=True)
print(miesta)




