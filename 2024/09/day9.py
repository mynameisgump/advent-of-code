import argparse
import re
import time
import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        start_time = time.time()
        line = f.read().split("\n")[0];
        f_or_s = "f"
        cur_id = 0
        base_list = []
        for char in line:
            if f_or_s == "f":
                char_i = int(char)
                base_list = base_list + [str(cur_id)]*int(char)
                f_or_s = "s"
                cur_id += 1
            else:
                char_i = int(char)
                base_list = base_list + list(("."*int(char)))
                f_or_s = "f"
        
        empty_indexes = []
        for char_i in range(len(base_list)):
            char = base_list[char_i]
            if char == ".":
                empty_indexes.append(char_i)
        

        final_list = base_list
        for char_i in range(len(final_list)-1, -1, -1):
            print(char_i,"/",len(final_list))
            char = base_list[char_i]
            if char != ".":
                final_list[char_i] = "."
               
                r_index = empty_indexes.pop(0)
                final_list[r_index] = char
                if "." not in "".join(final_list)[0:char_i]:
                    break
        
        final_sum = 0
        cur_i = 0
        for item in final_list:
            if item == ".":
                break
            else:
                # print(item)
                final_sum += int(item) * cur_i
                cur_i += 1
        print(final_sum)

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