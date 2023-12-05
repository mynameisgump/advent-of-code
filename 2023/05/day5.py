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

def get_overlap_type(range1,range2):
    if range1.start > range2.start and range1.stop < range2.stop:
        return "subset"
    elif range1.start < range2.start and range1.stop > range2.stop:
        return "superset"
    elif range1.start < range2.start and range1.stop < range2.stop:
        return "upper_inter"
    elif range1.start > range2.start and range1.stop > range2.stop:
        return "lower_inter"
# Left return will be mapped seeds and right return will be unmapped seeds

def map_point(value,starting_point,destination):
    stop_dist_from_source = value - starting_point
    return(destination+stop_dist_from_source)

def calc_seed_range_value(seed_range,dest,source,length):

    source_range_lower = source
    source_range_upper = source+length
    source_range = range(source_range_lower,source_range_upper)

    print("Calcing overlaps and values for:", seed_range, source_range)
    unmapped_seed_ranges = []
    mapped_seed_ranges = []


    if check_overlap(seed_range,source_range):
        overlap_type = get_overlap_type(seed_range,source_range)
        print("Overlapping, type:", overlap_type)
        if overlap_type == "subset":
            intersection_start = seed_range.start
            intersection_stop = seed_range.stop

            final_start_dest = map_point(intersection_start,source,dest)
            final_stop_dest = map_point(intersection_stop,source,dest)
            final_range = range(final_start_dest,final_stop_dest)

            mapped_seed_ranges.append(final_range)
        if overlap_type == "superset":
            inter_start = source_range.start
            inter_stop = source_range.stop
            final_inter_start_dest = map_point(inter_start,source,dest)
            final_inter_stop_dest = map_point(inter_stop,source,dest)
            
        
            mapped_seed_ranges.append(range(final_inter_start_dest,final_inter_stop_dest))
            # left and right
            unmapped_seed_ranges.append(range(seed_range.start,source_range.start))
            unmapped_seed_ranges.append(range(source_range.stop,seed_range.stop))
            
        if overlap_type == "upper_inter":
            inter_start = source_range.start
            inter_stop = seed_range.stop
            final_inter_start_dest = map_point(inter_start,source,dest)
            final_inter_stop_dest = map_point(inter_stop,source,dest)
            mapped_seed_ranges.append(range(final_inter_start_dest,final_inter_stop_dest))
            unmapped_seed_ranges.append(range(seed_range.start,source_range.start))
        
        if overlap_type == "lower_inter":
            inter_start = seed_range.start
            inter_stop = source_range.stop
            final_inter_start_dest = map_point(inter_start,source,dest)
            final_inter_stop_dest = map_point(inter_stop,source,dest)
            mapped_seed_ranges.append(range(final_inter_start_dest,final_inter_stop_dest))
            unmapped_seed_ranges.append(range(source_range.stop+1,seed_range.stop))

    else:
        return None
    print("Results:", mapped_seed_ranges,unmapped_seed_ranges)
    return [mapped_seed_ranges,unmapped_seed_ranges]


    

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
        seeds = [int(num) for num in list(filter(None, lines[:1][0].split(":")[1].split(" ")))]
        chunked_seeds = list(chunks(seeds,2))
        seed_ranges = []
        for seed_pair in chunked_seeds:
            seed_range = range(seed_pair[0],seed_pair[0]+seed_pair[1])
            seed_ranges.append(seed_range);
        
        map_strings = [line.split("\n") for line in lines[1:]]
        for plant_map in map_strings:
            print()
            print("||||||||||||||||||||||||||||||||")
            print("New Map:")
            number_strings = plant_map[1:]

            mapping_values = []
            for number_string in number_strings:
                numbers = [int(num) for num in number_string.split(" ")]
                [dest,source,length] = [int(num) for num in number_string.split(" ")]
                source_upper_bound = source+length
                mapping_values.append([dest,source,length])
            
            new_seed_ranges = []
            seed_queue = seed_ranges.copy()
            while len(seed_queue) > 0:
                seed_range = seed_queue.pop(0)
                print("Popped_seed:", seed_range)
                split = False
                for mapping_value in mapping_values:
                    calculated_seed_ranges = calc_seed_range_value(seed_range,mapping_value[0],mapping_value[1],mapping_value[2])
                    if calculated_seed_ranges:
                        split = True
                        print(calculated_seed_ranges[1])
                        new_seed_ranges.extend(calculated_seed_ranges[0])
                        seed_queue.extend(calculated_seed_ranges[1])
                if split == False:
                    new_seed_ranges.append(seed_range)
            seed_ranges = new_seed_ranges
            print("New seed Queue:", new_seed_ranges)
            # for seed_range in seed_ranges:
            #     final_seed_range = seed_range
            #     cur_seed_range = seed_range
            #     for mapping_value in mapping_values:
            #         calculated_val = calc_seed_range_value(seed_range,mapping_value[0],mapping_value[1],mapping_value[2])
            #         if calculated_val:
            #             print("Stuff was done")
            #             mapped_seed_ranges.extend(calculated_val[0])
            #             unmapped_seed_ranges.extend(calculated_val[1])
                    
                        
                    
            #         print("Calculated return:", calculated_val)

       
if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="testCase.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)