import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();


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
def get_diagonal_neighbours(position,max_h,max_w):
    neighbours = []
    if position[1]-1 >= 0 and position[0]-1 >= 0:
        neighbours.append((position[0]-1,position[1]-1))
    if position[0]-1 >= 0 and position[1]+1 < max_w:
        neighbours.append((position[0]-1,position[1]+1))
    if position[0]+1 < max_h and position[1]-1 >= 0:
        neighbours.append((position[0]+1,position[1]-1))
    if position[0]+1 < max_h and position[1]+1 < max_w:
        neighbours.append((position[0]+1,position[1]+1))
    return neighbours

def part1(filename):
    with open(filename) as f:
        garden = [list(item) for item in f.read().split("\n")];
        max_h = len(garden)
        max_w = len(garden)
        selected = None
        visited = set()
        total = 0 
        for x in range(len(garden)):
            for y in range(len(garden[x])):
                if (x,y) in visited:
                    pass
                else:
                    print()
                    value = garden[x][y]
                    searching = True
                    to_search = [(x,y)]
                    group = set()
                    peri = 0
                    area = 0
                    # print(to_search)
                    while searching:
                        if len(to_search) == 0:
                            searching = False
                            break
                        
                        current_item = to_search.pop()
                        # print(current_item)
                        area += 1

                        group.add(current_item)
                        neighbours = get_neighbours(current_item,max_h,max_w)
                        valid_neighbours = 0
                        for n in neighbours:
                            if garden[n[0]][n[1]] == value:
                                valid_neighbours += 1
                                if (n[0],n[1]) not in visited and (n[0],n[1]) not in to_search:
                                    to_search.append(n)
                        peri += 4-valid_neighbours
                        visited.add((current_item[0],current_item[1])) 

                    total += area*peri

        print(total)
                    



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