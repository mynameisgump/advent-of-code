extends Node

var run_day_1 = true;


const conversion_table = {
		"one": "1",
		"two": "2",
		"three": "3",
		"four": "4",
		"five":"5",
		"six": "6",
		"seven": "7",
		"eight": "8",
		"nine": "9",
}

const files = {
	"ex1": "res://data/01/example1.txt",
	"ex2": "res://data/01/example2.txt",
	"input": "res://data/01/input.txt",
}

func sort_descending_e2(a, b):
		if a[1] > b[1]:
			return true
		return false
		
func part1():
	var file = FileAccess.open("res://data/01/example1.txt", FileAccess.READ);
	var calibration_doc = file.get_as_text();
	print()
# Called when the node enters the scene tree for the first time.
func _ready():
	print("Running Day 1:")
	
		

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
