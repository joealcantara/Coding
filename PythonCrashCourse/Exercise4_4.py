# Exercise 4.4
# Make a list of the numbers from one to one million, and then use a for
# loop to print the numbers (If the output is taking too long, stop it by
# pressing CTRL-C or by closing the output window.)

numbers = []
for i in range(1000001):
    numbers.append(i)

print(numbers)