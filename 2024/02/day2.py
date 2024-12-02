import argparse
import operator
import re
from itertools import pairwise


parser = argparse.ArgumentParser()
parser.add_argument("s", choices=["p1","p2"])
parser.add_argument("i", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1_Attempt_1(filename):
    with open(filename) as f:
        lines = [line.rstrip().split(" ") for line in f]
        print(lines)
        total = 0
        for level_str in lines:
            level = [int(item) for item in level_str]
            print()
            print(level)
            safe = True
            state = "start"
            i = 0;
            list_of_changes = []
            while i+1 < len(level):
                change = level[i]-level[i+1]
                print(change)
                list_of_changes.append(change)
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
        pass

def part1(filename):
    with open(filename) as f:
        levels = [[int(item) for item in level] for level in [line.rstrip().split(" ") for line in f]]
        dec_set = set([1,2,3]);
        inc_set = set([-1,-2,-3]);
        total = 0;
        for level in levels:
            diff = [a - b for a, b in pairwise(level)]
            s = set(diff)
            safe = False
            if s <= dec_set:
                safe = True
            elif s <= inc_set:
                safe = True
            if safe:
                total += 1
        print("Total is: ",total)

def part2(filename):
    with open(filename) as f:
        levels = [[int(item) for item in level] for level in [line.rstrip().split(" ") for line in f]]
        dec_set = set([1,2,3]);
        inc_set = set([-1,-2,-3]);
        total = 0;
        for level in levels:
            diff = [a - b for a, b in pairwise(level)]
            s = set(diff)
            safe = False
            if s <= dec_set:
                safe = True
            elif s <= inc_set:
                safe = True
            else:
                combinations = [level[:i] + level[i+1:] for i in range(len(level))]
                for combo in combinations:
                    combo_set = set([a - b for a, b in pairwise(combo)])
                    if combo_set <= dec_set:
                        safe = True
                    elif combo_set <= inc_set:
                        safe = True
            if safe:
                total += 1
        print("Total is: ", total)
        

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