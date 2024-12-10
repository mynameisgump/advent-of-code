import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

# A Hiking trail is any path that starts at height 0, ends at height 9, 
# and always increases by a height of exactly 1 at each step. Hiking 
# trails never include diagonal steps - only up, down, left, or right (from the perspective of the map).

# Start by finding 0:
# go increase

def print_matrix(matrix):
    for row in matrix:
        print("".join(row))

def get_neighbours(position,max_h,max_w):
    neighbours = []
    if position[1]-1 >= 0:
        neighbours.append((position[0],position[1]-1))
    if position[0]-1 >= 0:
       neighbours.append( (position[0]-1,position[1])) 
    if position[0]+1 < max_h:
       neighbours.append((position[0]+1,position[1]))
    if position[1]+1 < max_h:
       neighbours.append((position[0],position[1]+1))    
    return neighbours

def find_trail(position,matrix,path):
    count = 0
    value = int(matrix[position[0]][position[1]])
    if value == 9:
        return path
    neighbours = get_neighbours(position,len(matrix),len(matrix[0]))
    for n in neighbours:
        n_val = int(matrix[n[0]][n[1]])
        if n_val == value+1 and (n[0],n[1]) not in path:
            path.append((n[0],n[1]))
            new_path = find_trail((n[0],n[1]),matrix,path)
            if new_path:
                count += 1
            #print(new_path)
    if count > 0:
        return count
    return False

def part1(filename):
    with open(filename) as f:
        lines = [list(line) for line in f.read().split("\n")];
        max_h = len(lines)
        max_w = len(lines[0])
        print_matrix(lines)
        print()
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                value = lines[x][y]
                
                if value == "0": 
                    print("New Zero: ",([x],[y]))
                    test = find_trail((x,y),lines,[(x,y)])
                    print(test)
                

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
            filename="ex1.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)