import sys
 
sys.setrecursionlimit(10**6)

def check_position(crabs,position):
    return sum([recursive_add(abs(position-int(crab))) for crab in crabs])

def recursive_add(number):
    if number == 0:
        return 0
    else:
        return number+recursive_add(number-1)

if __name__ == "__main__":
    print("Test:")
    print(recursive_add(3))
    
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        
        crabs = lines[0].split(",")

        min_fuel = 1000000000
        for i in range(2000):
            print(i)
            fuel = check_position(crabs,i)
            if fuel < min_fuel:
                min_fuel = fuel

        print("Min Fuel: "+str(min_fuel))
