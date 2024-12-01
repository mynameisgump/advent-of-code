import argparse
import operator
import re

parser = argparse.ArgumentParser()
parser.add_argument("s", choices=["p1","p2"])
parser.add_argument("i", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        print("Part 1")
        lines = [line.rstrip().split("  ") for line in f]
        
        left_list = [item[0] for item in lines]
        right_list = [item[1] for item in lines]
        left_list.sort()
        right_list.sort()
        print(left_list, right_list)
        total = 0
        for i in range(len(left_list)):
            abs_dist = abs(int(left_list[i])-int(right_list[i]))
            total += abs_dist
        print(total)
def part2(filename):
    with open(filename):
        print("Part 2")

if __name__ == "__main__":
    input_selection = args.i
    solution_selection = args.s;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="ex1.txt"
        case "ex2":
            filename="ex2.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)