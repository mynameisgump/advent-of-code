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
            #print(columns)
            row_hit = False
            r_duplicates = [item for item, count in collections.Counter(mirror).items() if count > 1]
            

            # r_indices = [i for i in range(len(mirror)) if mirror[i] in r_duplicates]
            # if len(r_duplicates) > 1:
            #     if r_indices[-1] == len(mirror)-1 or r_indices[0] == 0:
            #         print(r_duplicates,r_indices)
            #         total += r_indices[len(r_indices)//2]*100
            #         print("Row Split:", r_indices[len(r_indices)//2])

            c_duplicates = [item for item, count in collections.Counter(columns).items() if count > 1]
            print("Counts:",collections.Counter(columns))
            c_indices = [i for i in range(len(columns)) if columns[i] in c_duplicates]
            
            if len(c_duplicates) > 1:
                if c_indices[-1] == len(columns)-1 or c_indices[0] == 0:
                    print(c_duplicates,c_indices)
                    total += c_indices[len(c_indices)//2]
                    print("Column Split:", c_indices[len(c_indices)//2])

       

        print(h_indices,v_indices)
        print(total)
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