if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        window1 = []
        window2 = []
        increased = 0
        decreased = 0
        previous = None
        curLine = 0

        window1Index = 0
        window2Index = 1
        for index in range(len(lines)):
            
            if window1Index-1 >= 0 and window1Index+1 < len(lines):
                if window2Index-1 >= 0 and window2Index+1 < len(lines):
                    window1 = int(lines[window1Index-1])+int(lines[window1Index])+int(lines[window1Index+1])
                    window2 = int(lines[window2Index-1])+int(lines[window2Index])+int(lines[window2Index+1])
                    print(window1)
                    print(window2)
                    if window2 > window1:
                        increased +=1
                    elif window2 < window1:
                        decreased +=1

            window1Index += 1
            window2Index += 1            

        
    print("Increased: "+str(increased))
    print("Decreased: "+str(decreased))