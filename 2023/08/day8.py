import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        [instructions, nodes] = f.read().split("\n\n");
        pairs = [item.strip().split("=") for item in nodes.split("\n")]
        path_map = {}
        for i in range(len(pairs)):
            pairs[i][0] = pairs[i][0].strip()
            pairs[i][1] = re.sub("[()]",'',pairs[i][1]).strip().split(", ")
            path_map[pairs[i][0]] = pairs[i][1]
        
        print(path_map)

        found = False
        steps = 0 
        cur_index = 0
        key = "AAA"
        while not found:
            print(key)
            print(cur_index)
            print(steps)
            print(len(instructions))
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