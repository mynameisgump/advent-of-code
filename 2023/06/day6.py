import argparse
import re
from functools import reduce
parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();


# Speed increases by 1 mm per second


def part1(filename):
    with open(filename) as f:
        [time_string, distance_string] = f.read().split("\n")
        times = [int(num) for num in list(filter(None, time_string.split(":")[1].split(" ")))]
        distances = [int(num) for num in list(filter(None, distance_string.split(":")[1].split(" ")))]
        print(times)
        print(distances)

        total_solutions = []
        cur_race = 0 
        while cur_race < len(times):
            print()
            race_solutions = 0
            race_time = times[cur_race]
            race_distance = distances[cur_race]

            boat_distances = []
            for mils in range(race_time+1):
                seconds_held = mils
                time_at_speed = race_time-mils
                boat_distances.append(seconds_held*time_at_speed)
            print("Race Time: ", race_time)
            print("Race Distance: ",race_distance)
            print("Boat distances: ", boat_distances)
            for distance in boat_distances:
                if distance > race_distance:
                    race_solutions += 1
            total_solutions.append(race_solutions)
            cur_race += 1
        print()
        print("Total Solutions: ",total_solutions)
        print(reduce(lambda x, y: x*y, total_solutions))

def part2(filename):
    with open(filename) as f:
        [time_string, distance_string] = f.read().split("\n")
        times = list(filter(None, time_string.split(":")[1].split(" ")))
        distances = list(filter(None, distance_string.split(":")[1].split(" ")))
        
        print(times, distances)
        race_time = int("".join(times))
        race_distance = int("".join(distances))
        print(race_time,race_distance)
        race_solutions = 0

        boat_distances = []
        for mils in range(race_time+1):
            seconds_held = mils
            time_at_speed = race_time-mils
            boat_distances.append(seconds_held*time_at_speed)
        

        for distance in boat_distances:
                if distance > race_distance:
                    race_solutions += 1
        print(race_solutions)
        # print("Race Time: ", race_time)
        # print("Race Distance: ",race_distance)
        # print("Boat distances: ", boat_distances)

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