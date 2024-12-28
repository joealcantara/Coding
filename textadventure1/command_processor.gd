extends Node


signal response_generated(response_text)


var current_room = null


func initialize(starting_room):
	change_room(starting_room)


func process_command(input: String) -> String:
	var words = input.split(" ", false)
	if words.size() == 0:
		return "Error: no words were parsed"
	var first_word = words[0].to_lower()
	var second_word = ""
	if words.size() > 1:
		second_word = words[1].to_lower()
		
	match first_word:
		"go":
			return go(second_word)
		"help":
			return help()
		_:
			return "Unrecognized Command. Please try again!"
			
			
			
func go(direction: String):
	if direction == "":
		return "go where?"
	
	return "You go to %s" % direction
	

func help() -> String:
	return "You can use these commands: go [location], help"	


func change_room(new_room):
	current_room = new_room
	var exit_string = PackedStringArray(current_room.exits.keys())
	var strings = "\n".join(PackedStringArray([
		"You are now in: " + current_room.room_name + ". It is " + current_room.room_description,
		"Exits: " + ", ".join(exit_string)
	]))
	emit_signal("response_generated", strings)
