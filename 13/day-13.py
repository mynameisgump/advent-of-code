
def printPaper(matrix):
    for row in matrix:
        strRow = ""
        for num in row:
            if num == 0:
                strRow += "."
            else:
                strRow +="#"
        print(strRow)
        #print("".join(strRow))

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        dots = []
        maxX = 0
        maxY = 0
        folds = []
        inputFolds = False
        for line in lines:
            if inputFolds:
                folds.append(line.split(" ")[2])
            if line == "":
                inputFolds = True
            if not inputFolds:
                dot = line.split(",")
                dots.append(dot)
                if int(dot[0]) > maxX:
                    maxX = int(dot[0])
                if int(dot[1]) > maxY:
                    maxY = int(dot[1])

        #sprint(folds)
        matrix = [ [ 0 for i in range(maxX+1) ] for j in range(maxY+1) ]

        for dot in dots:
            x = int(dot[0])
            y = int(dot[1])
            matrix[y][x] = 1

        print(maxX)
        print(maxY)
        currentFold = 1
        for fold in folds:
            print("")
            print("Fold "+str(currentFold)+": ")
            currentFold += 1 
            print("Matrix Dimensions:")
            print(len(matrix))
            print(len(matrix[0]))
            
            foldAxis = fold[0]
            
            foldNum = int(fold.split("=")[1])

            if foldAxis == "y":
                
                topHalf = matrix[0:foldNum]
                topHalf = list(reversed(topHalf))
                bottomHalf = matrix[foldNum+1:]

                for y in range(len(bottomHalf)):
                    for x in range(len(bottomHalf[y])):
                        topHalf[y][x] += bottomHalf[y][x]
                        if topHalf[y][x] > 1:
                            topHalf[y][x] = 1

                matrix = list(reversed(topHalf))

            else:
                
                leftHalf = []
                rightHalf = []
                for row in matrix:
                    leftHalf.append(list(reversed(row[:foldNum])))
                    rightHalf.append(row[foldNum+1:])


                for y in range(len(rightHalf)):
                    for x in range(len(rightHalf[y])):
                        leftHalf[y][x] += rightHalf[y][x]
                        if leftHalf[y][x] > 1:
                            leftHalf[y][x] = 1
                leftHalf = [list(reversed(row))for row in leftHalf]
                matrix = leftHalf
            totalDots = sum(map(sum,matrix))

            
            print("Total Dots: "+str(totalDots))
        printPaper(matrix)
        
        #foldY = int(lines[-2].split(" ")[2][2])
        
        #foldX = int(lines[-1].split(" ")[2][2])
        
        #topHalf = matrix[0:foldY]

        #bottomHalf = matrix[foldY+1:]
        #bottomHalf = list(reversed(bottomHalf))
        
 
        #printPaper(matrix)
        #print(maxX)
        #print(maxY)




