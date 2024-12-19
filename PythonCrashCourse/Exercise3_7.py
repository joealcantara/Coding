# Exercise 3.7
# You just found out that your new dinner table won't arrive in time for the dinner,
# and now you have space for only two guests.
# - Start with your program from Exercise 3.6. Add a new line that prints a message
# saying that you can invite only two people for dinner.
# - Use pop() to remove guests from your list one at a time until only two names remain
# in your list. Each time you pop a name from your list, print a message to that person
# letting them know you're sorry you can't invite them to dinner.
# - Print a message to each of the two people still on your list, letting them know
# they're still invited.
# - Use del to remove the last two names from your list, so you have an empty list.
# Print your list to make sure you actually have an empty list at the end of your program.

people = ['Bill Gates', 'Seth Lazar', 'Chris Watkins']
print("I'd like to invite you to dinner " + people[0])
print("I'd like to invite you to dinner " + people[1])
print("I'd like to invite you to dinner " + people[2])
print(people[2] + ", sorry you can't make it")
people[2] = "Jewel Staite"
print("I'd like to invite you to dinner " + people[0])
print("I'd like to invite you to dinner " + people[1])
print("I'd like to invite you to dinner " + people[2])
print("I've found a bigger table!")
people.insert(0, "Valerie Guest")
people.insert(3, "Tom Bombadil")
people.append("Fern")
print("I'd like to invite you to dinner " + people[0])
print("I'd like to invite you to dinner " + people[1])
print("I'd like to invite you to dinner " + people[2])
print("I'd like to invite you to dinner " + people[3])
print("I'd like to invite you to dinner " + people[4])
print("I'd like to invite you to dinner " + people[5])
print('I can only invite two people for dinner.')
uninvited = people.pop()
print(f"Sorry {uninvited} can not invite you to dinner.")
uninvited = people.pop()
print(f"Sorry {uninvited} can not invite you to dinner.")
uninvited = people.pop()
print(f"Sorry {uninvited} can not invite you to dinner.")
uninvited = people.pop()
print(f"Sorry {uninvited} can not invite you to dinner.")
print("I'd like to invite you to dinner " + people[0])
print("I'd like to invite you to dinner " + people[1])
del(people[0])
del(people[0])
print(people)
