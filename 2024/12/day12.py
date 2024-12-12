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

def find_t_corners(coords):
    center = None
    for coord in coords:
        row, col = coord
        row_count = sum(1 for c in coords if c[0] == row)
        col_count = sum(1 for c in coords if c[1] == col)
        if row_count > 1 and col_count > 1:
            center = coord
            break

    if not center:
        raise ValueError("No valid T-shape center found")

    horizontal = [c for c in coords if c[0] == center[0] and c != center]
    vertical = [c for c in coords if c[1] == center[1] and c != center]

    corners = []
    for h in horizontal:
        for v in vertical:
            corner = (v[0], h[1])
            if corner not in coords:
                corners.append(corner)
    
    return corners


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
                    value = garden[x][y]
                    searching = True
                    to_search = [(x,y)]
                    group = set()
                    peri = 0
                    area = 0
                    while searching:
                        if len(to_search) == 0:
                            searching = False
                            break
                        
                        current_item = to_search.pop()
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
                    

def find_missing_corner(coords):
    rows = [coord[0] for coord in coords]
    cols = [coord[1] for coord in coords]
    
    missing_row = [row for row in rows if rows.count(row) == 1][0]
    missing_col = [col for col in cols if cols.count(col) == 1][0]

    return (missing_row, missing_col)

def part2(filename):
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
                    corners = 0
                    while searching:
                        if len(to_search) == 0:
                            searching = False
                            break
                        
                        current_item = to_search.pop()

                        area += 1

                        group.add(current_item)
                        neighbours = get_neighbours(current_item,max_h,max_w)
                        valid_neighbours = 0
                        
                        active_neighbours = []
                        for n in neighbours:
                            if garden[n[0]][n[1]] == value:
                                valid_neighbours += 1
                                active_neighbours.append(n)
                                if (n[0],n[1]) not in visited and (n[0],n[1]) not in to_search:
                                    to_search.append(n)
                        if len(active_neighbours) == 0:
                            corners += 4
                        elif len(active_neighbours) == 1:
                            corners += 2
                        elif len(active_neighbours) == 2:
                            if active_neighbours[0][0] == active_neighbours[1][0] or active_neighbours[0][1] == active_neighbours[1][1]:
                                pass
                            else:
                                missing_corner = find_missing_corner((current_item,active_neighbours[0],active_neighbours[1]))
                                if garden[missing_corner[0]][missing_corner[1]] != value:
                                    corners += 1
                                corners += 1
                        elif len(active_neighbours) == 3:
                            t_corn = find_t_corners((current_item,active_neighbours[0],active_neighbours[1],active_neighbours[2]))
                            if garden[t_corn[0][0]][t_corn[0][1]] != value:
                                    corners += 1
                            if garden[t_corn[1][0]][t_corn[1][1]] != value:
                                    corners += 1
                        elif len(active_neighbours) == 4:
                            diagonals = get_diagonal_neighbours(current_item,max_h,max_w)
                            for diag in diagonals:
                                if garden[diag[0]][diag[1]] != value: 
                                    corners += 1
                        peri += 4-valid_neighbours
                        visited.add((current_item[0],current_item[1])) 
                    print("Corners: ",corners)
                    total += area*corners

        print(total)

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