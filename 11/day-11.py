
if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        grid = []
        for line in lines:
            octopi_row = list(map(int,list(line)))
            final_oct = []
            for charge in octopi_row:
                final_oct.append(charge)

            grid.append(final_oct)

        steps = 100
        for row in grid:
            strong = ""
            for octi in row:
                strong += str(octi)
            print(strong)
        print()
        totalFlashes = 0
        for i in range(steps):
            
            #tempGrid = [ [ 0 for i in range(len(grid)) ] for j in range(len(grid)) ]

            explode = False

            # Initial Increment
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                        grid[x][y] = grid[x][y] + 1
                
            explode = True
            while explode:
                explode = False
                for x in range(len(grid)):
                    for y in range(len(grid[x])):
                        if grid[x][y] > 9:
                            explode = True
                            totalFlashes += 1
                            grid[x][y] = 0
                            for x2 in range(x-1,(x+1)+1):
                                for y2 in range(y-1,(y+1)+1):
                                    if x2 >= 0 and x2 < len(grid):
                                        if y2 >= 0 and y2 < len(grid[x2]):
                                            if grid[x2][y2] != 0:
                                                grid[x2][y2] = grid[x2][y2] + 1

           
            #grid = tempGrid
            #for row in grid:
            #    strong = ""
            #    for octi in row:
            #        strong += str(octi)
            #    print(strong)
            #print("\n")
        print(totalFlashes)

                    

                    
                    
                    
