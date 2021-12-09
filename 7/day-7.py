def check_position(crabs,position):
    return sum([abs(position-int(crab)) for crab in crabs])

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        
        crabs = lines[0].split(",")

        min_fuel = 1000000000
        for i in range(2000):
            fuel = check_position(crabs,i)
            if fuel < min_fuel:
                min_fuel = fuel

        print("Min Fuel: "+str(min_fuel))
