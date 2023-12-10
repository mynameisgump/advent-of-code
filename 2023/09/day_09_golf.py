import argparse
import re
from functools import partial

def get_predicted(history, reverse):
    done = False
    if reverse:
        history.reverse()
    current = history
    sequences = [history+[0]]
    while done == False:
        diff = [j-i for i, j in zip(current[:-1], current[1:])]
        sequences.append(diff+[0])
        current = diff
        if all(val == 0 for val in diff):
            done = True
    sequences.reverse()
    for i in range(len(sequences)-1):
        seq = sequences[i]
        seq_2 = sequences[i+1]
        last_val_1 = seq[-1]
        last_val_2 = seq_2[-2]
        seq_2[-1] = last_val_2+last_val_1
    return sequences[-1][-1]

if __name__ == "__main__":
    filename = "example1.txt"
    with open(filename) as f:
        histories = [list(map(int, item.split(" "))) for item in f.read().split("\n")];
        part1 = sum(list(map(partial(get_predicted,reverse=False),histories)))
        print("Part 1: ", part1)
        part2 = sum(list(map(partial(get_predicted,reverse=True),histories))) 
        print("Part 2: ", part2)