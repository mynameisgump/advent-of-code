import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def hash_string(string):
    total = 0
    for char in string:
        total += ord(char)
        total *= 17
        total %= 256
    return total

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n")[0].split(",");
        total = 0 
        for string in lines:
            total += hash_string(string)
        print(total)

def part2(filename):
    with open(filename) as f:
        lines = f.read().split("\n")[0].split(",");
        total = 0 
        hashmap = {k: {} for k in range(256)}
        for string in lines:
            if "=" in string:
                [label, focal_length] = string.split("=")
                print(label,focal_length)
                box_num = hash_string(label)
                hashmap[box_num][label] = focal_length
                pass
            elif "-" in string:
                pass
            total += hash_string(string)
        print(total)

if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="example1.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)