if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        
        elves = f.read().replace("\n", " ").split("  ")
        calorieTotals = [] 
        for elf in elves:
            food = elf.split(" ")
            print(food)

            food = [int(item) for item in food if item != ""]
            calories = sum(food)
            calorieTotals.append(calories)

            
        calorieTotals.sort()
        print(calorieTotals)
        print(calorieTotals[-1]+calorieTotals[-2]+calorieTotals[-3])
            
        #print(largest)