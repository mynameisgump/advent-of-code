import argparse
import re
from threading import Thread

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

# Have each thread updating a var with the parts it hit's Z,
# Collapse when all intersect with a given step number
# Steps: 
# 1. Get all that end with A
# 2. Create threads which wait for others to end when they hit a Z
# 3. From there continue by passing back to the function the current Z steps 
#    and the current key you were searching from

def threaded_path(starting_key,instructions,path_map,total_z):
    key = starting_key

    found = False
    steps = 0 
    cur_index = 0
    key = starting_key
    z_steps = []
    while not found and len(z_steps) < total_z:
        if found:
            found = False
        if cur_index > len(instructions)-1:
            cur_index = 0
        char = instructions[cur_index]
        if char == "L":
            key = path_map[key][0]
        elif char == "R":
            key = path_map[key][1]
        steps += 1
        cur_index += 1
        if key.endswith():
            found = True
    return z_steps


def part1(filename):
    with open(filename) as f:
        [instructions, nodes] = f.read().split("\n\n");
        pairs = [item.strip().split("=") for item in nodes.split("\n")]
        path_map = {}
        for i in range(len(pairs)):
            pairs[i][0] = pairs[i][0].strip()
            pairs[i][1] = re.sub("[()]",'',pairs[i][1]).strip().split(", ")
            path_map[pairs[i][0]] = pairs[i][1]
        
        found = False
        steps = 0 
        cur_index = 0
        key = "AAA"
        while not found:
            if cur_index > len(instructions)-1:
                cur_index = 0
            char = instructions[cur_index]
            if char == "L":
                key = path_map[key][0]
            elif char == "R":
                key = path_map[key][1]
            steps += 1
            cur_index += 1
            if key == "ZZZ":
                found = True
        print(steps)

def part2(filename):
    with open(filename) as f:
        [instructions, nodes] = f.read().split("\n\n");
        pairs = [item.strip().split("=") for item in nodes.split("\n")]
        path_map = {}
        sum_A = 0
        for i in range(len(pairs)):
            pairs[i][0] = pairs[i][0].strip()
            if pairs[i][0].endswith("A"):
                print(pairs[i][0])
                sum_A += 1
            pairs[i][1] = re.sub("[()]",'',pairs[i][1]).strip().split(", ")
            #print(pairs[i])

            path_map[pairs[i][0]] = pairs[i][1]
        print(sum_A)
        #print(path_map)
        for i in tange

if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="example1.txt"
        case "ex2":
            filename="example2.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)