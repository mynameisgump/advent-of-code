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
    print(field,groups)
    if len(field) > 1:
        char = field[0]
        if char == ".":
            new_string = field[1:]
            recursive_string_check(new_string,groups)
        elif char == "?":
            
            hash_string = "#" + field[1:]
            dot_string = "." + field[1:]
            #print()
            #print(field)
            #print(hash_string,dot_string)
            recursive_string_check(dot_string, groups)
            recursive_string_check(hash_string, groups)
        elif char == "#":
            new_i = 1
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
            if count == groups[0]:
                recursive_string_check(field[count:],groups[1:])
            # print()
            # print(field)
            # print(count)
            # print(new_i)
            # print(field[count:])
            #print("Counted:",field,count)
    else:
        print(groups)
        
            

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