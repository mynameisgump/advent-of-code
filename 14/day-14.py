
        

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        mainString = ""
        transitionDict = {}
        for i in range(len(lines)):
            if i == 0:
                mainString = lines[i]
            elif i > 1:
                transition = lines[i].split(" -> ")
                transitionDict[transition[0]] = transition[1]
        print(transitionDict)

        steps = 40
        curStep = 0
        for step in range(steps):
            print("Step: "+str(curStep))
            finalString = ""
            #stringLen = len(mainString)
            curIndex = 0
            while curIndex+1 < len(mainString):
                substring = mainString[curIndex]+mainString[curIndex+1]
                if substring in transitionDict.keys():
                    finalString += substring[:1]+transitionDict[substring]
                    if curIndex+1 == len(mainString)-1:
                        finalString += substring[1:]
                    curIndex += 1
                else:
                    finalString += substring
            mainString = finalString
            #print(finalString)
        
        print(len(mainString))    
        freqs = {}
        for i in mainString:
            if i in freqs:
                freqs[i] += 1
            else:
                freqs[i] = 1
        print(freqs)
        maxFreq = max(freqs.items(), key=lambda k: k[1])
        minFreq = min(freqs.items(), key=lambda k: k[1])
        print(maxFreq)
        print(minFreq)
        print(maxFreq[1]-minFreq[1])
            #for i in range(stringLen):
            #    substring = 