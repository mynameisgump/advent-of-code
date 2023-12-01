import argparse
import operator
import re

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

conversion_table = {
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

def remove_letters(string):
    return re.sub("[^0-9]", "", string);

def calc_calibration(string):
    return string[0]+string[-1]

def negative_index_filter(tuple):
    if tuple[1] == -1:
        return False;
    else:
        return True;

def words_to_num(string):
    positions = {}
    for key, value in conversion_table.items():
        positions[key] = string.find(key);
        
    sorted_positions = sorted(positions.items(), key=operator.itemgetter(1))
    filtered = list(filter(negative_index_filter, sorted_positions))
    for letter_pair in filtered:
        string = string.replace(letter_pair[0], conversion_table[letter_pair[0]]+letter_pair[0])

    return string

def part1(filename):
    with open(filename) as f:
        input_string = f.read().replace("\n", " ").split(" ");
        digits_list = [remove_letters(item) for item in input_string if item != ""]
        calibration_values = [int(calc_calibration(item)) for item in digits_list]
        print("The solution to part 1 is: ",sum(calibration_values))

def part2(filename):
    with open(filename) as f:
        input_strings = f.read().replace("\n", " ").split(" ");
        converted_strings = [words_to_num(item) for item in input_strings]
        digits_list = [remove_letters(item) for item in converted_strings if item != ""]
        calibration_values = [int(calc_calibration(item)) for item in digits_list]
        print(f'Part 2 on {filename}:\n{sum(calibration_values)}')

if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="example1.txt"
        case "ex2":
            filename="example2.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)