from dataclasses import dataclass
@dataclass
class Octopus:
    charge: int
    tired: False

    def power_up(self):
        if not self.tired:
            self.charge += 1

    def explode(self):
        self.power = 0
        self.tired = True

    def sleep(self):
        self.tired = False

@dataclass
class Octopi:
    grid: [Octopus]

    def valid(self,x,y):
        if x < 0 or y < 0 or x >= len(self.grid[0]) or y >= len(self.grid):
            return False
        else:
            return True 

    def explode(self,x,y):
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if valid(x,y):
                    grid[y][x].charge()

    def reset_oct(self):
        self.grid = [[octopus.sleep() for octopus in row] for row in grid] 

    def check_charges(self):
        for row in grid:
            for octopus in row:
                if octopus.charge > 9:
                    return True

    def step(self):

        for y in range(len(grid)):
            for x in range(len(grid)):
                grid[y][x].power_up()
        fully_charged = check_explosions()
        while fully_charged:
            



    def __str__(self):
        final_str = ""
        for row in grid:
            for octopus in row:
                final_str += str(octopus.charge)+" "
            final_str += "\n"
        return final_str
    
    def print_tired(self):
        final_str = ""
        for row in grid:
            for octopus in row:
                if octopus.tired == False:
                    final_str += "F "
                else:
                    final_str += "T "
            final_str += "\n"
        print(final_str)
        


    

def get_adj(x,y,min_val,max_val):
    adj = []
    for x_2 in range(-1,2):
        for y_2 in range(-1,2):
            if valid(x+x_2,y+y_2):
                adj.append((x+x_2,y+y_2))



if __name__ == "__main__":
    filename="ex-input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        grid = []
        for line in lines:
            octopi_row = list(map(int,list(line)))
            final_oct = []
            for charge in octopi_row:
                octopus = Octopus(charge,False)
                final_oct.append(octopus)
            #print(final_oct)
            grid.append(final_oct)
        #print(grid)
        octopi = Octopi(grid)

            
        # Initial
        steps = 3
        for step in range(steps):
            print("Step: "+str(step))
            print(octopi)
            octopi.print_tired()
        
            octopi.step()

        