# coding: utf-8
"""
Created on 01.09.2021 15:50:56
@author: setu1d

"""

# You just found a bigger dinner table, so now more space is 
# available. Think of three more guests to invite to dinner

# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print()
# call to the end of your program informing people that you found a bigger 
# dinner table.

hostia = ['tesla', 'hossa', 'chara']

host_1 = hostia[0].title()
pozvanka = f" Ahoj {host_1}, pozyvam ta na party!"
print(pozvanka)

host_2 = hostia[1].title()
pozvanka = f" Ahoj {host_2}, pozyvam ta na party!"
print(pozvanka)

host_3 = hostia[2].title()
pozvanka = f" Ahoj {host_3}, pozyvam ta na party!"
print(pozvanka,"\n")

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
print(f"{hostia[5].title()}, pozyvam ta na Jachtu!")








