extends Node

var run_day_1 = true;

const files = {
	"ex1": "res://data/01/example1.txt",
	"ex2": "res://data/01/example2.txt",
	"input": "res://data/01/input.txt",
}

# Called when the node enters the scene tree for the first time.
func _ready():
	if run_day_1:
		# Part 1:
		var file = FileAccess.open("res://data/01/example2.txt", FileAccess.READ);
		var calibration_doc = file.get_as_text();
		var lines = calibration_doc.split("\n");
		var filtered_lines = []
		var calibration_values = []
		for line in lines:
			var valid_digits = []
			for char in line:
				if char.is_valid_int():
					valid_digits.append(char);
			var filtered_string = "".join(valid_digits);

			calibration_values.append(int(filtered_string[0]+(filtered_string[-1])))
		# Sum the Values
		print(calibration_values.reduce(func(i, accum): return accum + i))



# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
