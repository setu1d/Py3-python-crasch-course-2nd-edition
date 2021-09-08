# coding: utf-8
"""
Created on 01.09.2021 15:04:02
@author: setu1d
"""

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the 
# dinner, so you need to send out a new set of invitations. You’ll have to think of 
# someone else to invite.
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

# •	 Start with your program from Exercise 3-4. Add a print() call at the end 
# of your program stating the name of the guest who can’t make it.
nezucastneny = hostia.pop(1)
print (f"Bohuzial party sa nemoze zucastnit {nezucastneny.title()}...")

# •	 Modify your list, replacing the name of the guest who can’t make it with 
# the name of the new person you are inviting.
hostia.insert(2,'Pallfy')
print(f"pana {nezucastneny.title()} nahradi pan {hostia[2].title()}\n")

# •	 Print a second set of invitation messages, one for each person who is still 
# in your list.
print(f"Pan {hostia[0].title()}, pan {hostia[1].title()} a pan {hostia[2].title()}.\nPozyvam vas na vecernu party nie veceru!")








