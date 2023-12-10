import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

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
        # 13884 to high, divide by 2    
        print(len(path)/2)
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
        case "ex2":
            filename="example2.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)