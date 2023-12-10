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
    return positions

def valid_positions(position, area_map):
    print("In Valid positions")
    print("Position:",position)
    adj_positions = [(position[0],position[1]+1),
                (position[0],position[1]-1),
                (position[0]+1,position[1]),
                (position[0]-1,position[1])
                ]
    valid_pos = set()
    valid_pos.add(position)
    for adj_pos in adj_positions:
        print("Pain")
        pos_char = area_map[adj_pos[0]][adj_pos[1]]
        positions = get_pipe_pos(pos_char,adj_pos)
        print(pos_char)
        print(positions)
        if position in positions:
            valid_pos.add(adj_pos)
        # print(pos_char)
        # print(adj_pos)
    print(valid_pos)
    pass

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n");
        area_map = [[*line] for line in lines]
        for area in area_map:
            print(area)
        print(lines)
        start_position = 0
        path = set()
        for i in range(len(lines)):
            line = lines[i]
            if line.find("S") != -1:
                start_position = (i,line.find("S"))
        print(start_position)
        path.add(start_position)
        test = valid_positions(start_position, area_map)
        print("Test:",test)

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