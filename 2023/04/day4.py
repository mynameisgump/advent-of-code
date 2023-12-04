import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    print("Running Part 1:")
    with open(filename) as f:
        lines = f.read().split("\n");
        total_points = 0
        for line in lines:
            print("")
            print("New Card:")
            points = 0
            [winning_numbers, chosen_numbers]= line.split(":")[1].split("|")
            winning_numbers = set((filter(None,winning_numbers.split(" "))))
            chosen_numbers = set(filter(None,chosen_numbers.split(" ")))
            intersections = winning_numbers.intersection((chosen_numbers));
            print(intersections)
            
            if len(intersections):
                for winner in intersections:
                    if points == 0:
                        points = 1;
                    else:
                        points = points * 2;
            print("Winning Points: ",points)
            total_points += points
        print("Final Points: ", total_points)
            #print(winning_numbers)

def part2(filename):
    print("Running Part 1:")
    with open(filename) as f:
        lines = f.read().split("\n");
        total_points = 0
        # {"Card Num": {intersections={1,2,3,4}, score}}
        winning_card = {}
        # Go through each car
        cards = {}
        card_stack = []
        card_totals = {}
        for line in lines:
            #print("")
            #print("New Card:")
            points = 0
            card_number = int(line.split(":")[0].replace("Card ",""))
            #print(card_number)
            [winning_numbers, chosen_numbers]= line.split(":")[1].split("|")
            winning_numbers = set((filter(None,winning_numbers.split(" "))))
            chosen_numbers = set(filter(None,chosen_numbers.split(" ")))
            intersections = winning_numbers.intersection((chosen_numbers));

            #print(intersections)
            
            cards[card_number] = len(intersections)
            card_totals[card_number] = 1;

            if len(intersections) > 0:
                card_stack.append(card_number)

        print("Cards Pass Done")
        print("Cards w Inter: ",cards)
        print("Card Stack: ", card_stack)
        print("Card Total: ", card_totals)
        
        while len(card_stack) > 0:
            card_num = card_stack.pop()
            card_iter = cards[card_num]
            for i in range(card_iter):
                cur_card = i+1+card_num
                card_totals[cur_card] += 1
                card_stack.append(cur_card)
        print(sum(card_totals.values()))



        # Iterating through original cards
        # for key, value in cards.items():
        #     for i in range(value):
        #         i = i+1
        #         print("Card_Val: ",key+i)
        #         print(i)
        #     print(key,value)
        #print(cards)
            #print("Winning Points: ",points)
            #total_points += points
        #print("Final Points: ", total_points)

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