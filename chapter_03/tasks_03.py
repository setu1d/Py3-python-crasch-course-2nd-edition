#3-1. Names: Store the names of a few of your friends in a list called names. 
#Print each person’s name by accessing each element in the list, one at a time.
print('\033[1m' + "3-1. Names" + '\033[0m')
names = ['laky', 'Puco', 'Zuza', 'Jay']
persons = f"person's name: {names[0].title()}, {names[1].title()}, {names[2].title()}, {names[-1].title()}."
print(persons, "\n")

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
#printing each person’s name, print a message to them. The text of each message
#should be the same, but each message should be personalized with the
#person’s name.
print('\033[1m' + "3-2. Greetings" + '\033[0m')
names = ['laky', 'Puco', 'Zuza', 'Jay']
print(f"Nazdar, {names[0].title()}!")
print(f"Nazdar, {names[1].title()}!")
print(f"Nazdar, {names[-2].title()}!")
print(f"Nazdar, {names[-1].title()}!\n")

#3-3. Your Own List: Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a
#Honda motorcycle.”
print('\033[1m' + "3-3. Your Own List" + '\033[0m')
cars = ["volvo", "seat", "porche"]
bike = ["santa cruz", "lapierre", "specialized"]
print(f"Rad by som vlastnil auto znacky: {cars[0].title()}.")
print(f"Rad by som vlastnil auto znacky: {cars[2].title()}.")
#poziadam polozku s indexom -3. Python vzy vrati polozku od konca
print(f"Rad by som vlastnil bike znacky: {bike[-3].title()}!\n")





















