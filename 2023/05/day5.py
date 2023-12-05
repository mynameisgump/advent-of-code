import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();


maps = []

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n\n");
        print("All Lines: ",lines)
        seeds_string = [int(num) for num in list(filter(None, lines[:1][0].split(":")[1].split(" ")))]
        print("Seed string: ", seeds_string)
        map_strings = [line.split("\n") for line in lines[1:]]
        for plant_map in map_strings:
            number_strings = plant_map[1:]
            print("Maps strings: ",number_strings)
            final_map = {}
            for number_string in number_strings:
                numbers = [int(num) for num in number_string.split(" ")]
                [dest,source,length] = [int(num) for num in number_string.split(" ")]
                dest_values = [*range(dest,dest+length)]
                source_values = [*range(source,source+length)]
                new_map = dict(map(lambda x, y: (x,y), source_values, dest_values))
                print()
                final_map.update(new_map)
            print(final_map)

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