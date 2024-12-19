# Exercise 4.2
# Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to print
# out the name of each animal.
# - Modify your program to print a statement about each animal, such as 'A dog
#   would make a great pet'
# - Add a line at the end of your program, stating what these animals have in common.
#   You could print a sentence, such as 'Any of these animals would make a great
#   pet!'

animals = ['Lion', 'Tiger', 'Leopard']
for animal in animals:
    print(animal)

for animal in animals:
    print(f"A {animal} is not a great pet")

print('Any of these animals would be not a good pet')