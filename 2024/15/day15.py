import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def print_matrix(matrix):
    for row in matrix:
        print("".join(row))

def part1(filename):
    with open(filename) as f:
        map_in, movements = f.read().split("\n\n");
        w_map = [list(line) for line in map_in.split("\n")]
        cur_loc = next((i, j) for i, row in enumerate(w_map) for j, val in enumerate(row) if val == '@')
        movements = "".join(movements.split("\n"))
        for direction in movements:   
                next_step = []
                if direction == "^":
                    next_step = [cur_loc[0]-1,cur_loc[1]]
                elif direction == ">":
                    next_step = [cur_loc[0],cur_loc[1]+1]
                elif direction == "<":
                    next_step = [cur_loc[0],cur_loc[1]-1]
                elif direction == "v":
                    next_step = [cur_loc[0]+1,cur_loc[1]]

                if len(next_step) == 0:
                    break
                if next_step[0] >= len(w_map) or next_step[0] < 0 or next_step[1] >= len(w_map[0]) or next_step[1] < 0:
                    break

                next_char = w_map[next_step[0]][next_step[1]]
                if next_char == ".":
                    w_map[next_step[0]][next_step[1]] = "@"
                    w_map[cur_loc[0]][cur_loc[1]] = "."
                    cur_loc = next_step
                elif next_char == "O":
                    sliced = []
                    empty_i = None
                    
                    if direction == "^":
                        sliced = [w_map[i][next_step[1]] for i in range(next_step[0] - 1, -1, -1)]
                        if "." in sliced:
                            wall_before_empty = "#" in sliced[:sliced.index(".")]
                            if not wall_before_empty:
                                empty_i = (next_step[0] - sliced.index(".") - 1, next_step[1])

                    elif direction == "v": 
                        sliced = [w_map[i][next_step[1]] for i in range(next_step[0] + 1, len(w_map))] 
                        if "." in sliced:
                            wall_before_empty = "#" in sliced[:sliced.index(".")]
                            if not wall_before_empty:
                                empty_i = (next_step[0] + sliced.index(".") + 1, next_step[1])

                    elif direction == "<":  
                        sliced = [w_map[next_step[0]][j] for j in range(next_step[1] - 1, -1, -1)]  
                        if "." in sliced:
                            wall_before_empty = "#" in sliced[:sliced.index(".")]
                            if not wall_before_empty:
                                empty_i = (next_step[0], next_step[1] - sliced.index(".") - 1)

                    elif direction == ">":  
                        sliced = [w_map[next_step[0]][j] for j in range(next_step[1] + 1, len(w_map[0]))]  
                        if "." in sliced:
                            wall_before_empty = "#" in sliced[:sliced.index(".")]
                            if not wall_before_empty:
                                empty_i = (next_step[0], next_step[1] + sliced.index(".") + 1)

                    if empty_i:
                        w_map[empty_i[0]][empty_i[1]] = "O"
                        w_map[next_step[0]][next_step[1]] = "@"
                        w_map[cur_loc[0]][cur_loc[1]] = "."
                        cur_loc = next_step

                    
        total = 0
        for x in range(len(w_map)):
            for y in range(len(w_map)):
                if w_map[x][y] == "O":
                    total += (100 * x) + y
                    
        print(total)
                
# Directions lookup
directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

def move(cur_loc, direction, w_map):
    i, j = cur_loc
    di, dj = directions[direction]
    next_i, next_j = i + di, j + dj

# def part1_r(filename):
#     map_in, movements = f.read().split("\n\n");
#     w_map = [list(line) for line in map_in.split("\n")]
#     cur_loc = next((i, j) for i, row in enumerate(w_map) for j, val in enumerate(row) if val == '@')
#     movements = "".join(movements.split("\n"))
#     for direction in movements:   
#         next_step = []
#         if direction == "^":
#             next_step = [cur_loc[0]-1,cur_loc[1]]
#         elif direction == ">":
#             next_step = [cur_loc[0],cur_loc[1]+1]
#         elif direction == "<":
#             next_step = [cur_loc[0],cur_loc[1]-1]
#         elif direction == "v":
#             next_step = [cur_loc[0]+1,cur_loc[1]]

#         if len(next_step) == 0:
#             break
#         if next_step[0] >= len(w_map) or next_step[0] < 0 or next_step[1] >= len(w_map[0]) or next_step[1] < 0:
#             break

#         next_char = w_map[next_step[0]][next_step[1]]
#         if next_char == ".":
#             w_map[next_step[0]][next_step[1]] = "@"
#             w_map[cur_loc[0]][cur_loc[1]] = "."
#             cur_loc = next_step
#         elif next_char == "0":

def convert_map(old_map):
    new_map = []
    for row in old_map:
        new_row = []
        for col in row:
            if col == "#":
                new_row.extend(["#","#"])
            elif col == "O":
                new_row.extend(["[","]"])
            elif col == ".":
                new_row.extend([".","."])
            elif col == "@":
                new_row.extend(["@","."])
        new_map.append(new_row)
    return new_map

def box_can_move(box,direction_vec,w_map):
    pos_1 = (box[0][0]+direction_vec[0],box[0][1]+direction_vec[1])
    pos_2 = (box[1][0]+direction_vec[0],box[1][1]+direction_vec[1])
    print(w_map[pos_1[0]][pos_1[1]],w_map[pos_1[0]][pos_1[1]])
    if w_map[pos_1[0]][pos_1[1]] != "#" and w_map[pos_2[0]][pos_2[1]] != "#":
        print("Box Can move")
        return True
    return False

def move_box(box,direction_vec,w_map):
   
    pos_1 = (box[0][0]+direction_vec[0],box[0][1]+direction_vec[1])
    pos_2 = (box[1][0]+direction_vec[0],box[1][1]+direction_vec[1]) 

    box_1_clone = w_map[box[0][0]][box[0][1]]
    box_2_clone = w_map[box[1][0]][box[1][1]]
    print("Boxndir:",box,direction_vec)
    print("Positions ", pos_1,pos_2)
    print("Clones: ", box_1_clone,box_2_clone)
    
    # w_map[pos_1[0]][pos_1[1]] = w_map[box[0][0]][box[0][1]]
    # w_map[pos_2[0]][pos_2[1]] = w_map[box[1][0]][box[1][1]]
    w_map[box[0][0]][box[0][1]] = "."
    w_map[box[1][0]][box[1][1]] = "."

    w_map[pos_1[0]][pos_1[1]] = box_1_clone
    w_map[pos_2[0]][pos_2[1]] = box_2_clone

    
    print("Move_box_w_map")
    print_matrix(w_map)
def push(location,direction,w_map):
    direction_vec = directions[direction]
    current_character = w_map[location[0]][location[1]]
    box = []
    print("Loc: ",location)
    if current_character == "[":
        box = (location,[location[0],location[1]+1])
    elif current_character == "]":
        box = (location,[location[0],location[1]-1]) 
    print(box)
    if len(box) > 0:
        combined = tuple(a + b for a, b in zip(location, tuple(x * 2 for x in direction_vec)))
        print(direction_vec*2)
        if not box_can_move(box,direction_vec,w_map):
            return False
            
        if not push(combined,direction,w_map):
            return False
        print("Box before move",box)
        move_box(box,direction_vec,w_map);
        
    return True

def part2(filename):
    with open(filename) as f:
        map_in, movements = f.read().split("\n\n");
        old_map = [list(line) for line in map_in.split("\n")]
        w_map = convert_map(old_map)
        
        
        movements = "".join(movements.split("\n"))
        cur_loc = next((i, j) for i, row in enumerate(w_map) for j, val in enumerate(row) if val == '@')
        print_matrix(w_map)
        for direction in movements:
            print()   
            next_step = []
            if direction == "^":
                next_step = [cur_loc[0]-1,cur_loc[1]]
            elif direction == ">":
                next_step = [cur_loc[0],cur_loc[1]+1]
            elif direction == "<":
                next_step = [cur_loc[0],cur_loc[1]-1]
            elif direction == "v":
                next_step = [cur_loc[0]+1,cur_loc[1]]

            if len(next_step) == 0:
                break
            if next_step[0] >= len(w_map) or next_step[0] < 0 or next_step[1] >= len(w_map[0]) or next_step[1] < 0:
                break

            next_char = w_map[next_step[0]][next_step[1]]
            if next_char == ".":
                w_map[next_step[0]][next_step[1]] = "@"
                w_map[cur_loc[0]][cur_loc[1]] = "."
                cur_loc = next_step
            elif next_char in "[]":
                push(next_step,direction,w_map)
                next_char = w_map[next_step[0]][next_step[1]] 
                if next_char == ".":
                    w_map[next_step[0]][next_step[1]] = "@"
                    w_map[cur_loc[0]][cur_loc[1]] = "."
                    cur_loc = next_step 
            print_matrix(w_map)

if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="ex1.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)