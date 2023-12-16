import argparse
import re
from dataclasses import dataclass

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();


def print_matrix(matrix):
    for row in matrix:
        print("".join(row))

def part1(filename):
    with open(filename) as f:
        rows = [[*row] for row in f.read().split("\n")];
        columns = []
        for i in range(len(rows[0])):
            cur_column = []
            for row in rows:
                cur_column.append(row[i])
            columns.append(cur_column)
        print_matrix(rows)
        print()
        print_matrix(columns)
        for col in range(len(rows[0])):
            print()
            print("Processing Column: ", columns[col])
            cur_collisions = []
            hit_empty = False
            for row in range(len(rows)):
                char = rows[row][col]
                print(char)
                match char:
                    case "O":
                        if not hit_empty:
                            cur_collisions.append("#")
                        else:
                            print("ZZZZZ")
                            print(cur_collisions)            
                            empty = True 
                            dist = len(cur_collisions)-1
                            final_index = len(cur_collisions)-1
                            while dist >= 0:
                                comp_char = cur_collisions[dist]
                                if comp_char == ".":
                                    final_index = dist
                                if comp_char == "#":
                                    break
                                dist -= 1
                            print("Final Index: ",final_index)
                            print_matrix(rows)
                            rows[final_index][col] = "O"
                            rows[row][col] = "."
                            print()
                            print_matrix(rows)
                            cur_collisions[final_index] = "#"
                            cur_collisions.append(".")
                    case ".":
                        hit_empty = True
                        cur_collisions.append(".")
                    case "#":
                        hit_empty = False
                        cur_collisions.append("#")
                print(cur_collisions)

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