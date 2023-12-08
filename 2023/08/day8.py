import argparse
import re
import threading
import logging

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
# After each run, get the max values of each. Should be at the end of the list.
# Remove everthing below the min of those values.

# Data structures are prob getting to big. Need to reduce in some capacity. 

def threaded_path(starting_key,instructions,path_map,z_steps,cur_index,thread_results,thread_num):
    key = starting_key
    found = False
    steps = 0
    if len(z_steps) > 0:
        steps = z_steps[-1]
    next_index = ""
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
        if key.endswith("Z"):
            z_steps.append(steps)
            found = True
    thread_results[thread_num] = [z_steps,cur_index,key]
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
        a_keys = []
        for i in range(len(pairs)):
            pairs[i][0] = pairs[i][0].strip()
            if pairs[i][0].endswith("A"):
                print(pairs[i][0])
                a_keys.append(pairs[i][0])
            pairs[i][1] = re.sub("[()]",'',pairs[i][1]).strip().split(", ")
            path_map[pairs[i][0]] = pairs[i][1]
        print(a_keys)
        ghosts = []
        for key in a_keys:
            ghost = {}
            ghost["key"] = key
            ghost["index"] = 0
            ghost["z_stop_points"] = []
            ghosts.append(ghost)
        
        thread_results = {}
        for i in range(4):
            threads = []
            for index in range(len(ghosts)):
                ghost = ghosts[index]
                print("Ghost: ", ghost)
                x = threading.Thread(target=threaded_path, 
                                        args=(ghost["key"],
                                        instructions,
                                        path_map,
                                        ghost["z_stop_points"],
                                        ghost["index"],
                                        thread_results,
                                        index))
                threads.append(x)
                x.start()
                
            for index, thread in enumerate(threads):
                logging.info("Main    : before joining thread %d.", index)
                thread.join()
                logging.info("Main    : thread %d done", index)
            for index in range(len(ghosts)):
                ghosts[index]["key"] = thread_results[index][2]
                ghosts[index]["z_stop_points"] = thread_results[index][0]
                ghosts[index]["index"] = thread_results[index][1]
            print(thread_results)
        #print(set.intersection(*map(set,list(thread_results.values()))))

        #print(path_map)


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