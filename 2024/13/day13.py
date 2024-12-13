import argparse
import re
from itertools import combinations
from sympy import symbols, Eq, solve, Integer

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        file_in = [machine.split("\n") for machine in f.read().split("\n\n")];
        machines = []
        for m in file_in:
            machine = {}
            splits = [x.split(" ")for x in m]
            machine["A"] = (int(splits[0][2].replace("X+","").replace(",","")),int(splits[0][3].replace("Y+","")))
            machine["B"] = (int(splits[1][2].replace("X+","").replace(",","")),int(splits[1][3].replace("Y+","")))
            machine["P"] = (int(splits[2][1].replace("X=","").replace(",","")),int(splits[2][2].replace("Y=","")))

            machines.append(machine)
        total = 0
        for machine in machines:
            x, y = symbols('x y', integer=True)

            # Define the equations
            eq1 = Eq(x * machine["A"][0]+ y * machine["B"][0], machine["P"][0])
            eq2 = Eq(x * machine["A"][1] + y * machine["B"][1], machine["P"][1])
            solutions = solve([eq1, eq2], (x, y))
            if solutions:
                total += solutions[x]*3 + solutions[y]*1
                
            print(f"Solutions for x and y: {solutions}")
            print(machine)
        print(total)

def part2(filename):
    with open(filename) as f:
        file_in = [machine.split("\n") for machine in f.read().split("\n\n")];
        machines = []
        for m in file_in:
            machine = {}
            splits = [x.split(" ")for x in m]
            machine["A"] = (int(splits[0][2].replace("X+","").replace(",","")),int(splits[0][3].replace("Y+","")))
            machine["B"] = (int(splits[1][2].replace("X+","").replace(",","")),int(splits[1][3].replace("Y+","")))
            machine["P"] = (int(splits[2][1].replace("X=","").replace(",",""))+10000000000000,int(splits[2][2].replace("Y=",""))+10000000000000)
            machines.append(machine)
        total = 0
        for machine in machines:
            x, y = symbols('x y', integer=True)
            eq1 = Eq(x * machine["A"][0]+ y * machine["B"][0], machine["P"][0])
            eq2 = Eq(x * machine["A"][1] + y * machine["B"][1], machine["P"][1])
            solutions = solve([eq1, eq2], (x, y))
            if solutions:
                total += solutions[x]*3 + solutions[y]*1

            print(f"Solutions for x and y: {solutions}")
            print(machine)
        print(total)

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