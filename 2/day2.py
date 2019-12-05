if __name__ == "__main__":
    codes = [line.rstrip('\n') for line in open("input.txt")][0].split(',')
    codes[1] = 12
    codes[2] = 2
    pointer = 0
    while (pointer<len(codes)):
        action = int(codes[pointer])
        if(action == 1):
            result,location = (int(codes[int(codes[pointer+1])])+int(codes[int(codes[pointer+2])])),int(codes[pointer+3])
            codes[location] = result
            pointer = pointer + 4
        elif (action == 2):
            result,location = (int(codes[int(codes[pointer+1])])*int(codes[int(codes[pointer+2])])),int(codes[pointer+3])
            codes[location] = result
            pointer = pointer + 4
        elif(action == 99): 
            pointer = len(codes)
    print(codes[0])

