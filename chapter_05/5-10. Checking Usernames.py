# coding: utf-8
"""
Created on 26.10.2021 19:07
@author: setu1d

"""

# 5-10. Checking Usernames: Do the following to create a program that simulates 
# how websites ensure that everyone has a unique username.

#•	 Make a list of five or more usernames called current_users.
current_users = ['mirec', 'laky', 'zuza', 'puco', 'pisko']

#•	 Make another list of five usernames called new_users. Make sure one or 
#    two of the new usernames are also in the current_users list
new_users = ['minister', 'laky', 'eso', 'karida', 'pisko']

# •	 Loop through the new_users list to see if each new username has already 
#    been used. If it has, print a message that the person will need to enter a 
#    new username. If a username has not been used, print a message saying 
#    that the username is available.
for new_users in new_users:
    if new_users in current_users:
        print(f'Meno {new_users.title()} je uz obsadene. Prosim zadajte nove meno ')
    else: 
        print(f"Pouzivatelske meno: {new_users.title()} je k dispozicii")

