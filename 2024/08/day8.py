import argparse
import re
import itertools
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        file_in = f.read().split("\n")
        lines = [list(line) for line in file_in];

        antinode_positions = set()
        frequencies = {}
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                char = lines[x][y]
                if char != ".":
                    if char not in frequencies:
                        frequencies[char] = [(x,y)]
                    else:
                        frequencies[char].append((x,y))
        
        for key in frequencies:
            positions = frequencies[key]
            pairs = list(itertools.combinations(positions,2))
            for pair in pairs:
                x_dist = pair[0][0]-pair[1][0]
                y_dist = pair[0][1]-pair[1][1]
                
                antinode_positions.add((pair[0][0]+x_dist,pair[0][1]+y_dist))
                antinode_positions.add((pair[1][0]-x_dist,pair[1][1]-y_dist))

        antinode_positions = [(x, y) for x, y in antinode_positions if 0 <= x < len(lines) and 0 <= y < len(lines[0])]

        print(len(antinode_positions))

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
        case "ex2":
            filename="ex2.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)