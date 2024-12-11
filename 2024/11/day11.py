import argparse
import re
from collections import deque
from concurrent.futures import ThreadPoolExecutor
import numpy as np
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n")[0].split(" ");
        blinks = 11
        current_index = 0

        for i in range(blinks):
            while current_index < len(lines):
                stone = lines[current_index]
                if int(stone) == 0:
                    lines[current_index] = str(1)
                elif len(stone) % 2 == 0:
                    new_stones = [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
                    lines[current_index:current_index+1] = new_stones 
                    current_index += 1
                else:
                    lines[current_index] = str(int(lines[current_index])*2024)
                    
                current_index += 1
            current_index = 0
        print(len(lines))

def part2(filename):
    with open(filename) as f:
        blinks = 75
        stone_dict = dict(Counter(f.read().split("\n")[0].split(" ")))

        for blink in range(blinks):
            new_stones = {}
            for stone, stone_value in stone_dict.items():
                if int(stone) == 0:
                    new_stones["1"] = new_stones.get("1", 0) + stone_value
                elif len(str(stone)) % 2 == 0:
                    left_stone, right_stone = str(int(stone[:len(stone)//2])),str(int(stone[len(stone)//2:]))
                    new_stones[left_stone] = new_stones.get(left_stone, 0) + stone_value
                    new_stones[right_stone] = new_stones.get(right_stone, 0) + stone_value
                else:
                    stone_mult = str(int(stone)*2024)
                    new_stones[stone_mult] = new_stones.get(stone_mult, 0) + stone_value
            stone_dict = {key: value for key, value in new_stones.items() if value != 0}
        print(sum(stone_dict.values()))



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