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
		var file = FileAccess.open("res://data/01/example1.txt", FileAccess.READ);
		var calibration_doc = file.get_as_text();
		var lines = calibration_doc.split("\n");
		print(lines)
		var filtered_lines = []
		for line in lines:
			var valid_digits = []
			for char in line:
				if char.is_valid_int():
					valid_digits.append(char);
			filtered_lines.append("".join(valid_digits))
		print(filtered_lines[3][-1])
		

		
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
