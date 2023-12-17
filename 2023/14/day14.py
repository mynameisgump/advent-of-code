import argparse
import re
from dataclasses import dataclass
from functools import cache
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

rows_answers = {}
rows_cycles = {}
@cache
def cycle(rows_tuple):
    rows = list(list(sub) for sub in rows_tuple)
    for i in range(4):
        for col in range(len(rows[0])):
            cur_collisions = []
            hit_empty = False
            for row in range(len(rows)):
                char = rows[row][col]
                match char:
                    case "O":
                        if not hit_empty:
                            cur_collisions.append("#")
                        else:        
                            dist = len(cur_collisions)-1
                            final_index = len(cur_collisions)-1
                            while dist >= 0:
                                comp_char = cur_collisions[dist]
                                if comp_char == ".":
                                    final_index = dist
                                if comp_char == "#":
                                    break
                                dist -= 1
                            rows[final_index][col] = "O"
                            rows[row][col] = "."
                            cur_collisions[final_index] = "#"
                            cur_collisions.append(".")
                    case ".":
                        hit_empty = True
                        cur_collisions.append(".")
                    case "#":
                        hit_empty = False
                        cur_collisions.append("#")
        rows = [list(row) for row in zip(*rows[::-1])]
    return tuple(tuple(sub) for sub in rows)  

def print_matrix(matrix):
    print()
    for row in matrix:
        print("".join(row))
# 112773
def part1(filename):
    with open(filename) as f:
        rows = [[*row] for row in f.read().split("\n")];
        columns = []
        for i in range(len(rows[0])):
            cur_column = []
            for row in rows:
                cur_column.append(row[i])
            columns.append(cur_column)
        for col in range(len(rows[0])):
            cur_collisions = []
            hit_empty = False
            for row in range(len(rows)):
                char = rows[row][col]
                match char:
                    case "O":
                        if not hit_empty:
                            cur_collisions.append("#")
                        else:        
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
                            rows[final_index][col] = "O"
                            rows[row][col] = "."
                            cur_collisions[final_index] = "#"
                            cur_collisions.append(".")
                    case ".":
                        hit_empty = True
                        cur_collisions.append(".")
                    case "#":
                        hit_empty = False
                        cur_collisions.append("#")
        print("Rows: ")
        print_matrix(rows)
        total = 0
        row_load = len(rows)
        for row in rows:
            print(row.count("O"))
            total += row.count("O") * row_load
            row_load -= 1
        print(total)
            
        #print(lines)


def part2(filename):
    with open(filename) as f:
        rows = [[*row] for row in f.read().split("\n")];
        # print_matrix(rows)
        # rows = cycle(rows)
        # print()
        # print_matrix(rows)
        rows = tuple(tuple(sub) for sub in rows);
        for z in range(1000):
            
            rows = cycle(rows)
            #print_matrix(rows)
            total = 0
            row_load = len(rows)
            for row in rows:
                total += row.count("O") * row_load
                row_load -= 1
            print(z, total)
        
        #     for i in range(4):
        #         for col in range(len(rows[0])):
        #             cur_collisions = []
        #             hit_empty = False
        #             for row in range(len(rows)):
        #                 char = rows[row][col]
        #                 match char:
        #                     case "O":
        #                         if not hit_empty:
        #                             cur_collisions.append("#")
        #                         else:        
        #                             dist = len(cur_collisions)-1
        #                             final_index = len(cur_collisions)-1
        #                             while dist >= 0:
        #                                 comp_char = cur_collisions[dist]
        #                                 if comp_char == ".":
        #                                     final_index = dist
        #                                 if comp_char == "#":
        #                                     break
        #                                 dist -= 1
        #                             rows[final_index][col] = "O"
        #                             rows[row][col] = "."
        #                             cur_collisions[final_index] = "#"
        #                             cur_collisions.append(".")
        #                     case ".":
        #                         hit_empty = True
        #                         cur_collisions.append(".")
        #                     case "#":
        #                         hit_empty = False
        #                         cur_collisions.append("#")
        #         # print("After turn:")
        #         # print_matrix(rows)
        #         # print() 98887 too low 
        #         # 98898 
        #         rows = [list(row) for row in zip(*rows[::-1])]
            
        #     total = 0
        #     row_load = len(rows)
        #     for row in rows:
        #         total += row.count("O") * row_load
        #         row_load -= 1
        #     print(z, total)

        #print_matrix(rows)98893m98894
        
        #print(total)
            

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