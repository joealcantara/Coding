# This is my first attempt at recreating and updating Deathtrap Dungeon.
# Imports
import random

class monster:
    def __init__(self, name, skill, stamina, luck):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.luck = luck

class player:
    def __init__(self, name):
        self.name = name
        self.maxStrength = random.randint(1, 6)
        self.maxStamina = random.randint(2, 12)
        self.maxLuck = random.randint(1, 6)
        self.strength = self.maxStrength
        self.stamina = self.maxStamina
        self.luck = self.maxLuck

def combat(player, monster):
    pass

def printCharacter(player):
    print(player.name)
    print(f"Strength: {player.strength}/{player.maxStrength}")
    print(f"Stamina: {player.stamina}/{player.maxStamina}")
    print(f"Luck: {player.luck}/{player.maxLuck}")

def main():
    print('Welcome to Text RPG')
    print('')
    player1 = player(input('What is your name? '))
    printCharacter(player1)

main()