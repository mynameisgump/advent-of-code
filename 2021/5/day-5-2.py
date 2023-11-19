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
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)

            # Horizontal and Verticle Lines 
            if x1==x2 or y1==y2:

                points = []
                for x in range(min(x1,x2),max(x1,x2)+1):
                    for y in range(min(y1,y2),max(y1,y2)+1):
                        point = (x,y)
                        if point not in total_points:
                            total_points[point] = 1
                        elif point in total_points:
                            total_points[point] += 1
            else:
                #print()
                #print("Diagonal")
                #print(x1,x2,y1,y2)
                min_x = min(x1,x2)
                max_x = max(x1,x2)
                min_y = min(y1,y2)
                max_y = max(y1,y2)
                #print(min_x)

                x_d = x1-x2
                y_d = y1-y2
                # Bottom-Left to Top-Right line
                if (x_d >= 0 and y_d >= 0) or (x_d < 0 and y_d < 0):
                    for i in range(max_x-min_x+1):
                        x = min_x+i
                        y = min_y+i

                        point = (x,y)
                        if point not in total_points:
                            total_points[point] = 1
                        elif point in total_points:
                            total_points[point] += 1
 
                # Top-Left to Bottom-Right line
                else:
                    for i in range(max_y-min_y+1):
                        x = min_x+i
                        y = max_y-i
                        #print(x,y)
                        point = (x,y)
                        if point not in total_points:
                            total_points[point] = 1
                        elif point in total_points:
                            total_points[point] += 1
                        


                
                
        filtered_points = {k:v for k,v in total_points.items() if v > 1}
        print()
        print("Points:")
        print(len(filtered_points))

        