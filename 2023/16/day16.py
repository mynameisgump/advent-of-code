import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();


# Have a queue of laser objects:
# Position, next position or dir
def print_matrix(matrix):
    print()
    for row in matrix:
        print("".join(row))
# R,L,U,D
def part1(filename):
    with open(filename) as f:
        laser_map = [[*row] for row in f.read().split("\n")];
        initial_char = laser_map[0][0];
        lasers = [((0,-1),"R")]
        print_matrix(laser_map)
        laser_map_dup =  [x[:] for x in laser_map]
        seen_lasers = set()
        init_flag = False
        while len(lasers) > 0 :
            laser = lasers.pop()
            print(laser)
            cur_pos = laser[0]
            direction = laser[1]
            if init_flag:
                laser_map_dup[cur_pos[0]][cur_pos[1]] = "#"
            init_flag = True
            #char = laser_map[laser[1][0]][laser[1][1]]
            next_pos = ()
            match direction:
                case "R":
                    next_pos = (cur_pos[0],cur_pos[1]+1)
                case "L":
                    next_pos = (cur_pos[0],cur_pos[1]-1)
                case "U":
                    next_pos = (cur_pos[0]-1,cur_pos[1])
                case "D":
                    next_pos = (cur_pos[0]+1,cur_pos[1])
            
            if next_pos[0] >= 0 and next_pos[0] < len(laser_map) and next_pos[1] >= 0 and next_pos[1] < len(laser_map[0]) and laser not in seen_lasers:
                char = laser_map[next_pos[0]][next_pos[1]]
                #print("Current Char: ",char, next_pos)
                match char:
                    case ".":
                        lasers.append((next_pos,direction))
                    case "|":
                        if direction == "R" or direction == "L":
                            if next_pos[0]-1 >= 0:
                                lasers.append(((next_pos[0],next_pos[1]), "U"))
                            if next_pos[0]+1 < len(laser_map):
                                lasers.append(((next_pos[0],next_pos[1]), "D"))
                        else:
                            lasers.append((next_pos,direction))
                    case "-":
                        if direction == "U" or direction == "D":
                            if next_pos[1]-1 >= 0:
                                lasers.append(((next_pos[0],next_pos[1]), "L"))
                            if next_pos[1]+1 < len(laser_map[0]):
                                lasers.append(((next_pos[0],next_pos[1]), "R"))
                        else:
                            lasers.append((next_pos,direction))
                    case "\\":
                        if direction == "R":
                            lasers.append(((next_pos[0],next_pos[1]), "D"))
                        if direction == "L":
                            #print(":(")
                            lasers.append(((next_pos[0],next_pos[1]), "U"))
                        if direction == "U":
                            lasers.append(((next_pos[0],next_pos[1]), "L"))
                        if direction == "D":
                            lasers.append(((next_pos[0],next_pos[1]), "R"))
                    case "/":
                        if direction == "R":
                            lasers.append(((next_pos[0],next_pos[1]), "U"))
                        if direction == "L":
                            lasers.append(((next_pos[0],next_pos[1]), "D"))
                        if direction == "U":
                            lasers.append(((next_pos[0],next_pos[1]), "R"))
                        if direction == "D":
                            lasers.append(((next_pos[0],next_pos[1]), "L"))
                #if char == '.':
                #    lasers.append((laser[1][1]))
                #print(char)
                #print("Current Lasers: ",lasers)
            seen_lasers.add(laser)

            #print_matrix(laser_map_dup)7308 :(
        print("")
    map_string = ""
    for row in laser_map_dup:
        map_string += "".join(row)
    print(map_string.count("#"))
    print_matrix(laser_map_dup)


def part2(filename):
    with open(filename) as f:
        laser_map = [[*row] for row in f.read().split("\n")];
        laser_map_dup =  [x[:] for x in laser_map]
        totals = set()
        # Left Column
        for i in range(len(laser_map)):
            laser_map_dup =  [x[:] for x in laser_map]
            lasers = [((i,-1),"R")]
            seen_lasers = set()
            init_flag = False
            while len(lasers) > 0 :
                laser = lasers.pop()
                # print(laser)
                cur_pos = laser[0]
                direction = laser[1]
                if init_flag:
                    laser_map_dup[cur_pos[0]][cur_pos[1]] = "#"
                init_flag = True
                #char = laser_map[laser[1][0]][laser[1][1]]
                next_pos = ()
                match direction:
                    case "R":
                        next_pos = (cur_pos[0],cur_pos[1]+1)
                    case "L":
                        next_pos = (cur_pos[0],cur_pos[1]-1)
                    case "U":
                        next_pos = (cur_pos[0]-1,cur_pos[1])
                    case "D":
                        next_pos = (cur_pos[0]+1,cur_pos[1])
                
                if next_pos[0] >= 0 and next_pos[0] < len(laser_map) and next_pos[1] >= 0 and next_pos[1] < len(laser_map[0]) and laser not in seen_lasers:
                    char = laser_map[next_pos[0]][next_pos[1]]
                    #print("Current Char: ",char, next_pos)
                    match char:
                        case ".":
                            lasers.append((next_pos,direction))
                        case "|":
                            if direction == "R" or direction == "L":
                                if next_pos[0]-1 >= 0:
                                    lasers.append(((next_pos[0],next_pos[1]), "U"))
                                if next_pos[0]+1 < len(laser_map):
                                    lasers.append(((next_pos[0],next_pos[1]), "D"))
                            else:
                                lasers.append((next_pos,direction))
                        case "-":
                            if direction == "U" or direction == "D":
                                if next_pos[1]-1 >= 0:
                                    lasers.append(((next_pos[0],next_pos[1]), "L"))
                                if next_pos[1]+1 < len(laser_map[0]):
                                    lasers.append(((next_pos[0],next_pos[1]), "R"))
                            else:
                                lasers.append((next_pos,direction))
                        case "\\":
                            if direction == "R":
                                lasers.append(((next_pos[0],next_pos[1]), "D"))
                            if direction == "L":
                                #print(":(")
                                lasers.append(((next_pos[0],next_pos[1]), "U"))
                            if direction == "U":
                                lasers.append(((next_pos[0],next_pos[1]), "L"))
                            if direction == "D":
                                lasers.append(((next_pos[0],next_pos[1]), "R"))
                        case "/":
                            if direction == "R":
                                lasers.append(((next_pos[0],next_pos[1]), "U"))
                            if direction == "L":
                                lasers.append(((next_pos[0],next_pos[1]), "D"))
                            if direction == "U":
                                lasers.append(((next_pos[0],next_pos[1]), "R"))
                            if direction == "D":
                                lasers.append(((next_pos[0],next_pos[1]), "L"))
                    #if char == '.':
                    #    lasers.append((laser[1][1]))
                    #print(char)
                    #print("Current Lasers: ",lasers)
                seen_lasers.add(laser)

                #print_matrix(laser_map_dup)7308 :(
            #print("")
            map_string = ""
            for row in laser_map_dup:
                map_string += "".join(row)
            totals.add(map_string.count("#"))
        # Top Column
        for i in range(len(laser_map[0])):
            laser_map_dup =  [x[:] for x in laser_map]
            lasers = [((-1,i),"D")]
            seen_lasers = set()
            init_flag = False
            while len(lasers) > 0 :
                laser = lasers.pop()
                # print(laser)
                cur_pos = laser[0]
                direction = laser[1]
                if init_flag:
                    laser_map_dup[cur_pos[0]][cur_pos[1]] = "#"
                init_flag = True
                #char = laser_map[laser[1][0]][laser[1][1]]
                next_pos = ()
                match direction:
                    case "R":
                        next_pos = (cur_pos[0],cur_pos[1]+1)
                    case "L":
                        next_pos = (cur_pos[0],cur_pos[1]-1)
                    case "U":
                        next_pos = (cur_pos[0]-1,cur_pos[1])
                    case "D":
                        next_pos = (cur_pos[0]+1,cur_pos[1])
                
                if next_pos[0] >= 0 and next_pos[0] < len(laser_map) and next_pos[1] >= 0 and next_pos[1] < len(laser_map[0]) and laser not in seen_lasers:
                    char = laser_map[next_pos[0]][next_pos[1]]
                    #print("Current Char: ",char, next_pos)
                    match char:
                        case ".":
                            lasers.append((next_pos,direction))
                        case "|":
                            if direction == "R" or direction == "L":
                                if next_pos[0]-1 >= 0:
                                    lasers.append(((next_pos[0],next_pos[1]), "U"))
                                if next_pos[0]+1 < len(laser_map):
                                    lasers.append(((next_pos[0],next_pos[1]), "D"))
                            else:
                                lasers.append((next_pos,direction))
                        case "-":
                            if direction == "U" or direction == "D":
                                if next_pos[1]-1 >= 0:
                                    lasers.append(((next_pos[0],next_pos[1]), "L"))
                                if next_pos[1]+1 < len(laser_map[0]):
                                    lasers.append(((next_pos[0],next_pos[1]), "R"))
                            else:
                                lasers.append((next_pos,direction))
                        case "\\":
                            if direction == "R":
                                lasers.append(((next_pos[0],next_pos[1]), "D"))
                            if direction == "L":
                                #print(":(")
                                lasers.append(((next_pos[0],next_pos[1]), "U"))
                            if direction == "U":
                                lasers.append(((next_pos[0],next_pos[1]), "L"))
                            if direction == "D":
                                lasers.append(((next_pos[0],next_pos[1]), "R"))
                        case "/":
                            if direction == "R":
                                lasers.append(((next_pos[0],next_pos[1]), "U"))
                            if direction == "L":
                                lasers.append(((next_pos[0],next_pos[1]), "D"))
                            if direction == "U":
                                lasers.append(((next_pos[0],next_pos[1]), "R"))
                            if direction == "D":
                                lasers.append(((next_pos[0],next_pos[1]), "L"))

                seen_lasers.add(laser)
            map_string = ""
            for row in laser_map_dup:
                map_string += "".join(row)
            totals.add(map_string.count("#"))
        # Right Column
        for i in range(len(laser_map)):
            laser_map_dup =  [x[:] for x in laser_map]
            lasers = [((i,len(laser_map[0])),"L")]
            seen_lasers = set()
            init_flag = False
            while len(lasers) > 0 :
                laser = lasers.pop()
                # print(laser)
                cur_pos = laser[0]
                direction = laser[1]
                if init_flag:
                    laser_map_dup[cur_pos[0]][cur_pos[1]] = "#"
                init_flag = True
                #char = laser_map[laser[1][0]][laser[1][1]]
                next_pos = ()
                match direction:
                    case "R":
                        next_pos = (cur_pos[0],cur_pos[1]+1)
                    case "L":
                        next_pos = (cur_pos[0],cur_pos[1]-1)
                    case "U":
                        next_pos = (cur_pos[0]-1,cur_pos[1])
                    case "D":
                        next_pos = (cur_pos[0]+1,cur_pos[1])
                
                if next_pos[0] >= 0 and next_pos[0] < len(laser_map) and next_pos[1] >= 0 and next_pos[1] < len(laser_map[0]) and laser not in seen_lasers:
                    char = laser_map[next_pos[0]][next_pos[1]]
                    #print("Current Char: ",char, next_pos)
                    match char:
                        case ".":
                            lasers.append((next_pos,direction))
                        case "|":
                            if direction == "R" or direction == "L":
                                if next_pos[0]-1 >= 0:
                                    lasers.append(((next_pos[0],next_pos[1]), "U"))
                                if next_pos[0]+1 < len(laser_map):
                                    lasers.append(((next_pos[0],next_pos[1]), "D"))
                            else:
                                lasers.append((next_pos,direction))
                        case "-":
                            if direction == "U" or direction == "D":
                                if next_pos[1]-1 >= 0:
                                    lasers.append(((next_pos[0],next_pos[1]), "L"))
                                if next_pos[1]+1 < len(laser_map[0]):
                                    lasers.append(((next_pos[0],next_pos[1]), "R"))
                            else:
                                lasers.append((next_pos,direction))
                        case "\\":
                            if direction == "R":
                                lasers.append(((next_pos[0],next_pos[1]), "D"))
                            if direction == "L":
                                #print(":(")
                                lasers.append(((next_pos[0],next_pos[1]), "U"))
                            if direction == "U":
                                lasers.append(((next_pos[0],next_pos[1]), "L"))
                            if direction == "D":
                                lasers.append(((next_pos[0],next_pos[1]), "R"))
                        case "/":
                            if direction == "R":
                                lasers.append(((next_pos[0],next_pos[1]), "U"))
                            if direction == "L":
                                lasers.append(((next_pos[0],next_pos[1]), "D"))
                            if direction == "U":
                                lasers.append(((next_pos[0],next_pos[1]), "R"))
                            if direction == "D":
                                lasers.append(((next_pos[0],next_pos[1]), "L"))

                seen_lasers.add(laser)
            map_string = ""
            for row in laser_map_dup:
                map_string += "".join(row)
            totals.add(map_string.count("#")) 
        #Bottom Column
        for i in range(len(laser_map[0])):
            laser_map_dup =  [x[:] for x in laser_map]
            lasers = [((len(laser_map[0]),i),"U")]
            seen_lasers = set()
            init_flag = False
            while len(lasers) > 0 :
                laser = lasers.pop()
                # print(laser)
                cur_pos = laser[0]
                direction = laser[1]
                if init_flag:
                    laser_map_dup[cur_pos[0]][cur_pos[1]] = "#"
                init_flag = True
                #char = laser_map[laser[1][0]][laser[1][1]]
                next_pos = ()
                match direction:
                    case "R":
                        next_pos = (cur_pos[0],cur_pos[1]+1)
                    case "L":
                        next_pos = (cur_pos[0],cur_pos[1]-1)
                    case "U":
                        next_pos = (cur_pos[0]-1,cur_pos[1])
                    case "D":
                        next_pos = (cur_pos[0]+1,cur_pos[1])
                
                if next_pos[0] >= 0 and next_pos[0] < len(laser_map) and next_pos[1] >= 0 and next_pos[1] < len(laser_map[0]) and laser not in seen_lasers:
                    char = laser_map[next_pos[0]][next_pos[1]]
                    #print("Current Char: ",char, next_pos)
                    match char:
                        case ".":
                            lasers.append((next_pos,direction))
                        case "|":
                            if direction == "R" or direction == "L":
                                if next_pos[0]-1 >= 0:
                                    lasers.append(((next_pos[0],next_pos[1]), "U"))
                                if next_pos[0]+1 < len(laser_map):
                                    lasers.append(((next_pos[0],next_pos[1]), "D"))
                            else:
                                lasers.append((next_pos,direction))
                        case "-":
                            if direction == "U" or direction == "D":
                                if next_pos[1]-1 >= 0:
                                    lasers.append(((next_pos[0],next_pos[1]), "L"))
                                if next_pos[1]+1 < len(laser_map[0]):
                                    lasers.append(((next_pos[0],next_pos[1]), "R"))
                            else:
                                lasers.append((next_pos,direction))
                        case "\\":
                            if direction == "R":
                                lasers.append(((next_pos[0],next_pos[1]), "D"))
                            if direction == "L":
                                #print(":(")
                                lasers.append(((next_pos[0],next_pos[1]), "U"))
                            if direction == "U":
                                lasers.append(((next_pos[0],next_pos[1]), "L"))
                            if direction == "D":
                                lasers.append(((next_pos[0],next_pos[1]), "R"))
                        case "/":
                            if direction == "R":
                                lasers.append(((next_pos[0],next_pos[1]), "U"))
                            if direction == "L":
                                lasers.append(((next_pos[0],next_pos[1]), "D"))
                            if direction == "U":
                                lasers.append(((next_pos[0],next_pos[1]), "R"))
                            if direction == "D":
                                lasers.append(((next_pos[0],next_pos[1]), "L"))

                seen_lasers.add(laser)
            map_string = ""
            for row in laser_map_dup:
                map_string += "".join(row)
            totals.add(map_string.count("#"))
        
        print(max(totals))

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