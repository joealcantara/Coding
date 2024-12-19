# Exercise 3.5
# You just heard that one of your guests can't make the dinner, so you need to send out
# a new set of invitations. You'll have to think of someone else to invite.
# - Start with your program from Exercise 3.4. Add a print() call at the end of your program,
#   stating the name of the guest who can't make it.
# - Modify your list, replacing the name of the guest who can't make it with the name of the
#   new person you are inviting.
# - Print a second set of invitation messages, one for each person who is still on your list.

people = ['Bill Gates', 'Seth Lazar', 'Chris Watkins']
print("I'd like to invite you to dinner " + people[0])
print("I'd like to invite you to dinner " + people[1])
print("I'd like to invite you to dinner " + people[2])
print(len(people))
print(people[2] + ", sorry you can't make it")
people[2] = "Jewel Staite"
print("I'd like to invite you to dinner " + people[0])
print("I'd like to invite you to dinner " + people[1])
print("I'd like to invite you to dinner " + people[2])