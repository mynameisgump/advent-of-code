import argparse
import re
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

max_red = 12
max_green = 13
max_blue = 14

def part1(filename):
    with open(filename) as f:
        games = f.read().split("\n");
        possible_games = 0;
        total_valid_games = 0;
        for game in games:
            valid_game = True
            split = game.split(":")
            game_id = int(split[0].replace("Game ", ""))
            draws = re.split("; |,", split[1])
            draws = [item.strip() for item in draws]
            for draw in draws:
                print("Chosen Draw:",draw)
                if "red" in draw:
                    total = int(draw.replace(" red", ""))
                    if total > max_red:
                        valid_game = False
                elif "blue" in draw:
                    total = int(draw.replace(" blue", ""))
                    if total > max_blue:
                        valid_game = False
                elif "green" in draw:
                    total = int(draw.replace(" green", ""))
                    if total > max_green:
                        valid_game = False
            
            if valid_game:
                total_valid_games += game_id
        print("Final Answer: ",total_valid_games)

def part2(filename):
    with open(filename) as f:
        games = f.read().split("\n");
        possible_games = 0;
        powers_sum = 0 
        for game in games:
            valid_game = True
            split = game.split(":")
            game_id = int(split[0].replace("Game ", ""))
            draws = re.split("; |,", split[1])
            draws = [item.strip() for item in draws]
            game_max_red = 0
            game_max_blue = 0
            game_max_green = 0
            for draw in draws:
                if "red" in draw:
                    total = int(draw.replace(" red", ""))
                    if total > game_max_red:
                        game_max_red = total
                elif "blue" in draw:
                    total = int(draw.replace(" blue", ""))
                    if total > game_max_blue:
                        game_max_blue = total
                elif "green" in draw:
                    total = int(draw.replace(" green", ""))
                    if total > game_max_green:
                        game_max_green = total
            
            powers_sum += game_max_red*game_max_green*game_max_blue;
            print(f'Power of Game {game_id}: {game_max_red*game_max_green*game_max_blue}')
        print("Powers Sum: ",powers_sum)
        


if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="example1.txt"
        case "ex2":
            filename="example2.txt"
    match solution_selection:
        case "p1":
            part1(filename)
        case "p2":
            part2(filename)