import argparse
import operator
import re
from itertools import pairwise
import fnmatch
import re
import fnmatch

parser = argparse.ArgumentParser()
parser.add_argument("s", choices=["p1","p2"])
parser.add_argument("i", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        input_string = [line for line in f][0];
        expressions = re.findall(r"mul\(\d{1,3},\d{1,3}\)",input_string)
        total = 0
        for expression in expressions:
            print(expression)
            expression = expression.lstrip("mul(").rstrip(")")
            numbers = [int(num) for num in expression.split(",")]
            total += numbers[0]*numbers[1]
        print(total)

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