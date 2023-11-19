import math 
if __name__ == '__main__':
    lineList = [line.rstrip('\n') for line in open("input.txt")]
    function = lambda x: (math.floor(int(x)/3)-2)
    print(sum(list(map(function, lineList))))
        
