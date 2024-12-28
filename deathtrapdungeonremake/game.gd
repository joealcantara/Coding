extends Node





func _ready() -> void:
	print('hello world')
	for i in range(5):
		print(roll_dice(6))
	var player = preload("res://scenes/character.tscn").instantiate()
	add_child(player)
	player.skill = roll_dice(6)
	player.stamina = roll_dice(6) + roll_dice(6)
	player.luck = roll_dice(6)
	player.displayStats()
	
	



func roll_dice(sides: int):
	return randi_range(1, sides)
	
	
	
