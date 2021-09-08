
print('\033[1m' + "2-3. Personal Message:" + '\033[0m')
name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message, "\n") 
 

print('\033[1m' + "2-4. Name Cases:" + '\033[0m')
first_name = "miroslav"
last_name = "gensor"
full_name = f"{first_name} {last_name}"
names = f"{full_name.lower()} \n{full_name.upper()} \n{full_name.title()}"
print(names, "\n")


#################################################################################
#Author:		setu1d
#Date:			26-08-2021
#Description: 	vypisanie citatu oblubenej osobnosti pomocou f-stringu
#################################################################################
print('\033[1m' + "2-5. Famous Quote 1+2:" + '\033[0m')
famous_person = "nikola tesla"
message2 = "\tNetrápi ma, že mi ukradli nápad. \n\tTrápi ma, že nemajú žiadne vlastné."
citat = f"{message2} \n\t\t\t '{famous_person.title()}'"
print(citat,"\n")


#################################################################################
#Author: 		setu1d
#Date: 			26-08-2021
#Description: 	pouzitie "strippingu", odstranovanie medzier v stringoch
#################################################################################
print('\033[1m' + "2-7. Stripping Names:" + '\033[0m')
stripping = ' python '
print (f"\t\033[1m{stripping}\033[0m\n\t'{stripping.rstrip()}' \n\t'{stripping.lstrip()}' \n\t'{stripping.strip()}'\n")


print('\033[1m' + "2-8. Number Eight:" + '\033[0m')
print(5+3)
print(11-3)
print(2*4)
print(16/2, "\n")


print('\033[1m' + "2-9. Favorite Number:" + '\033[0m')
favorite_number = 21
number_message = f"Hello, my favorite number is: {favorite_number}!"
print(number_message, "\n")


#print('\033[1m' + "" + '\033[0m')













