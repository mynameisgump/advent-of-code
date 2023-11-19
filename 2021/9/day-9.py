

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        height_map = list(map(list,lines))

        low_points = []        
        for y in range(len(height_map)):
            row = height_map[y]
            for x in range(len(row)):
                smallest = True
                number = int(row[x])
                compare = []
                
                if x-1 >= 0:
                    compare.append(int(row[x-1]))
                if x+1 < len(row):
                    compare.append(int(row[x+1]))
                if y-1 >= 0:
                    compare.append(int(height_map[y-1][x]))
                if y+1 < len(height_map):
                    compare.append(int(height_map[y+1][x]))

                
                for adj_num in compare:
                    if number >= adj_num:
                        smallest = False
                        break
                
                
                if smallest == True:
                    #print(x,y,compare)
                    low_points.append(number)
                
        print(low_points)
        risk_levels = [num+1 for num in low_points]
        print(risk_levels)
        result = sum(risk_levels)
        print(result)
        #[[num for num in row] for row in self.rows]