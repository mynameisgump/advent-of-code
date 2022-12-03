import string

def splitstring(str):
    str1, str2 = str[:len(str)//2], str[len(str)//2:]
    return str1, str2

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        #print(lines)
        values = []
        groups = []
        counter = 0
        currentGroup = []
        for line in lines:
            print(line)
            if counter < 2:
                currentGroup.append(line)
                counter += 1
            else:
                currentGroup.append(line)
                counter = 0
                groups.append(currentGroup)
                currentGroup = []
        
        for group in groups:
            intersection = list(set(group[0]).intersection(group[1]).intersection(group[2]))[0]
            if intersection.islower():
                values.append(string.ascii_lowercase.index(intersection)+1)
            else:
                values.append(string.ascii_lowercase.index(intersection.lower())+1+26)
            

        print(sum(values))
        
