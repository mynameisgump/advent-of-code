if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        
        elves = f.read().replace("\n", " ").split("  ")
        largest = 0 
        for elf in elves:
            food = elf.split(" ")
            print(food)

            food = [int(item) for item in food if item != ""]
            calories = sum(food)

            if calories > largest:
                largest = calories
            
        print(largest)