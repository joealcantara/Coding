# Exercise 4.7
# Make a list of the multiple of 3, from 3 to 30. Use a for loop
# to print the numbers in your list.

threes = []
for i in range(1, 11):
    threes.append(i*3)

for i in threes:
    print(i)