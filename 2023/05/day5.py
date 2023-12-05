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

def remove_overlap(ranges):
    result = []
    current_start = -1
    current_stop = -1 

    for start, stop in sorted(ranges):
        if start > current_stop:
            # this segment starts after the last segment stops
            # just add a new segment
            result.append( (start, stop) )
            current_start, current_stop = start, stop
        else:
            # segments overlap, replace
            result[-1] = (current_start, stop)
            # current_start already guaranteed to be lower
            current_stop = max(current_stop, stop)

    return result


def calc_seed_value(seed_num,dest,source,length):
    source_upper_bound = source+length;
    if source <= seed_num < source_upper_bound:
        dist_from_source = seed_num - source
        final_dest = dest+dist_from_source
        return final_dest
    else:
        return None
    
def check_overlap(range1, range2):
    return range1[0] < range2[1] and range2[0] < range1[1]

def overlap(start1, end1, start2, end2):
    return (
        start1 <= start2 <= end1 or
        start1 <= end2 <= end1 or
        start2 <= start1 <= end2 or
        start2 <= end1 <= end2
    )

def get_overlap_type(range1,range2):
    if range1[0] >= range2[0] and range1[1] <= range2[1]:
        return "subset"
    elif range1[0] < range2[0] and range1[1] > range2[1]:
        return "superset"
    elif range1[0] < range2[0] and range1[1] <= range2[1] and range1[1] > range2[0]:
        return "upper_inter"
    elif range1[0] >= range2[0] and range1[0] < range2[1] and range1[1] > range2[1]:
        return "lower_inter"
    else:
        return None
# Left return will be mapped seeds and right return will be unmapped seeds

def map_point(value,starting_point,destination):
    stop_dist_from_source = value - starting_point
    return(destination+stop_dist_from_source)

def calc_seed_range_value(seed_range,dest,source,length):

    source_range_lower = source
    source_range_upper = source+length
    source_range = source_range_lower,source_range_upper

    #print("Calcing overlaps and values for:", seed_range, source_range)
    unmapped_seed_ranges = []
    mapped_seed_ranges = []
    print()
    print("New comparison:")
    print("Seed Range:", seed_range)
    print("Source Range:", source_range)

    if get_overlap_type(seed_range,source_range):
        overlap_type = get_overlap_type(seed_range,source_range)
        print("Overlapping, type:", overlap_type)
        if overlap_type == "subset":
            intersection_start = seed_range[0]
            intersection_stop = seed_range[1]

            final_start_dest = map_point(intersection_start,source,dest)
            final_stop_dest = map_point(intersection_stop,source,dest)
            final_range = final_start_dest,final_stop_dest

            mapped_seed_ranges.append((final_range))
        if overlap_type == "superset":
            inter_start = source_range[0]
            inter_stop = source_range[1]
            final_inter_start_dest = map_point(inter_start,source,dest)
            final_inter_stop_dest = map_point(inter_stop,source,dest)
            
        
            mapped_seed_ranges.append((final_inter_start_dest,final_inter_stop_dest))
            # left and right
            unmapped_seed_ranges.append((seed_range[0],source_range[0]))
            unmapped_seed_ranges.append((source_range[1],seed_range[1]))
            
        if overlap_type == "upper_inter":
            print("Source Range:", source_range)
            print("Seed range:", seed_range)
            inter_start = source_range[0]
            inter_stop = seed_range[1]
            final_inter_start_dest = map_point(inter_start,source,dest)
            final_inter_stop_dest = map_point(inter_stop,source,dest)
            mapped_seed_ranges.append((final_inter_start_dest,final_inter_stop_dest))
            unmapped_seed_ranges.append((seed_range[0],source_range[0]))
        
        if overlap_type == "lower_inter":
            inter_start = seed_range[0]
            inter_stop = source_range[1]
            final_inter_start_dest = map_point(inter_start,source,dest)
            final_inter_stop_dest = map_point(inter_stop,source,dest)
            mapped_seed_ranges.append((final_inter_start_dest,final_inter_stop_dest))
            unmapped_seed_ranges.append((source_range[1],seed_range[1]))

    else:
        return None
    print("Results:", mapped_seed_ranges,unmapped_seed_ranges)
    return [mapped_seed_ranges,unmapped_seed_ranges]


# def maximize_nonoverlapping_count(intervals):
#     # sort by the end-point
#     L = sorted(intervals, key=lambda (start, end): (end, (end - start)),
#                reverse=True) # O(n*logn)
#     iv = build_interval_tree(intervals) # O(n*log n)
#     result = []
#     while L: # until there are intervals left to consider
#         # pop the interval with the smallest end-point, keep it in the result
#         result.append(L.pop()) # O(1)
#         # remove intervals that overlap with the popped interval
#         overlapping_intervals = iv.pop(result[-1]) # O(log n + m)
#         remove(overlapping_intervals, from_=L) 
#     return result




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
            #print(mapping_values)
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
            seed_range = (seed_pair[0],seed_pair[0]+seed_pair[1])
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
            print("Mapping Values: ", mapping_values)
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
                    #print("Seed Range:", seed_range)
                    new_seed_ranges.append(seed_range)

            seed_ranges = remove_overlap(new_seed_ranges)
            
            # Test nums backup: seeds: 51 2 40 100 45 10 55 10
            print("New seed Queue:", new_seed_ranges)
            total_seeds = 0
            for seed in seed_ranges:
                total_seeds += seed[1]-seed[0]
            print("Total Seeds:", total_seeds)
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
        res = min(seed_ranges, key = lambda i : i[0])[0]
        print("Result: ",res)
if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="input.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)