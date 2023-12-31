import argparse
import re
import collections

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2","ex3","tst"])
args = parser.parse_args();

# Two main options that I could try:
# Calc edges and full tuples ((0,1)(0,2)(0,3)) etc. and check for how many edges total in the raycast
# Figure out weird count math for determining this
# What we know:
# there will be an even number of corners in the cast every time, so I would say count them as 1
# For left and Right if there's a corner, the only thing that matter is how many |

# New Test: 
# Full Columns and Rows
# Filter out | or - depending on the problem 
# 
corner_pair_val = {
    ('F','J'): 1,
    ('F','7'): 2,
    ('L','J'): 2,
    ('L','7'): 1,
}

def corner_count(freq_dict):
    count = 0
    for key, value in freq_dict.items():
        if key != "-" and key != "|":
            count += value
    return count

def get_pipe_pos(pipe_char,position):
    positions = []
    if pipe_char == "|":
        positions.append((position[0]-1,position[1]))
        positions.append((position[0]+1,position[1]))
    elif pipe_char == "-":
        positions.append((position[0],position[1]-1))
        positions.append((position[0],position[1]+1))
    elif pipe_char == "L":
        positions.append((position[0]-1,position[1]))
        positions.append((position[0],position[1]+1))
    elif pipe_char == "J":
        positions.append((position[0]-1,position[1]))
        positions.append((position[0],position[1]-1))
    elif pipe_char == "7":
        positions.append((position[0]+1,position[1]))
        positions.append((position[0],position[1]-1))
    elif pipe_char == "F":
        positions.append((position[0]+1,position[1]))
        positions.append((position[0],position[1]+1))
    elif pipe_char == "S":
        positions.append((position[0],position[1]-1))
        positions.append((position[0],position[1]+1))
        positions.append((position[0]-1,position[1]))
        positions.append((position[0]+1,position[1]))
    return positions

def valid_positions(start_position, area_map):
    starting_char = area_map[start_position[0]][start_position[1]]
    if starting_char == "S":
        valid_pos = []
        adj_positions = get_pipe_pos(starting_char,start_position)
        for adj_pos in adj_positions:
            pos_char = area_map[adj_pos[0]][adj_pos[1]]
            positions = get_pipe_pos(pos_char,adj_pos)
            if start_position in positions:
                valid_pos.append(adj_pos)
        return valid_pos
    else:
        new_positions = get_pipe_pos(starting_char,start_position)
        return new_positions

def filter_straight(char):
    if char != "-" and char != "|":
        return True
    else:
        return False

def map_corner_pair(pair):
    return corner_pair_val[pair]

def get_s_pipe_type(start_position, area_map):
    starting_char = area_map[start_position[0]][start_position[1]]
    if starting_char == "S":
        valid_pos = []
        adj_positions = get_pipe_pos(starting_char,start_position)
        for adj_pos in adj_positions:
            pos_char = area_map[adj_pos[0]][adj_pos[1]]
            positions = get_pipe_pos(pos_char,adj_pos)
            if start_position in positions:
                valid_pos.append(adj_pos)
        init = start_position
        if (init[0]-1,init[1]) in valid_pos and (init[0]+1,init[1]) in valid_pos:
            return "|"
        elif (init[0],init[1]-1) in valid_pos and (init[0],init[1]+1) in valid_pos:
            print("Dashy")
            return "-"
        elif (init[0]-1,init[1]) in valid_pos and (init[0]+1,init[1]) in valid_pos:
            return "|"
        elif (init[0]+1,init[1]) in valid_pos and (init[0],init[1]+1) in valid_pos:
            return "F"
        elif (init[0]-1,init[1]) in valid_pos and (init[0],init[1]+1) in valid_pos:
            return "L"
        elif (init[0],init[1]-1) in valid_pos and (init[0]+1,init[1]) in valid_pos:
            return "7"
        elif (init[0],init[1]-1) in valid_pos and (init[0]-1,init[1]) in valid_pos:
            return "J"
        
def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n");
        area_map = [[*line] for line in lines]
        for area in area_map:
            print(area)
        start_position = 0
        for i in range(len(lines)):
            line = lines[i]
            if line.find("S") != -1:
                start_position = (i,line.find("S"))

        path = set()
        visited = set()
        queue = [start_position]
        print("Start Post:", start_position)
        while len(queue) > 0:
            print("Current Queue:", queue)
            cur_pos = queue.pop()
            print("Current Position: ",cur_pos)
            visited.add(cur_pos)
            path.add(cur_pos)
            new_positions = valid_positions(cur_pos, area_map)
            print("New Positions: ",new_positions)
            for new_pos in new_positions:
                print("New pos:", new_pos)
                if new_pos not in visited:
                    queue.append(new_pos)
            print()
        print(len(path)/2)

def part2(filename):
    with open(filename) as f:
        lines = f.read().split("\n");
        area_map = [[*line] for line in lines]
        def map_pos(pos):
            return area_map[pos[0]][pos[1]]

        for area in area_map:
            print(area)
        start_position = 0
        for i in range(len(lines)):
            line = lines[i]
            if line.find("S") != -1:
                start_position = (i,line.find("S"))

        path = set()
        visited = set()
        queue = [start_position]
        while len(queue) > 0:
            cur_pos = queue.pop()
            visited.add(cur_pos)
            path.add(cur_pos)
            new_positions = valid_positions(cur_pos, area_map)
            for new_pos in new_positions:
                if new_pos not in visited:
                    queue.append(new_pos)
        path.add(start_position)
        area_map[start_position[0]][start_position[1]] = get_s_pipe_type(start_position,area_map)
        hits = 0
        for row in range(len(area_map)):
            for column in range(len(area_map[0])):
                #print("Current Val:", (row,column))
                if (row,column) not in path:                
                    left_to_right_ray = set([(row,n) for n in range(0, column, 1)])

                    l_to_r_count = 0
                    l_to_r_inter = list(path.intersection(left_to_right_ray))
                    l_to_r_inter.sort(key = lambda x: x[1]) 
                    l_to_r_corner_chars = list(filter(filter_straight,list(map(map_pos,l_to_r_inter))))
                    l_to_r_corner_pairs = [(l_to_r_corner_chars[i],l_to_r_corner_chars[i + 1]) for i in range(0, len(l_to_r_corner_chars), 2)]
                    l_to_r_pair_vals = sum(list(map(map_corner_pair,l_to_r_corner_pairs)))
                    l_to_r_freq = dict(collections.Counter(list(map(map_pos,path.intersection(left_to_right_ray)))))
        
                    
                    final_val = 0
                    final_val += l_to_r_pair_vals
                    if "|" in l_to_r_freq:
                        final_val += l_to_r_freq["|"]
                    
                    if row == 3 and column == 14:
                        print()
                        print("YYYYYYYEEEEEHHHHHHHH")
                        print("Point: ", (row,column))
                        print(l_to_r_inter)
                        print("Iter: ", l_to_r_pair_vals)
                        print("Corner Vals: ", l_to_r_pair_vals)
                        print("Final Val: ", final_val)

                    if final_val % 2:
                        print()
                        print("YYYYYYYEEEEEHHHHHHHH")
                        print("Point: ", (row,column))
                        print(l_to_r_inter)
                        print("Iter: ", l_to_r_pair_vals)
                        print("Corner Vals: ", l_to_r_pair_vals)
                        print("Final Val: ", final_val)
                        hits += 1
                        # print("Left to right Ita:", left_to_right_freq)
                        # print("Up to down Ita: ", up_to_down_freq)
                        # print("Corner counts: ", corner_count(left_to_right_freq)//2)
                    
                    # left_to_right_count = 0
                    # left_to_right_count += corner_count(left_to_right_freq)//2
                    # if "|" in left_to_right_freq:
                    #     left_to_right_count += left_to_right_freq["|"]
                    # up_to_down_count = 0
                    # up_to_down_count += corner_count(up_to_down_freq)//2
                    # if "-" in up_to_down_freq:
                    #     up_to_down_count += up_to_down_freq["-"]

                    # if left_to_right_count % 2 and \
                    #     up_to_down_count % 2:
                    #     hits += 1
        print("Total hits: ",hits)

if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="example1.txt"
        case "ex2":
            filename="example2.txt"
        case "ex3":
            filename="example3.txt"
        case "test":
            filename="test.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)