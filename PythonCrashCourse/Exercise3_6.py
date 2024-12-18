# Exercise 3.6
# You just found a bigger table, so now more space is available. Think of three more guests to invite.
# - Start with your program from Exercise 3.4 or 3.5. Add a print() call to the end of your program,
#   informing people that you found a bigger table.
# - Use insert() to add one new guest to the beginning of your list.
# - Use insert() to add one new guest to the middle of your list.
# - Use append() to add one new guest to the end of your list.
# - Print a new set of invitation messages, one for each person in your list.

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