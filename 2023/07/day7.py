import argparse
import re
from functools import cmp_to_key
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

card_strength = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}
card_strength_p2 = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14
}


def judge_hand(hand):
    card_vals = {}
    for card in hand:
        card_vals[card] = card_vals.get(card, 0) + 1
    
    if sorted(card_vals.values()) == [5]:
        return 6
    if sorted(card_vals.values()) == [1,4]:
        return 5
    if sorted(card_vals.values()) == [2,3]:
        return 4
    if sorted(card_vals.values()) == [1,1,3]:
        return 3
    if sorted(card_vals.values()) == [1,2,2]:
        return 2 
    if sorted(card_vals.values()) == [1,1,1,2]:
        return 1 
    if sorted(card_vals.values()) == [1,1,1,1,1]:
        return 0
    print(card_vals)


    
def sort_hand(hand_1, hand_2):
    hand_1_type = judge_hand(hand_1)
    hand_2_type = judge_hand(hand_2)
    if hand_1_type > hand_2_type:
        return 1
    elif hand_2_type > hand_1_type:
        return -1
    elif hand_1_type == hand_2_type:
        for i in range(len(hand_1)):
            char_1 = card_strength[hand_1[i]]
            char_2 = card_strength[hand_2[i]]
            if char_1 > char_2:
                return 1
            if char_2 > char_1: 
                return -1
        return 0

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n");
        hands = [line.split(" ")[0] for line in lines]
        bids = [int(line.split(" ")[1]) for line in lines]
        players = dict(map(lambda i,j : (i,j) , hands,bids))

        sorted_winners = sorted(hands, key=cmp_to_key(sort_hand))
        final_sum = 0
        for i in range(len(sorted_winners)):
            bid = players[sorted_winners[i]] * (i+1)
            final_sum += bid
        print("Sum: ", final_sum)

def judge_hand_p2(hand):
    card_vals = {}
    for card in hand:
        card_vals[card] = card_vals.get(card, 0) + 1
    
    # Five Kind
    # Four Kind 
    # Full house
    # Three Kind
    # Two Pair
    # One Pair 
    # High Card
    if "J" not in card_vals.keys():
        if sorted(card_vals.values()) == [5]:
            return 6
        if sorted(card_vals.values()) == [1,4]:
            return 5
        if sorted(card_vals.values()) == [2,3]:
            return 4
        if sorted(card_vals.values()) == [1,1,3]:
            return 3
        if sorted(card_vals.values()) == [1,2,2]:
            return 2 
        if sorted(card_vals.values()) == [1,1,1,2]:
            return 1 
        if sorted(card_vals.values()) == [1,1,1,1,1]:
            return 0
        print(card_vals)
    else:
        total_jokers = card_vals.pop("J")
        max_val = max(card_vals, key=card_vals.get)
        card_vals

        # Five Kind
        # if sorted(card_vals.values()) == [5]:
        #     return 6
        # if sorted(card_vals.values()) == [4]:
        #     return 6
        # if sorted(card_vals)
        
        # Four Kind



        # print("Judging hand w/ J: ", hand)
        # 
        # print(sorted(card_vals.values()))
        # 1 joker
        # if sorted(card_vals.values()) == [4]:
        #     return 6
        # if sorted(card_vals.values()) == [1,3]:
        #     return 5
        # if sorted(card_vals.values()) == [2,2]:
        #     return 4
        # if sorted(card_vals.values()) == [1,1,2]:
        #     return 3
        # if sorted(card_vals.values()) == [1,1,1,1]:
        #     return 1
        # 2 joker
        # if sorted(card_vals.values()) == [1,2]:
        #     return 4
        # if sorted(card_vals.values()) == [2,2]:
        #     return 4
        # if sorted(card_vals.values()) == [2,2]:
        #     return 4
        
            


        print(total_jokers)
    return 0

def sort_hand_p2(hand_1, hand_2):
    hand_1_type = judge_hand_p2(hand_1)
    hand_2_type = judge_hand_p2(hand_2)
    if hand_1_type > hand_2_type:
        return 1
    elif hand_2_type > hand_1_type:
        return -1
    elif hand_1_type == hand_2_type:
        for i in range(len(hand_1)):
            char_1 = card_strength[hand_1[i]]
            char_2 = card_strength[hand_2[i]]
            if char_1 > char_2:
                return 1
            if char_2 > char_1: 
                return -1
        return 0



def part2(filename):
    with open(filename) as f:
        lines = f.read().split("\n");
        hands = [line.split(" ")[0] for line in lines]
        bids = [int(line.split(" ")[1]) for line in lines]
        players = dict(map(lambda i,j : (i,j) , hands,bids))

        sorted_winners = sorted(hands, key=cmp_to_key(sort_hand_p2))
        final_sum = 0
        for i in range(len(sorted_winners)):
            bid = players[sorted_winners[i]] * (i+1)
            final_sum += bid
        print("Sum: ", final_sum)

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