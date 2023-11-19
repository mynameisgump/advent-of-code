from dataclasses import dataclass

@dataclass 
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]

        #point_pairs = []
        total_points = {}
        for line in lines:
            line = line.split(" -> ")
            x1,y1 = line[0].split(",")
            x2,y2 = line[1].split(",")
            
            if x1==x2 or y1==y2:
                print()
                print(x1)
                
                x1 = int(x1)
                x2 = int(x2)
                y1 = int(y1)
                y2 = int(y2)

                points = []
                for x in range(min(x1,x2),max(x1,x2)+1):
                    for y in range(min(y1,y2),max(y1,y2)+1):
                        point = (x,y)
                        if point not in total_points:
                            total_points[point] = 1
                        elif point in total_points:
                            total_points[point] += 1

        filtered_points = {k:v for k,v in total_points.items() if v > 1}
        print(len(filtered_points))

        