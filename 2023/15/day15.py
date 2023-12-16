import argparse
from collections import OrderedDict

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def hash_string(string):
    total = 0
    for char in string:
        total += ord(char)
        total *= 17
        total %= 256
    return total

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n")[0].split(",");
        total = 0 
        for string in lines:
            total += hash_string(string)
        print(total)

def part2(filename):
    with open(filename) as f:
        lines = f.read().split("\n")[0].split(",");
        total = 0 
        hashmap = {k: OrderedDict() for k in range(256)}
        for string in lines:
            if "=" in string:
                [label, focal_length] = string.split("=")
                print(label,focal_length)
                box_num = hash_string(label)
                hashmap[box_num][label] = int(focal_length)
                pass
            elif "-" in string:
                label = string.replace("-","")
                box_num = hash_string(label)
                if label in hashmap[box_num]:
                    del hashmap[box_num][label]
        filtered_dict = {k: v for k, v in hashmap.items() if len(v) > 0}
        print(filtered_dict)
        values = []
        for box_num, items in filtered_dict.items():
            cur_index = 0 
            for label,focal_length in items.items():
                cur_index += 1
                values.append((box_num+1)*cur_index*focal_length)
        print(sum(values))
            # total += (1+box_num)*
            # print(box_num,items)

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