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
    
def check_overlap(range1, range2):
    return range1.start < range2.stop and range2.start < range1.stop
# Left return will be mapped seeds and right return will be unmapped seeds
def calc_seed_range_value(seed_range,dest,source,length):
    print()
    print("Calcing range value: ", seed_range,dest,source,length)
    seed_range_lower = seed_range[0]
    seed_range_upper = seed_range[1]
    seed_range = range(seed_range[0],seed_range[1])
    
    
    source_range_lower = source
    source_range_upper = source+length
    source_range = range(source_range_lower,source_range_upper)

    unmapped_seed_ranges = []
    mapped_seed_ranges = []

    print("Seed Range: ", seed_range);
    print("Source Range: ", source_range);
    if check_overlap(seed_range,source_range):
        print("Ranges overlap")
        intersection_start = max(seed_range.start, source_range.start)
        intersection_stop = min(seed_range.stop, source_range.stop)
        
        # only works if subset of section 
        
        final_range = range(dest+(intersection_start-source_range_lower),dest+(intersection_stop-source_range_lower))
        mapped_seed_ranges.append(final_range)
    
        # if source_range.start > start:
        #     start = source_range.start

        # Calculate the difference for the stop
        # if source_range.stop < stop:
        #     stop = source_range.stop

        # if start < stop:
        #     return range(start, stop) 
        #difference_stop = 
        #print(range(start,stop))


    else:
        unmapped_seed_ranges = seed_range
        return [mapped_seed_ranges,unmapped_seed_ranges]
    # if seed_range_lower >= source_range_lower and seed_range_upper < source_range_upper:

    #     print("seed in incapsulated in the mapping range")
    

    

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


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
                    calculated_val = calc_seed_value(seed_num,)
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
        lines = f.read().split("\n\n");
        print("All Lines: ",lines)
        seeds = [int(num) for num in list(filter(None, lines[:1][0].split(":")[1].split(" ")))]
        chunked_seeds = list(chunks(seeds,2))
        seed_ranges = []
        for seed_pair in chunked_seeds:
            seed_range = [seed_pair[0],seed_pair[0]+seed_pair[1]]
            print(seed_range)
            seed_ranges.append(seed_range);
        
        print(seed_ranges)
        map_strings = [line.split("\n") for line in lines[1:]]
        for plant_map in map_strings:
            number_strings = plant_map[1:]
            #print("Maps strings: ",number_strings)
            mapping_values = []
            for number_string in number_strings:
                numbers = [int(num) for num in number_string.split(" ")]
                [dest,source,length] = [int(num) for num in number_string.split(" ")]
                source_upper_bound = source+length
                mapping_values.append([dest,source,length])
            new_seed_ranges = []
            for seed_range in seed_ranges:
                final_seed_range = seed_range
                cur_seed_range = seed_range
                for mapping_value in mapping_values:
                    calculated_val = calc_seed_range_value(seed_range,mapping_value[0],mapping_value[1],mapping_value[2])
            #print(mapping_values)
            # new_seeds = []
            # for seed_num in seeds:
            #     final_seed_val = seed_num
            #     for mapping_value in mapping_values:
            #         calculated_val = calc_seed_value(seed_num,mapping_value[0],mapping_value[1],mapping_value[2])
            #         if calculated_val:
            #             final_seed_val = calculated_val
            #     print("Seed final value: ", final_seed_val)
            #     new_seeds.append(final_seed_val)
            # seeds = new_seeds
        # print("Final seed: ", min(seeds))
       
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