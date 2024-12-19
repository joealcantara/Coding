# Exercise 4.10
# Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# - Print the message 'The first three items in the list are:' Then
# use a slice to print the first three items from that programs list.
# - Print the message 'Three items from the middle of the list are:' Then
# use a slice to print three items from the middle of the list.
# - Print the message 'The last three items in the list are:' Then
# use a slice to print the last three items from that programs list.

cubes = [value**3 for value in range(1, 11)]
print(cubes)
print('The first three items in the list are: ' + str(cubes[0:3]))
print('Three items from the middle of the list are: ' + str(cubes[4:7]))
print('The last three items in the list are: ' + str(cubes[:6:-1]))