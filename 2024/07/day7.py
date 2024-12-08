import argparse
import re
import time
from concurrent.futures import ProcessPoolExecutor

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

operators = ["+","*","||"]

# def recursive_calc(first_number,index,numbers,total,goal):
#     cur_number = 0
#     if first_number == None:
#         cur_number == numbers[0]
#         total = cur_number
#     cur_number = numbers[index]
#     index += 1 
#     if index >= len(numbers):
#         print("Final total: ",total)
#         return
#     else:
#         for operator in operators:
#             print("Total? ", total)
#             if operator == "+":
#                 next_number = numbers[index]
#                 print(cur_number,"+",next_number)
#                 new_total = total+next_number
#                 print("Running total: ", new_total)
#                 recursive_calc(True,index,numbers,new_total,goal)
#             elif operator == "*":
#                 next_number = numbers[index]
#                 new_total = total*next_number 
#                 recursive_calc(True,index,numbers,new_total,goal)

def recursive_calc(total,index,numbers,goal):
    if total == 0:
        total += numbers[0]
    if index+1 >= len(numbers):
        if goal == total:
            #valid_count += 1
            return True
        return False
    else:
        valid = False
        for operator in operators:
            next_number = numbers[index+1]
            if operator == "+":
                new_total = total + next_number
                test_result = recursive_calc(new_total,index+1,numbers,goal)
                if test_result:
                    valid = True
                
            elif operator == "*":
                new_total = total * next_number
                test_result = recursive_calc(new_total,index+1,numbers,goal)
                if test_result:
                    valid = True
        return valid

def recursive_calc_con(total,index,numbers,goal):
    if total == 0:
        total += numbers[0]
    if index+1 >= len(numbers):
        if goal == total:
            #valid_count += 1
            return True
        return False
    else:
        valid = False
        for operator in operators:
            next_number = numbers[index+1]
            if operator == "+":
                new_total = total + next_number
                test_result = recursive_calc_con(new_total,index+1,numbers,goal)
                if test_result:
                    valid = True
                
            elif operator == "*":
                new_total = total * next_number
                test_result = recursive_calc_con(new_total,index+1,numbers,goal)
                if test_result:
                    valid = True

            elif operator == "||":
                new_total = int(str(total) + str(next_number))
                test_result = recursive_calc_con(new_total,index+1,numbers,goal)
                if test_result:
                    valid = True 

        return valid


def part1(filename):
    with open(filename) as f:
        lines = [line.split(":") for line in f.read().split("\n")];
        lines = [[int(line[0]),[int(item) for item in line[1].strip().split(" ")]] for line in lines]
        final_total = 0
        for line in lines:
            is_valid = recursive_calc(0,0,line[1],line[0])
            if is_valid:
                final_total += line[0]
        print(final_total)

def process_line(line):
    target, numbers = line
    is_valid = recursive_calc_con(0, 0, numbers, target)
    return target if is_valid else 0

def part2(filename):
    with open(filename) as f:
        start_time = time.time()
        lines = [line.split(":") for line in f.read().split("\n")];
        lines = [[int(line[0]),[int(item) for item in line[1].strip().split(" ")]] for line in lines]
        final_total = 0
        with ProcessPoolExecutor() as executor:
            results = list(executor.map(process_line, lines))
            final_total = sum(results)
            print(final_total)

        print((time.time() - start_time))

if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="ex1.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)