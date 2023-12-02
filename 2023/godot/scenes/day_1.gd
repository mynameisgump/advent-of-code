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
		print(calibration_values.reduce(func(i, accum): return accum + i))

# Called when the node enters the scene tree for the first time.
func _ready():
	print("Running Day 1:")
	if run_day_1:
		# Part 1:
		var file = FileAccess.open("res://data/01/input.txt", FileAccess.READ);
		var calibration_doc = file.get_as_text();
		var lines = calibration_doc.split("\n", false);
		var filtered_lines = []
		var calibration_values = []
		
		# Part 2:
		for line in lines:
			for key in conversion_table:
				line = line.replace(key,key[0]+key+key[-1])
			
			var positions = {}
			for key in conversion_table:
				var value = conversion_table[key];
				positions[key] = line.find(key);
			
			var position_pairs = []
			for key in positions:
				var value = positions[key];
				position_pairs.append([key,value])
			position_pairs.sort_custom(func(a, b): return a[1] < b[1]);
			position_pairs = position_pairs.filter(func(pair): return int(pair[1]) != -1);
#			print()
#			print("position pairs", position_pairs)
#			print("Line Before:", line)
			for pair in position_pairs:
				line = line.replace(pair[0], conversion_table[pair[0]]+pair[0]);
				#string = string.replace(letter_pair[0], conversion_table[letter_pair[0]]+letter_pair[0])
#			print("Line After: ", line)
			# filtered_lines.append(line);
			# Filter out characters
			var valid_digits = []
			for char in line:
				if char.is_valid_int():
					valid_digits.append(char);
			var filtered_string = "".join(valid_digits);
			filtered_lines.append(filtered_string)
			calibration_values.append(int(filtered_string[0]+(filtered_string[-1])))
		# Sum the Values
		print(filtered_lines)
		print(calibration_values.reduce(func(i, accum): return accum + i))


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
