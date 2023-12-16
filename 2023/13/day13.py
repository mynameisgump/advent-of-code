import argparse
import re
import collections
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();
# First then second: sorted_list = sorted(list, key=lambda x: (x[0], -x[1]))
# Attempt 1: 51329 :(
# Attemp 2: 38687 :(((
# Attempt 3: 35360 :)))
# #.##.#.##.#.#
# #.#.##.#.##.#
def part1(filename):
    with open(filename) as f:
        lines = [line.split("\n") for line in f.read().split("\n\n")];
        h_indices = []
        v_indices = []
        total = 0 
        for mirror in lines:
            print()
            for row in mirror:
                print(row)
            columns = []
            for i in range(len(mirror[0])):
                cur_column = ""
                for row in mirror:
                    cur_column += row[i]
                columns.append(cur_column)
            rows = mirror.copy()

 
            col_index = 0
            mirrored_cols = []
            while len(columns) > 0:
                front_ele = columns.pop(0)
                mirrored_cols.insert(0,front_ele)
                if len(columns) > 0:                    
                    if all(x == y for x, y in zip(columns, mirrored_cols)):
                        col_index = len(mirrored_cols)
                        total += col_index
                        break 

            print("Col Index: ", col_index)
            row_index = 0
            mirrored_rows = []
            while len(rows) > 0:
                front_ele = rows.pop(0)
                mirrored_rows.insert(0,front_ele)
                if len(rows) > 0:
                    if all(x == y for x, y in zip(rows, mirrored_rows)):
                        row_index = len(mirrored_rows)
                        total += row_index*100
                        break
            print("Row Index: ",row_index)
       
            print("Total: ", total)
        #print(h_indices,v_indices)
        #print(total)
        #print(lines)
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