# Exercise 4.11
# Start with your program from Exercise 4.1. Make a copy of the list of pizzas,
# and call it friend_pizzas. Then, do the following:
# - Add a new pizza to the original list
# - Add a different pizza to the list friend_pizzas.
# - Prove that you have two separate lists. Print the message 'My favourite pizzas are:',
#   and then use a for loop to print the first list. Print the messsage 'My friend's
#   favourite pizzas are:', and then use a for loop to print the second list. Make sure
#   each new pizza is stored in the appropriate list.

pizzas = ['Meat Feast', 'Margherita', 'Ham and Mushroom']
for pizza in pizzas:
    print(f"I like {pizza} pizzas. ")

print("I really love pizzas")

friend_pizzas = pizzas[:]
pizzas.append('Texas BBQ')
friend_pizzas.append('Tuna Melt')

print('My favourite pizzas are: ')
for pizza in pizzas:
    print(pizza)

print('My friends favourite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)