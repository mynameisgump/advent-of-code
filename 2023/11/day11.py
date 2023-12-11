import argparse
import re
import math
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def manhattan(a, b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))

def print_grid(grid):
    print()
    for item in grid:
        print("".join(item))

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n");
        star_map = [[*line] for line in lines]
        rows = [[*line] for line in lines]
        

        row_length = len(star_map)
        total_empty = 0
        print_grid(star_map)

        rows_to_increase = []
        for i in range(len(rows)):
            row = rows[i]
            if all(val == "." for val in row):
                rows_to_increase.append(i)

        
        print(rows_to_increase)

        rows_added = 0
        for row_num in rows_to_increase:
            star_map.insert(row_num+rows_added,[*"."*row_length])
            rows_added += 1
        print_grid(star_map)

        columns = []
        for i in range(len(star_map[0])):
            cur_column = []
            for row in star_map:
                cur_column.append(row[i])
            columns.append(cur_column)

        column_length = len(columns[0])

        columns_to_increase = []
        for i in range(len(columns)):
            column = columns[i]
            if all(val == "." for val in column):
                columns_to_increase.append(i)

        columns_added = 0
        for column_num in columns_to_increase:
            for row in star_map:
                row.insert(column_num+columns_added,".")
            columns_added += 1
        print_grid(star_map)

        points = []
        for i in range(len(star_map)):
            row = star_map[i]
            for x in range(len(row)):
                char = row[x]
                if char == "#":
                    points.append((i,x))
        distances = {}
        cur_galaxy = 1
        total = 0 
        distance_pair = {}
        for point_1 in points:
            print("Cur Galaxy:", cur_galaxy)
            distances[cur_galaxy] = []
            galaxy_2 = 1
            for point_2 in points:                    
                if point_1 != point_2:
                    dis = 0
                    for i in range(len(point_1)):
                        dis += abs(point_1[i] - point_2[i])
                    print(galaxy_2,dis)
                    total+=dis
                    #distances[cur_galaxy] = distances[cur_galaxy]+[[galaxy_2,manhattan(point_1,point_2)]]
                galaxy_2 += 1
            cur_galaxy += 1
        #print(points)
        #print(distances)
        print(total)


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