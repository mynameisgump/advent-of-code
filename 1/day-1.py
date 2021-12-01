if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]

        increased = 0
        decreased = 0
        previous = None
        for line in lines:
            number = int(line)
            if previous == None:
                previous = number 
            else:
                if number > previous:
                    increased += 1
                    previous = number
                elif number < previous:
                    decreased += 1
                    previous = number
    print("Increased: "+str(increased))
    print("Decreased: "+str(decreased))