import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1", "p2"])
parser.add_argument("input", choices=["i1", "ex1", "ex2"])
args = parser.parse_args()

def check_horizontal(lines, row, col, map):
    string = ""
    current_index = col
    while current_index + 1 <= len(lines[row]) and len(string) < 4:
        string += lines[row][current_index]
        current_index += 1
    if string == "XMAS" or string == "SAMX":
        if string == "XMAS":
            map[row][col] = "X"
            map[row][col + 1] = "M"
            map[row][col + 2] = "A"
            map[row][col + 3] = "S"
        else:
            map[row][col] = "S"
            map[row][col + 1] = "A"
            map[row][col + 2] = "M"
            map[row][col + 3] = "X"
        return 1
    else:
        return 0


def check_right_diagonal(lines, row, col, map):
    string = ""
    current_row = row
    current_col = col
    while (
        current_row + 1 <= len(lines)
        and current_col + 1 <= len(lines[row])
        and len(string) < 4
    ):
        string += lines[current_row][current_col]
        current_row += 1
        current_col += 1
    print(string, current_row, current_col)
    if string == "XMAS" or string == "SAMX":
        if string == "XMAS":
            map[row][col] = "X"
            map[row + 1][col + 1] = "M"
            map[row + 2][col + 2] = "A"
            map[row + 3][col + 3] = "S"
        else:
            map[row][col] = "S"
            map[row + 1][col + 1] = "A"
            map[row + 2][col + 2] = "M"
            map[row + 3][col + 3] = "X"
        return 1
    else:
        return 0


def check_left_diagonal(lines, row, col, map):
    string = ""
    current_row = row
    current_col = col
    string += lines[current_row][current_col]
    while current_row + 1 < len(lines) and current_col - 1 >= 0 and len(string) < 4:
        current_row += 1
        current_col -= 1
        string += lines[current_row][current_col]
    if string == "XMAS" or string == "SAMX":
        if string == "XMAS":
            map[row][col] = "X"
            map[row + 1][col - 1] = "M"
            map[row + 2][col - 2] = "A"
            map[row + 3][col - 3] = "S"
        else:
            map[row][col] = "S"
            map[row + 1][col - 1] = "A"
            map[row + 2][col - 2] = "M"
            map[row + 3][col - 3] = "X"
        return 1
    else:
        return 0


def check_vertical(lines, row, col, map):
    string = ""
    current_index = row
    while current_index + 1 <= len(lines) and len(string) < 4:
        string += lines[current_index][col]
        current_index += 1
    if string == "XMAS" or string == "SAMX":
        if string == "XMAS":
            map[row][col] = "X"
            map[row + 1][col] = "M"
            map[row + 2][col] = "A"
            map[row + 3][col] = "S"
        else:
            map[row][col] = "S"
            map[row + 1][col] = "A"
            map[row + 2][col] = "M"
            map[row + 3][col] = "X"
        return 1
    else:
        return 0


def xmas_checker(lines, row, col, map):
    center = lines[row][col]
    if center != "A":
        return 0
    bl_to_tr_diag = ""
    br_to_tl_diag = ""
    if (
        row + 1 < len(lines)
        and row - 1 >= 0
        and (col + 1) < len(lines[row])
        and (col - 1) >= 0
    ):
        bl_to_tr_diag += lines[row + 1][col - 1]
        bl_to_tr_diag += lines[row][col]
        bl_to_tr_diag += lines[row - 1][col + 1]

        br_to_tl_diag += lines[row + 1][col + 1]
        br_to_tl_diag += lines[row][col]
        br_to_tl_diag += lines[row - 1][col - 1]
    if bl_to_tr_diag == "SAM" or bl_to_tr_diag == "MAS":
        if br_to_tl_diag == "SAM" or br_to_tl_diag == "MAS":
            return 1
    return 0


def part1(filename):
    with open(filename) as f:
        lines = [list(line) for line in f.read().split("\n")]
        total = 0
        map = []
        for row in range(len(lines)):
            map.append([])
            for col in range(len(lines[row])):
                map[row].append(".")

        for row in range(len(lines)):
            for col in range(len(lines[row])):
                total += check_horizontal(lines, row, col, map)
                total += check_vertical(lines, row, col, map)
                total += check_right_diagonal(lines, row, col, map)
                total += check_left_diagonal(lines, row, col, map)
        for row in map:
            print("".join(row))
    print("Total:", total)


def part2(filename):
    with open(filename) as f:
        lines = [list(line) for line in f.read().split("\n")]
        total = 0
        map = []
        for row in range(len(lines)):
            map.append([])
            for col in range(len(lines[row])):
                map[row].append(".")

        for row in range(len(lines)):
            for col in range(len(lines[row])):
                total += xmas_checker(lines, row, col, map)
        
        for row in map:
            print("".join(row))

        print(total)


if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution
    filename = ""
    match input_selection:
        case "i1":
            filename = "input.txt"
        case "ex1":
            filename = "ex1.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)
