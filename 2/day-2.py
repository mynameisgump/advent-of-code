if __name__ == "__main__":
    filename="input.txt"

    rpcDict = {"X": 1,"Y": 2, "Z": 3}
    scoreDict = {
        "AX": 3,
        "BX": 0,
        "CX": 6,
        "AY": 6,
        "BY": 3,
        "CY": 0,
        "AZ": 0,
        "BZ": 6,
        "CZ": 3,
    }

    winDict = {
        "AX": "Z",
        "BX": "X",
        "CX": "Y",
        "AY": "X",
        "BY": "Y",
        "CY": "Z",
        "AZ": "X",
        "BZ": "Z",
        "CZ": "X",
    }


    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        gameScore = 0
        for line in lines:
            game = line.split(" ")
            gameScore += rpcDict[game[1]]+gameDict[game[0]+game[1]]
        print(gameScore)