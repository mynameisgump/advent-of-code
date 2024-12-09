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
            char = base_list[char_i]
            if char != ".":
                final_list[char_i] = "."
               
                r_index = empty_indexes.pop(0)
                final_list[r_index] = char
                if final_list[0:char_i].count(".") == 0:
                    break

        final_sum = 0
        cur_i = 0
        for item in final_list:
            if item == ".":
                break
            else:
                final_sum += cur_i * int(item) 
                cur_i += 1
        print(final_sum)

def print_tuple_list(tuple_list):
    final_string = ""
    for item in tuple_list:
        final_string = final_string + str(item[0])*item[1]
    print(final_string)

def calc_tuple_list_sum(tuple_list):
    final_list = []
    for item in tuple_list:
        final_list = final_list + [item[0]]*item[1]
    print(final_list)
    final_sum = 0
    cur_i = 0
    for item in final_list:
        if item != ".":
            final_sum += cur_i * int(item) 
        cur_i += 1
    print(final_sum)


# Switching to ranges
def part2(filename):
    with open(filename) as f:
        start_time = time.time()
        line = f.read().split("\n")[0];
        
        f_or_s = "f"
        cur_id = 0
        base_list = []
        for char in line:
            if f_or_s == "f":
                char_i = int(char)
                base_list.append((str(cur_id),int(char)))
                f_or_s = "s"
                cur_id += 1
            else:
                char_i = int(char)
                base_list.append((".",int(char)))
                f_or_s = "f"
        #print(base_list)
        empty_indexes = []
        for char_i in range(len(base_list)):
            char = base_list[char_i]
            if char[0] == ".":
                empty_indexes.append(char_i)
        
        final_list = base_list
        print_tuple_list(final_list)
        for char_i in range(len(final_list)-1, -1, -1):
            char = final_list[char_i]
            empty_indexes = [x for x in empty_indexes if x <= char_i]
            if char[0] != ".":
                for i in range(len(empty_indexes)):
                    e_index = final_list[empty_indexes[i]]
                    # print("Both: ",e_index,char)
                    # print(empty_indexes)
                    if e_index[1] >= char[1]:
                        if e_index[1]-char[1] == 0:
                            # print()
                            # print("Replace", empty_indexes)
                            final_list[empty_indexes[i]] = char
                            final_list[char_i] = (".",char[1])
                            # print_tuple_list(final_list)
                            empty_indexes.pop(i)
                        else:
                            #print()
                            # print("Insert", empty_indexes)
                            new_e_index = (e_index[0],e_index[1]-char[1])
                            empty_indexes = [x + 1 if ind >= i else x for ind, x in enumerate(empty_indexes)]
                            final_list.insert(empty_indexes[i]-1,char)
                            final_list[empty_indexes[i]] = new_e_index
                            final_list[char_i+1] = (".",char[1])
                            # print(empty_indexes)
                            # print_tuple_list(final_list)


                        break
        calc_tuple_list_sum(final_list)
        # print()
        # print("Goal:")
        # print("00...111...2...333.44.5555.6666.777.888899")
        # print("0099.111...2...333.44.5555.6666.777.8888..")
        # print("0099.1117772...333.44.5555.6666.....8888..")
        # print("0099.111777244.333....5555.6666.....8888..")
        # print("00992111777.44.333....5555.6666.....8888..")


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