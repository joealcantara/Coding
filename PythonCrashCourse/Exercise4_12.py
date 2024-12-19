# Exercise 4.12
# All versions of foods.py in this section have avoided using for loops
# when printing, to save space. Choose a version of foods.py, and write
# two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

print("My favourite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favourite foods are:")
for food in friend_foods:
    print(food)