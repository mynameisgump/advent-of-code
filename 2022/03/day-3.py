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
        for line in lines:
            ruck1, ruck2 = splitstring(line)
            intersection = list(set(ruck1).intersection(ruck2))[0]
            if intersection.islower():
                values.append(string.ascii_lowercase.index(intersection)+1)
            else:
                values.append(string.ascii_lowercase.index(intersection.lower())+1+26)
        print(sum(values))


           
