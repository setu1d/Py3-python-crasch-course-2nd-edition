# coding: utf-8
"""
Created on 26.10.2021 18:56
@author: setu1d

"""

# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
# not empty.
# •	 If the list is empty, print the message We need to find some users!
# •	 Remove all of the usernames from your list, and make sure the correct 
#    message is printed.


user_names = []

if user_names:
    for user_names in user_names:
        print(f"Hello {user_names.title()}, thank you for logging in again")

else:
    print('We need to find some users!')