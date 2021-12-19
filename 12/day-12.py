from dataclasses import dataclass
import copy
@dataclass
class Node:
    name: str
    paths: list

class Cave:
    start: str
    nodes: list

finalPaths = []

def getPathsGood(curNode,nodes,curPath,paths):
    #print()
    #print("Function Called: ")
    #print("CurNode: "+curNode)
    #print("CurPath: "+str(curPath))
    #print("Paths: "+str(paths))
    
    if curNode == "end":
        curPath.append(curNode)
        paths.append(curPath)
        finalPaths.append(curPath)
        return paths

    else:
        curPath.append(curNode)
        tempPaths = []
        for child in nodes[curNode]:
            # Does not go back to start
            if child != "start":
                if child.isupper():
                    tempPaths.append(getPathsGood(child,nodes,copy.deepcopy(curPath),copy.deepcopy(paths)))
                else:
                    if child not in curPath:
                        tempPaths.append(getPathsGood(child,nodes,copy.deepcopy(curPath),copy.deepcopy(paths)))
        paths.append(tempPaths)
        if len(paths) > 0:
            return paths
    

def getPaths(curNode,nodes,curPath,paths):
    curPath.append(curNode)
    #if curNode 
    print(curNode)
    if curNode == "end":
        print(curPath)
        return curPath
    else:
        for child in nodes[curNode]:
            print(curNode+","+child)
            for child2 in nodes[child]:
                
                if child2 != "start":
                    print(curNode+","+child+","+child2)

                    if child2 in nodes.keys() and child2 != "end":

                        for child3 in nodes[child2]:
                            if child3 != "start" and child3:
                                print(curNode+","+child+","+child2+","+child3)



        #if curNode in nodes.keys():
        #    for child in nodes[curNode]:
        #        if child.isupper():
        #            getPaths(curNode,nodes,curPath,paths)
        #        else:
        #            if child not in curPath:
        #                getPaths(curNode,nodes,curPath,paths)
        #else:
        #    return []
    
    #for child in nodes[curNode]:
        #print()
        #print(child)
        #for child2 in nodes[child]:
            #print(child2)
            #print(child2 in nodes.keys())

        #paths = getPaths(child,nodes,curPath,paths)
    #return paths    

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        nodes = {}
        for line in lines:
            path = line.split("-")
            #print(line.split("-"))
            if path[0] not in nodes.keys():
                nodes[path[0]] = []
            #elif path[0] in nodes.keys():
            if path[1] not in nodes.keys():
                nodes[path[1]] = []
            nodes[path[0]].append(path[1])
            nodes[path[1]].append(path[0])

            
        #print(nodes)
        curNode = "start"
        
        paths = getPathsGood(curNode,nodes,[],[])
        #print("")
        #print("Final Paths: ")
        #print(paths)
        #for path in paths:
        #    print(path)
        
        print(len(finalPaths))
       

        