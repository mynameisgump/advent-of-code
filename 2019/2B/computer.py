if __name__ == "__main__":
    #Before program instructions
    for noun in range(99):
        for verb in range(99):
            codes = [line.rstrip('\n') for line in open("input.txt")][0].split(',')

            codes[1] = noun
            codes[2] = verb

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
            if (int(codes[0]) == 19690720):
                print(codes[0])
                print(noun,verb)

