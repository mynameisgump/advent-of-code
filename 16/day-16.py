if __name__ == "__main__":
    filename="ex-input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        string = lines[0]
        hexa2bin = {
            '0' : '0000',
            '1' : '0001',
            '2' : '0010',
            '3' : '0011',
            '4' : '0100',
            '5' : '0101',
            '6' : '0110',
            '7' : '0111',
            '8' : '1000',
            '9' : '1001',
            'A' : '1010',
            'B' : '1011',
            'C' : '1100',
            'D' : '1101',
            'E' : '1110',
            'F' : '1111'
        }

        print("Hex String: ",string)
        binaryString = ""
        for char in string:
            #print(ord(char))
            binaryString += hexa2bin[char]
            #binaryString += format(ord(char), 'b')
            #print(format(ord(char), 'b'))
        print("Binary String:",binaryString)

        curIndex = 0
        curParse = "version"
        for char in range(len(binaryString)):
            if curParse == "version":
                version = int(binaryString[curIndex:curIndex+3],2)
                print("Version:",version)
                curIndex += 3 
                curParse = "typeID"
            
            if curParse == "typeID":
                typeID = int(binaryString[curIndex:curIndex+3],2)
                print("Type ID:",typeID)
        
        #version = int(binaryString[:3],2)
        #print("Version: ",version)
        #packageID = int(binaryString[3:6],2)
        #print("Package ID: ",packageID)
