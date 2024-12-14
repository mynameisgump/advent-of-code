import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

field_h = 103
field_w = 101

def print_field(field):
    for line in field:
        print("".join([str(item) for item in line]).replace("0","."))

def print_field_w_robots(robots):
    field_clone = [[0 for _ in range(field_w)] for _ in range(field_h)]
    positions = [robot[0] for robot in robots]
    print(positions)
    for position in positions:
        position[0] = position[0] % len(field_clone[0])
        position[1] = position[1] % len(field_clone)
        field_clone[position[1]][position[0]] += 1
    print_field(field_clone)

def get_quadrants(robots):
    field_clone = [[0 for _ in range(field_w)] for _ in range(field_h)]
    positions = [robot[0] for robot in robots]
    for position in positions:
        position[0] = position[0] % len(field_clone[0])
        position[1] = position[1] % len(field_clone)
        field_clone[position[1]][position[0]] += 1 

   
    rows = len(field_clone)
    cols = len(field_clone[0])
    mid_row = rows // 2
    mid_col = cols // 2

    top_left = [row[:mid_col] for row in field_clone[:mid_row]]
    top_right = [row[mid_col+1:] for row in field_clone[:mid_row]]
    bottom_left = [row[:mid_col] for row in field_clone[mid_row+1:]]
    bottom_right = [row[mid_col+1:] for row in field_clone[mid_row+1:]]

    return (top_left,top_right,bottom_left,bottom_right)


def part1(filename):
    with open(filename) as f:
        robots = [[[int(n) for n in part[2:].split(',')] for part in robot.split()] for robot in f.read().strip().split("\n")]
        field = [[0 for _ in range(field_w)] for _ in range(field_h)]
        print(robots)
        print_field(field)
        print_field_w_robots(robots)
        print(len(robots))
        for seconds in range(100):
            for r_i in range(len(robots)):
                robot = robots[r_i]
                r_position = robot[0]
                r_velocity = robot[1]
                robot[0] = [robot[0][0]+robot[1][0],robot[0][1]+robot[1][1]]
        quadrants = get_quadrants(robots)
        print()
        total = 1
        for quad in quadrants:
            # print()
            total_robots = 0
            for row in quad:
                for value in row:
                    if value != 0:
                        total_robots += value
            print("Robots:  ",total_robots)
            total *= total_robots
            print_field(quad)
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
            filename="ex1.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)