# coding: utf-8
"""
Created on 01.09.2021 16:04:29
@author: setu1d

"""
# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and you have space for only two guests.

# •	 Start with your program from Exercise 3-6. Add a new line that prints a 
# 	 message saying that you can invite only two people for dinner.

hostia = ['tesla', 'hossa', 'chara']

print(f"Nazdar {hostia[0].title()}, pozyvam ta ku stolu na veceru.")
print(f"Nazdar {hostia[1].title()}, pozyvam ta ku stolu na veceru.")
print(f"Nazdar {hostia[2].title()}, pozyvam ta ku stolu na veceru.\n")

print(f"Pani mame pre nas celu jachtu!\n")

# •	 Use insert() to add one new guest to the beginning of your list.
hostia.insert(0, "Laky")
# •	 Use insert() to add one new guest to the middle of your list.
hostia.insert(2, "Zuza")
# •	 Use append() to add one new guest to the end of your list
hostia.append("Milan")
# •	 Print a new set of invitation messages, one for each person in your list.
print("novy zoznam:\n")
print(f"{hostia[0].title()}, pozyvam ta na Jachtu!")
print(f"{hostia[1].title()}, pozyvam ta na Jachtu!")
print(f"{hostia[2].title()}, pozyvam ta na Jachtu!")
print(f"{hostia[3].title()}, pozyvam ta na Jachtu!")
print(f"{hostia[4].title()}, pozyvam ta na Jachtu!")
print(f"{hostia[5].title()}, pozyvam ta na Jachtu!\n")

print("Sorry guys, mame miesto len pre dvoch hosti\n")

# •	 Use pop() to remove guests from your list one at a time until only two 
#	 names remain in your list. Each time you pop a name from your list, print 
#	 a message to that person letting them know you’re sorry you can’t invite 
#	 them to dinner.

print(f"sorry {hostia.pop()}, nemame pre teba miesto")
print(f"sorry {hostia.pop()}, nemame pre teba miesto")
print(f"sorry {hostia.pop()}, nemame pre teba miesto")
print(f"sorry {hostia.pop()}, nemame pre teba miesto\n")

# •	 Print a message to each of the two people still on your list, letting them 
# 	 know they’re still invited.

print(f"{hostia[0].title()}, pre teba miesto zostalo.")
print(f"{hostia[1].title()}, pre teba miesto zostalo.\n")

#•	 Use del to remove the last two names from your list, so you have an empty 
#	 list. Print your list to make sure you actually have an empty list at the end 
#	 of your program.

del hostia[0]
del hostia[0]


#pouzil som funkciu len() pre zistenie stavu hosti
print(f"momentalny pocet ucastnikov na mojom pozyvacom zozname je: {len(hostia)}.")












