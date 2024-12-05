import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        lines = [l.split("\n") for l in f.read().split("\n\n")];
        rules = [line.split("|") for line in lines[0]]
        updates = [line.split(",") for line in lines[1]]
        rulebook = {}
        reverse_rulebook = {}
        for rule in rules:
            if rule[0] in rulebook:
                rulebook[rule[0]].append(rule[1])
            else:
                rulebook[rule[0]] = [rule[1]]
            if rule[1] in reverse_rulebook:
                reverse_rulebook[rule[1]].append(rule[0])
            else:
                reverse_rulebook[rule[1]] = [rule[0]]
        print(rulebook)
        total = 0
        for update in updates:
            print()
            print(update)
            valid = True
            for index in range(len(update)):
                value = update[index]
                print("Current Val:", value)
                before = set(update[:index])
                after = set(update[index+1:])
                rule = []
                if value in rulebook:
                    rule = set(rulebook[value])
                
                print("Before Rules: ",rule)
                if not after.issubset(rule):
                    valid = False

            if valid:
                middle_num = int(update[len(update)//2])
                total += middle_num

        print(total)
                #Step 1: Check list forwards for 
          
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