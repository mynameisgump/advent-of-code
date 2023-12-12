import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

# Recursion?
# Check both sides of strings 
# S = S[:Index] + S[Index + 1:]
def recursive_string_check(field,groups):
    print(field)
    for i in range(len(field)):
        char = field[i]
        if char == ".":
            new_string = field[:i] + field[i + 1:]
            # Remove check 
            #print(new_string)

        if char == "?":
            hash_string = field[:i] + "#" + field[i + 1:]
            dot_string = field[:i] + "." + field[i + 1:]
            recursive_string_check(dot_string, groups)
            recursive_string_check(hash_string, groups)
            #recursive_string_check(field)
        if char == "#":
            print("Boutta Count:")
            new_i = i+1
            count = 1
            counting = True 
            while counting:
                if new_i < len(field):
                    new_char = field[new_i]
                    if new_char == "#":
                        count += 1
                        new_i += 1
                    else:
                        counting = False
                else:
                    counting = False
           
            print("Counted:",field,count)
            

def part1(filename):
    with open(filename) as f:
        records = [[item.split(" ")[0],[int(num) for num in item.split(" ")[1].split(",")]]for item in f.read().split("\n")];
        for record in records:
            recursive_string_check(record[0],record[1])
def part2(filename):
    with open(filename) as f:
        lines = f.read().split("\n");

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