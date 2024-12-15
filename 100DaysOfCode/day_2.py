print("Welcome to the tip calculator!")
total = float(input("What was the total bill? £\n"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
percent = tip / 100
persons = int(input("How many people to split the bill?\n"))
print("Each person should pay: £" + str((total + total * percent)/persons))