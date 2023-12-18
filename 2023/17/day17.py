import argparse
import heapq

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def reconstruct_path(came_from, current):
    print(current)
    total_path = [current]
    while current in came_from:
        current = came_from[current][0]
        total_path.append(current)
    return total_path


def get_neighbors(node,lava_map):
    [position, direction] = node
    positions = []
    if position[0]-1 > 0:
        positions.append(((position[0]-1,position[1]),"U"))
    if position[0]+1 < len(lava_map):
        positions.append(((position[0]+1,position[1]),"D"))
    if position[1]-1 > 0:
        positions.append(((position[0],position[1]-1),"L"))
    if position[1]+1 < len(lava_map):
        positions.append(((position[0],position[1]+1),"R"))
    return positions

def h(node_1,came_from):
    if len(came_from) > 3:
        dir_1 = node_1[1]
        node_2 = came_from[node_1[0]]
        dir_2 = node_2[1]
        node_3 = came_from[node_2[0]]
        dir_3 = node_3[1]
        if dir_1 == dir_2 == dir_3:
            return float('inf')
    return 0

def astar(start,stop,lava_map):
    print()
    all_nodes = []
    came_from = {}
    g_score = {}
    f_score = {}
    for y in range(len(lava_map)):
        for x in range(len(lava_map[0])):
            all_nodes.append((y,x))
            g_score[(y,x)] = float('inf')
            f_score[(y,x)] = float('inf')
    g_score[start] = 0
    f_score[start] = lava_map[0][0]
    open_nodes = []
    heapq.heappush(open_nodes,(f_score[start],start))
    

    cur_it = 0
    while len(open_nodes) > 0:
    #while cur_it < 5:
        [score, current] = heapq.heappop(open_nodes)
        print(open_nodes)
        if current == stop:
            return reconstruct_path(came_from, current)
        neighbors = get_neighbors((current,"S"),lava_map)

        for neighbor,direction in neighbors:
            tentative_gScore = g_score[current] + lava_map[neighbor[0]][neighbor[1]]
            #print(tentative_gScore)
            if tentative_gScore < g_score[neighbor]:
                #print("Addin")
                came_from[neighbor] = (current,direction)
                g_score[neighbor] = tentative_gScore
                f_score[neighbor] = tentative_gScore + h((neighbor,direction),came_from)
                if neighbor not in open_nodes:
                    heapq.heappush(open_nodes,(f_score[neighbor],neighbor))
        cur_it += 1
    # float inf
    
    # prev = {}
    # g_score[start] = 0 
    # f_score[start] = lava_map[0][0]
    # openSet = set((f_score[start],start))

    # while len(openSet) > 1:
    #     current = 
    # pass

def part1(filename):
    with open(filename) as f:

        lava_map = [[int(item2) for item2 in [*item]] for item in f.read().split("\n")];
        
        for row in lava_map:
            print("".join(str(num) for num in row))

        path = astar((0,0),(len(lava_map)-1,len(lava_map[0])-1),lava_map)
        for node in path:
            lava_map[node[0]][node[1]] = "#"
        for row in lava_map:
            print("".join(str(num) for num in row))
        #print(lava_map)

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
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)