import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

operators = ["+","*"]

def recursive_calc_2(first_number,index,numbers,total,goal):
    cur_number = 0
    if first_number == None:
        cur_number == numbers[0]
        total = cur_number
    cur_number = numbers[index]
    index += 1 
    if index >= len(numbers):
        print("Final total: ",total)
        return
    else:
        for operator in operators:
            if operator == "+":
                next_number = numbers[index]
                print(cur_number,"+",next_number)
                new_total = total+next_number
                print("Running total: ", total)
                recursive_calc(index,numbers,total,goal)
            elif operator == "*":
                next_number = numbers[index]
                print(total,"*",next_number)
                new_total = total*next_number 
                print("Running total: ", total)
                recursive_calc(index,numbers,total,goal)

def recursive_calc(index,numbers,total,goal):
    cur_number = numbers[index]
    index += 1 
    if index >= len(numbers):
        print("Final total: ",total)
        return
    else:
        for operator in operators:
            if operator == "+":
                next_number = numbers[index]
                print(cur_number,"+",next_number)
                new_total = cur_number+next_number
                print("Running total: ", new_total)
                recursive_calc(index,numbers,new_total,goal)
            elif operator == "*":
                next_number = numbers[index]
                print(cur_number,"*",next_number)
                new_total = cur_number*next_number 
                print("Running total: ", new_total)
                recursive_calc(index,numbers,new_total,goal)
            #recursive_calc(in)
    #next_number = numbers[index+1]

def part1(filename):
    with open(filename) as f:
        lines = [line.split(":") for line in f.read().split("\n")];
        lines = [[int(line[0]),[int(item) for item in line[1].strip().split(" ")]] for line in lines]
        for line in lines:
            print()
            print("New Line:")
            recursive_calc_2(None,0,line[1],0,line[0])
            
        print(lines)

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
            filename="ex1.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)