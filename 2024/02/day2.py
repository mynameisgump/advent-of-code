import argparse
import operator
import re

parser = argparse.ArgumentParser()
parser.add_argument("s", choices=["p1","p2"])
parser.add_argument("i", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        lines = [line.rstrip().split(" ") for line in f]

        print(lines)
        # Cases:
        # increase greater then 2
        # no increase 

    
        total = 0
        for level_str in lines:
            level = [int(item) for item in level_str]
            print()
            print(level)
            safe = True
            state = "start"
            i = 0;
            while i+1 < len(level):
                change = level[i]-level[i+1]
                print(change)
                if state == "start":
                    if change == 0:
                        # Fail
                        safe = False
                        break
                    elif change > 3 or change < -3:
                        safe = False
                        break
                    elif change > 0:
                        state = "decreasing"
                        print("Decreasing")
                    elif change < 0:
                        state = "increasing"
                        print("Increasing")
                    
                elif state == "decreasing":
                    if change > 3 or change <= 0:
                        safe = False
                        break
                elif state == "increasing":
                    if change < -3 or change >=0:
                        safe = False
                        break
                i += 1
                
            if safe:
                total += 1
        print("Total", total)
        

                #print("Yay")
        pass

def part2(filename):
    with open(filename) as f:
        pass
if __name__ == "__main__":
    input_selection = args.i
    solution_selection = args.s;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="ex1.txt"
        case "ex2":
            filename="ex2.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)