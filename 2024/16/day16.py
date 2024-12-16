import argparse
import re
import heapq
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])

args = parser.parse_args();

def reconstruct(cameFrom, curNode):
    #print("Reconstruct")
    pass

def get_neighbours(position,max_h,max_w):
    neighbours = []
    if position[1]-1 >= 0:
        neighbours.append((position[0],position[1]-1,"<"))
    if position[0]-1 >= 0:
       neighbours.append( (position[0]-1,position[1],"^")) 
    if position[0]+1 < max_h:
       neighbours.append((position[0]+1,position[1],"v"))
    if position[1]+1 < max_h:
       neighbours.append((position[0],position[1]+1,">"))    
    return neighbours


def h(start,goal):
    return abs(start[0]-goal[0])+abs(start[1]-goal[1])

def aStar(start, direction, goal, grid):
    openSet = [start]
    closedSet = []
    cameFrom = {}
    heapq.heapify(openSet)

    gScore = {}
    gScore = defaultdict(lambda:float("inf"),gScore)
    gScore[start] = 0

    fScore = {}
    fScore = defaultdict(lambda:float("inf"),fScore)
    fScore[start] = h(start,goal)

    while len(openSet) != 0:
        # Switch to heap
        curNode = heapq.heappop(openSet)
        if curNode == goal:
            print(gScore[goal])
            reconstruct(cameFrom,curNode)
        
        neighbors = get_neighbours(grid,curNode)
        for neighbor in neighbors:
            tentgScore = gScore[curNode]+int(grid[neighbor[0]][neighbor[1]])
            if tentgScore < gScore[neighbor]:
                cameFrom[neighbor] = curNode
                gScore[neighbor] = tentgScore
                fScore[neighbor] = tentgScore + h(neighbor,goal)
                if neighbor not in openSet:
                    heapq.heappush(openSet,neighbor)

def part1(filename):
    with open(filename) as f:
        lines = [list(line) for line in f.read().split("\n")];
        print(lines)

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