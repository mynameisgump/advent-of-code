import argparse
import re
import time
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
        final_string = ""
        for char in line:
            if f_or_s == "f":
                char_i = int(char)
                final_string = final_string + (str(cur_id)*int(char))
                f_or_s = "s"
                cur_id += 1
            else:
                char_i = int(char)
                final_string = final_string + ("."*int(char))
                f_or_s = "f"
        
        empty_indexes = []
        for char_i in range(len(final_string)):
            char = final_string[char_i]
            if char == ".":
                empty_indexes.append(char_i)
        
        final_list = list(final_string)
        print(len(final_list))
        for char_i in range(len(final_list)-1, -1, -1):
            print(char_i,"/",len(final_list))
            char = final_string[char_i]
            if char != ".":
                final_list[char_i] = "."
               
                r_index = empty_indexes.pop(0)
                final_list[r_index] = char
                if "." not in "".join(final_list)[0:char_i]:

                    break
                #print("".join(final_list)[0:char_i])

        print("".join(final_list))
        print("Crying")
        print((time.time() - start_time))
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