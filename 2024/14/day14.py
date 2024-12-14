import argparse
import numpy as np
from PIL import Image


def matrix_to_image(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    img = Image.new("1", (cols, rows), color=0)

    pixels = img.load()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != ".":
                pixels[j, i] = 1

    return img


parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1", "p2"])
parser.add_argument("input", choices=["i1", "ex1", "ex2"])
args = parser.parse_args()

field_h = 103
field_w = 101


def print_field(field):
    for line in field:
        print("".join("." if item == 0 else str(item) for item in line))


def print_field_w_robots(robots):
    field_clone = np.zeros((field_h, field_w), dtype=int)
    for robot in robots:
        x, y = robot[0][0] % field_w, robot[0][1] % field_h
        field_clone[y][x] += 1

    field_clone = np.where(field_clone == 0, ".", field_clone)
    return field_clone


def get_quadrants(robots):
    field_clone = np.zeros((field_h, field_w), dtype=int)
    for robot in robots:
        x, y = robot[0][0] % field_w, robot[0][1] % field_h
        field_clone[y][x] += 1

    mid_row, mid_col = field_h // 2, field_w // 2

    top_left = field_clone[:mid_row, :mid_col]
    top_right = field_clone[:mid_row, mid_col + 1 :]
    bottom_left = field_clone[mid_row + 1 :, :mid_col]
    bottom_right = field_clone[mid_row + 1 :, mid_col + 1 :]

    return top_left, top_right, bottom_left, bottom_right


def part1(filename):
    with open(filename) as f:
        robots = [
            [[int(n) for n in part[2:].split(",")] for part in robot.split()]
            for robot in f.read().strip().split("\n")
        ]
        field = np.zeros((field_h, field_w), dtype=int)

        for seconds in range(100):
            for r_i in range(len(robots)):
                robot = robots[r_i]
                robots[r_i][0] = [robot[0][0] + robot[1][0], robot[0][1] + robot[1][1]]

        quadrants = get_quadrants(robots)

        total = 1
        for quad in quadrants:
            total_robots = np.sum(quad)
            total *= total_robots
        print("Total")


def part2(filename):
    with open(filename) as f:
        robots = [
            [[int(n) for n in part[2:].split(",")] for part in robot.split()]
            for robot in f.read().strip().split("\n")
        ]
        for seconds in range(10000):
            for r_i in range(len(robots)):
                robot = robots[r_i]
                robots[r_i][0] = [robot[0][0] + robot[1][0], robot[0][1] + robot[1][1]]
            field = print_field_w_robots(robots)
            img = matrix_to_image(field)
            img.save(f"./images/{seconds}.bmp", optimize=True, compress_level=3)


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
