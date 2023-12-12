import argparse
import re
from functools import lru_cache
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

# Recursion?
# Check both sides of strings 
# S = S[:Index] + S[Index + 1:]
# 
def recursive_string_check_2(field,groups):
    if "?" in field:
        #print()
        #print(field)
        for i in range(len(field)):
            char = field[i]
            if char == "?":
                hash_string = field[:i]+ "#" + field[i+1:]
                dot_string = field[:i]+ "." + field[i+1:]
                if hash_string.count("#") <= sum(groups):
                    recursive_string_check_2(hash_string, groups)

                recursive_string_check_2(dot_string, groups)
                #print(hash_string)
                #print(dot_string)
    else:
        print(field)

@lru_cache(maxsize=None)
def recursive_string_check(field,groups):
    print(field,groups)
    if len(field) == 0 or len(groups) == 0:
        if len(field) == 0 and len(groups) == 0:
            print("Empties")
        

    elif len(field) > 0:
        char = field[0]
        if char == ".":
            new_string = field[1:]
            recursive_string_check(new_string,groups)
        elif char == "?":
            
            hash_string = "#" + field[1:]
            dot_string = "." + field[1:]
            recursive_string_check(dot_string, groups)
            recursive_string_check(hash_string, groups)

        elif char == "#":
            #print()
            #print("Hashtag Check: ", field, groups)
            count = 1
            group = groups[0]
            # ensure can index 
            if len(field) >= group:

                new_i = 1
                counting = True 
                valid = False

                while counting:
                    print(counting)
                    if new_i < len(field):
                        new_char = field[new_i]
                        if count == group: 
                            if new_char == "?" or new_char == ".":
                                counting = False
                                valid = True
                            else:
                                counting = False
                        elif count > group:
                            counting = False

                        if new_char == "#":
                            count += 1
                            new_i += 1
                        elif new_char == "?":
                            count += 1
                            new_i += 1
                    else:
                        if count == group: 
                            valid = True
                        counting = False
                #print(valid)
                if valid:
                     recursive_string_check(field[count:],groups[1:])
            #print()
            # print()
            # print(field)
            # print(count)
            # print(new_i)
            # print(field[count:])
            #print("Counted:",field,count)
        
            

def part1(filename):
    with open(filename) as f:
        records = [[item.split(" ")[0],tuple([int(num) for num in item.split(" ")[1].split(",")])]for item in f.read().split("\n")];
        count = 0 
        for record in records:
            print()
            print("New Record: ")
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