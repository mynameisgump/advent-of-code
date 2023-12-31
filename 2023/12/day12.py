import argparse
import re
from functools import lru_cache
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2","p1t"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

# Recursion?
# Check both sides of strings 
# S = S[:Index] + S[Index + 1:]
# 
# def recursive_string_check_2(field,groups):
#     if "?" in field:
#         #print()
#         #print(field)
#         for i in range(len(field)):
#             char = field[i]
#             if char == "?":
#                 hash_string = field[:i]+ "#" + field[i+1:]
#                 dot_string = field[:i]+ "." + field[i+1:]
#                 if hash_string.count("#") <= sum(groups):
#                     recursive_string_check_2(hash_string, groups)

#                 recursive_string_check_2(dot_string, groups)
#                 #print(hash_string)
#                 #print(dot_string)
#     else:
#         print(field)

# Attempt 1 too high: 9612

@lru_cache(maxsize=None)
def recursive_string_check(field,groups,prev,total):
    #print("|"*prev,field,groups,prev)
    new_total = 0
    if len(field) == 0 or len(groups) == 0:
        field = field.replace(".","")
        field = field.replace("?","")
        if field.count("#") == 0 and len(groups) == 0:
            #print(field,groups)
            new_total += 1
    elif len(field) > 0:
        #print("Checking Char of field")
        char = field[0]
        if char == ".":
            new_string = field[1:]
            new_total += recursive_string_check(new_string,groups,prev+1,total)
        elif char == "?":
            
            hash_string = "#" + field[1:]
            dot_string = "." + field[1:]
            new_total += recursive_string_check(hash_string, groups,prev+1,total)
            new_total += recursive_string_check(dot_string, groups,prev+1,total)
            
        elif char == "#":
            count = 1
            group = groups[0]
            if len(field) >= group:

                new_i = 1
                counting = True 
                valid = False

                while new_i < len(field):
                    new_char = field[new_i]
                    if count > group:
                        break
                    if count == group: 
                        if new_char == "?" or new_char == ".":
                            valid = True
                            break

                    if new_char == "#":
                        count += 1
                    elif new_char == "?":
                        count += 1
                    elif new_char == ".":
                        break
                    new_i += 1
                if count == group: 
                    valid = True
                #print(valid)
                if valid:
                    new_total += recursive_string_check(field[count+1:],groups[1:],prev+1,total)
            #print()
            # print()
            # print(field)
            # print(count)
            # print(new_i)
            # print(field[count:])
            #print("Counted:",field,count)
    return new_total
def part1_testing():
    with open("test.txt") as f:
        records = [[item.split(" ")[0],tuple([int(num) for num in item.split(" ")[1].split(",")]),int(item.split(" ")[2])]for item in f.read().split("\n")];
        count = 0 
        for record in records:
            print()
            print("New Record: ")

            total = recursive_string_check(record[0],record[1],0,0)
            assert total == record[2]
            count += total
        print("Final Sum: ", count)            

def part1(filename):
    with open(filename) as f:
        records = [[item.split(" ")[0],tuple([int(num) for num in item.split(" ")[1].split(",")])]for item in f.read().split("\n")];
        count = 0 
        for record in records:
            total = recursive_string_check(record[0],record[1],0,0)
            count += total
        print(count)

def part2(filename):
    with open(filename) as f:
        records = [[item.split(" ")[0],tuple([int(num) for num in item.split(" ")[1].split(",")])]for item in f.read().split("\n")];
        count = 0 
        for record in records:
            new_field = (record[0]+"?")*4+record[0]
            new_items = record[1]*5
            print(new_field)
            print(new_items)
            total = recursive_string_check(new_field,new_items,0,0)
            count += total
        print(count)


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
        case "p1t":
            part1_testing()