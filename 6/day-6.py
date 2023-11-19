def checkFish(fish):

    if fish == 0:
        return 6
    else:
        return fish-1


if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        fishes = lines[0].split(",")
        fishes = list(map(int,fishes))
        print(fishes)
        days = 256
        current = 0
        
        for day in range(days):
            print("Current Day: "+str(current))
            current += 1

            if current == 1:
                list_of_fish = list(map(checkFish,fishes))

            else:
                zeros = list_of_fish.count(0)
                list_of_fish = list(map(checkFish,list_of_fish))
                #print(list_of_fish.count(0))
                fish_to_add = zeros * [8]
                list_of_fish = list_of_fish + fish_to_add
            #print(list_of_fish)
            
        # 433675 too high
        print(len(list_of_fish))