import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def print_map(map):
    for row in map:
        print("".join(row))

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n");
        guard_map = [list(line) for line in lines]
        map_copy = [list(line) for line in lines]
        start = []
        for x in range(len(guard_map)):
            for y in range(len(guard_map[x])):
                if guard_map[x][y] == "^":
                    #print("Found: ", x,y)
                    start = [x,y]
        walking = True 
        direction = "^"
        cur_loc = start
        while walking:
            if direction == "^":
                next_step = [cur_loc[0]-1,cur_loc[1]]
            elif direction == ">":
                next_step = [cur_loc[0],cur_loc[1]+1]
            elif direction == "<":
                next_step = [cur_loc[0],cur_loc[1]-1]
            elif direction == "v":
                next_step = [cur_loc[0]+1,cur_loc[1]]
            map_copy[cur_loc[0]][cur_loc[1]] = "X"
            #print()
            #print_map(map_copy)
            if next_step[0] >= len(map_copy) or next_step[0] < 0 or next_step[1] >= len(map_copy[0]) or next_step[1] < 0:
                break
            
            next_value = guard_map[next_step[0]][next_step[1]];
            if next_value == "#":
                if direction == "^":
                    direction = ">"
                elif direction == ">":
                    direction = "v"
                elif direction == "v":
                    direction = "<"
                elif direction == "<":
                    direction = "^" 
            else:
                cur_loc = next_step
        total = "".join(["".join(row) for row in map_copy]).count("X")
        print_map(map_copy)
        print(total)


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