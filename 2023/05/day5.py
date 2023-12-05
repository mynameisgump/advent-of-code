import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();


maps = []

# Try storeing the range instead of the values 
# AKA grab the 

# Deal with jumping in the for loop
# The create this for each line:
# [source_lower,source_upper,length,dest]

def calc_seed_value(seed_num,dest,source,length):
    source_upper_bound = source+length;
    if source <= seed_num < source_upper_bound:
        dist_from_source = seed_num - source
        final_dest = dest+dist_from_source
        return final_dest
    else:
        return None

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n\n");
        print("All Lines: ",lines)
        seeds = [int(num) for num in list(filter(None, lines[:1][0].split(":")[1].split(" ")))]
        print("Seed string: ", seeds)
        map_strings = [line.split("\n") for line in lines[1:]]
        for plant_map in map_strings:
            number_strings = plant_map[1:]
            print("Maps strings: ",number_strings)
            mapping_values = []
            for number_string in number_strings:
                numbers = [int(num) for num in number_string.split(" ")]
                [dest,source,length] = [int(num) for num in number_string.split(" ")]
                source_upper_bound = source+length
                mapping_values.append([dest,source,length])
            print(mapping_values)
            new_seeds = []
            for seed_num in seeds:
                final_seed_val = seed_num
                for mapping_value in mapping_values:
                    calculated_val = calc_seed_value(seed_num,mapping_value[0],mapping_value[1],mapping_value[2])
                    if calculated_val:
                        final_seed_val = calculated_val
                print("Seed final value: ", final_seed_val)
                new_seeds.append(final_seed_val)
            seeds = new_seeds
        print("Final seed: ", min(seeds))
                # This does not work 
                # dest_values = [*range(dest,dest+length)]
                # source_values = [*range(source,source+length)]
                # new_map = dict(map(lambda x, y: (x,y), source_values, dest_values))
                # print()
                # final_map.update(new_map)
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