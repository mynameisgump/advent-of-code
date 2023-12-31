import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1"])
args = parser.parse_args();
# Attempt 1: 1772145894 Too High
# Attempt 2: 1772145754 (Bug was using Sum(diff))
def part1(filename):
    with open(filename) as f:
        lines = [list(map(int, item.split(" "))) for item in f.read().split("\n")];
        total_sum = 0
        for line in lines:
            done = False
            current = line
            sequences = [line+[0]]
            while done == False:
                diff = [j-i for i, j in zip(current[:-1], current[1:])]
                sequences.append(diff+[0])
                current = diff
                if all(val == 0 for val in diff):
                    done = True
            sequences.reverse()
            #print("Sequences:", sequences)
            for i in range(len(sequences)-1):
                seq = sequences[i]
                seq_2 = sequences[i+1]
                last_val_1 = seq[-1]
                last_val_2 = seq_2[-2]
                seq_2[-1] = last_val_2+last_val_1
            #print("seq_result", sequences[-1][-1]) 
            total_sum += sequences[-1][-1]
        print("Total Sum: ",total_sum)
        

def part2(filename):
    with open(filename) as f:
        lines = [list(map(int, item.split(" "))) for item in f.read().split("\n")];
        total_sum = 0
        for line in lines:
            line.reverse()
            done = False
            current = line
            sequences = [line+[0]]
            while done == False:
                diff = [j-i for i, j in zip(current[:-1], current[1:])]
                sequences.append(diff+[0])
                current = diff
                if all(val == 0 for val in diff):
                    done = True
            sequences.reverse()
            #print("Sequences:", sequences)
            for i in range(len(sequences)-1):
                seq = sequences[i]
                seq_2 = sequences[i+1]
                last_val_1 = seq[-1]
                last_val_2 = seq_2[-2]
                seq_2[-1] = last_val_2+last_val_1
            #print("seq_result", sequences[-1][-1]) 
            total_sum += sequences[-1][-1]
        print("Total Sum: ",total_sum)

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