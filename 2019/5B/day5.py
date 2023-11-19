if __name__ == "__main__":
    file_name = input("What is the input file? ")
    codes = [line.rstrip('\n') for line in open(file_name)][0].split(',')
    #codes[1] = 12
    #codes[2] = 2
    pointer = 0
    while (pointer<len(codes)):
        action = str(codes[pointer]).zfill(5)
        op = action[-2:]
        var4_codes = ["01","02","07","08"]
        var3_codes = ["05","06"]
        var2_codes = ["03","04"]
        var_codes = ["99"]
        '''
        print(action)
        print(codes)
        print(pointer)
        input()
        '''
        if (op in var4_codes):
            if (action[-3] == "0"):
                adr1 = int(codes[pointer+1])
                val1 = int(codes[adr1])
            if (action[-3] == "1"):
                val1 = int(codes[pointer+1])

            if (action[-4] == "0"):
                adr2 = int(codes[pointer+2])    
                val2 = int(codes[adr2])
            if (action[-4] == "1"):
                val2 = int(codes[pointer+2])
            
            dest = int(codes[pointer+3])


        if (op in var3_codes):
            if (action[-3] == "0"):
                adr1 = int(codes[pointer+1])
                val1 = int(codes[adr1])
            if (action[-3] == "1"):
                val1 = int(codes[pointer+1])
            
            if (action[-4] == "0"):
                adr2 = int(codes[pointer+2])
                dest = int(codes[adr2])
            if (action[-4] == "1"):
                dest = int(codes[pointer+2])

        if (op == "01"):
            result = val1+val2
            codes[dest] = result
            pointer += 4

        elif (op == "02"):
            result = val1*val2
            codes[dest] = result
            pointer += 4

        elif (op == "03"):
            val = input("USER INPUT REQUIRED: ")
            dest = int(codes[pointer+1])
            codes[dest] = str(val)
            pointer += 2

        elif (op == "04"):
            loc = int(codes[pointer+1])
            var_out = codes[loc]
            print("OUTPUT:"+str(var_out))
            pointer += 2

        elif (op == "05"):
            if (val1 != 0):
                pointer = dest
            else:
                pointer += 3

        elif (op == "06"):
            if (val1 == 0):
                pointer = dest
            else:
                pointer += 3

        elif (op == "07"):
            if (val1 < val2):
                codes[dest] = 1
            else:
                codes[dest] = 0
            pointer += 4

        elif (op == "08"):
            if (val1 == val2):
                codes[dest] = 1
            else:
                codes[dest] = 0
            pointer += 4

        elif(op == "99"): 
            pointer = len(codes)

