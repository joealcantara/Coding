extends Node

@export var skill = 1
@export var stamina = 1
@export var luck = 1


func displayStats():
	print("Player Stats")
	print("Skill: " + str(skill))
	print("Stamina: " + str(stamina))
	print("Luck: " + str(luck))
