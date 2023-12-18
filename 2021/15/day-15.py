from types import MappingProxyType
from typing import final
from collections import defaultdict
import heapq
# (Value, (x,y))

#def h(node):

def reconstruct(cameFrom, curNode):
    #print("Reconstruct")
    pass

def getNeighbors(grid,node):
    neighbors = []
    #print(node)
    x = node[0]
    y = node[1]
    
    if x-1 > 0:
        left = (x-1,y)
        neighbors.append(left)
    if x+1 < len(grid[0]):
        right = (x+1,y)
        neighbors.append(right)
    if y-1 > 0:
        up = (x,y-1)
        neighbors.append(up)
    if y+1 < len(grid):
        down = (x,y+1)
        neighbors.append(down)
    return neighbors

    #print(neighbors)

def h(start,goal):
    return abs(start[0]-goal[0])+abs(start[1]-goal[1])

def aStar(start, goal, grid):
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
        #curNode = openSet.pop()
        curNode = heapq.heappop(openSet)
        #closedSet.append(curNode)
        #print(curNode)
        #print(openSet)
        if curNode == goal:
            print(gScore[goal])
            reconstruct(cameFrom,curNode)
        
        neighbors = getNeighbors(grid,curNode)
        for neighbor in neighbors:
            tentgScore = gScore[curNode]+int(grid[neighbor[0]][neighbor[1]])
            if tentgScore < gScore[neighbor]:
                cameFrom[neighbor] = curNode
                gScore[neighbor] = tentgScore
                fScore[neighbor] = tentgScore + h(neighbor,goal)
                if neighbor not in openSet:
                    heapq.heappush(openSet,neighbor)

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        grid = []
        for line in lines:
            grid.append(list(line))
            #print(list(line))
        maxY = len(grid)-1
        maxX = len(grid[0])-1
        print("Goal:")
        print(maxY,maxX)
        test = aStar((0,0,0),(maxY,maxX),grid)
