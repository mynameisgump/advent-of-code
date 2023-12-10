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
        hits = 0
        for row in range(len(area_map)):
            for column in range(len(area_map[0])):
                #print("Current Val:", (row,column))
                if (row,column) not in path:                
                # Left search 
                    left_ray = set([(row,n) for n in range(0, column, 1)])
                    right_ray = set([(row,n) for n in range(column+1, len(area_map[0]), 1)])
                    up_ray = set([(n,column) for n in range(0, row, 1)])
                    down_ray = set([(n,column) for n in range(row+1, len(area_map), 1)])

                    left_inter = dict(collections.Counter(list(map(map_pos,path.intersection(left_ray)))))
                    right_inter = dict(collections.Counter(list(map(map_pos,path.intersection(right_ray)))))
                    up_inter = dict(collections.Counter(list(map(map_pos,path.intersection(up_ray)))))
                    down_inter = dict(collections.Counter(list(map(map_pos,path.intersection(down_ray)))))
                    print()
                    if row == 3 and column == 14:
                        print("YYYYYYYEEEEEHHHHHHHH")
                    print("Point: ", (row,column))
                    print("Left Ita: ",left_inter)
                    print("Right Ita: ", right_inter)
                    print("Up ita: ", up_inter)
                    print("Down ita: ", down_inter)

                    print("Corner counts: ", corner_count(left_inter), corner_count(right_inter), corner_count(up_inter),corner_count(down_inter))
                    if "|" in left_inter:
                        print("Filtered Left: ", left_inter["|"])

                    left_heur = 
                    # right_inter = len(path.intersection(right_ray))
                    # up_inter = len(path.intersection(up_ray))
                    # down_inter = len(path.intersection(down_ray))

                    if sum(left_inter.values()) % 2 and \
                        sum(right_inter.values()) % 2 and \
                        sum(up_inter.values()) % 2 and \
                        sum(down_inter.values()) % 2:
                        print(left_inter,right_inter,up_inter,down_inter)
                        print("HiTTTTTTTTt val:", (row,column))
                        hits += 1
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