extends Node


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
