extends PanelContainer
class_name Zones

@export var room_name = "Room Name"
@export var room_description = "This is the description of the room"

var exits: Dictionary = {
	
}


func connect_exit(direction: String, zone):
	match direction:
		"west":
			exits[direction] = room_description
			zone.exits["east"] = self
		"east":
			exits[direction] = room_description
			zone.exits["west"] = self
		"north":
			exits[direction] = room_description
			zone.exits["south"] = self
		"south":
			exits[direction] = room_description
			zone.exits["north"] = self
		_:
			printerr("Tried to connect invalid direction: %s", direction)
