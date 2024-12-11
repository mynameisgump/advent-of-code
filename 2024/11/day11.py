import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n")[0].split(" ");
        blinks = 25
        current_index = 0
        for i in range(blinks):
            while current_index < len(lines):
                stone = lines[current_index]
                if int(stone) == 0:
                    lines[current_index] = str(1)
                elif len(stone) % 2 == 0:
                    new_stones = [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
                    lines = lines[:current_index]+new_stones+lines[current_index+1:]
                    current_index += 1
                else:
                    lines[current_index] = str(int(lines[current_index])*2024)
                    
                current_index += 1
            current_index = 0
            print(" ".join(lines))
        print(len(lines))

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