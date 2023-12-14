import argparse
import re
import collections
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();
# First then second: sorted_list = sorted(list, key=lambda x: (x[0], -x[1]))
def part1(filename):
    with open(filename) as f:
        lines = [line.split("\n") for line in f.read().split("\n\n")];
        for mirror in lines:
            print(mirror)

            columns = []
            for i in range(len(mirror[0])):
                cur_column = ""
                for row in mirror:
                    cur_column += row[i]
                columns.append(cur_column)
            print(columns)
            row_hit = False
            r_duplicates = [item for item, count in collections.Counter(mirror).items() if count > 1]
            r_indices = [i for i in range(len(mirror)) if mirror[i] in r_duplicates]
            if r_indices[-1] == len(mirror[0]) or r_indices[0] == 0:
                hit = True

            c_duplicates = [item for item, count in collections.Counter(columns).items() if count > 1]
            c_indices = [i for i in range(len(mirror)) if columns[i] in c_duplicates]
            
            print(c_duplicates)
            print(c_indices)
            if c_indices[-1] == len(columns[0]) or c_indices[0] == 0:
                hit = True
            # for item in duplicates:
            #     indices = [i for i in range(len(mirror)) if mirror[i] == item]
            #     print(indices)
            #indices = [i for i in range(len(mirror)) if mirror[i] in duplicates]

            #for row in mirror:

            # row_pairs = []
            # forward_pairs = []
            # for i in range(len(mirror)):
            #     row_pairs.append((mirror[i],i,len(mirror)-1-i))
            #     print((mirror[i],i))
            
            # print(row_pairs)

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