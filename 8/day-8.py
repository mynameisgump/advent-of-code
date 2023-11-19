if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        number_dict = {}
        for i in range(10):
            number_dict[i] = 0
        for line in lines:
            displays = line.split("|")[1].split(" ")
            displays.remove("")
            # First Pass:
            for number in displays:
                if len(number) == 2:
                    number_dict[1] += 1
                if len(number) == 3:
                    number_dict[7] += 1
                if len(number) == 4:
                    number_dict[4] += 1
                if len(number) == 7:
                    number_dict[8] += 1


            
           
        print(sum(number_dict.values()))