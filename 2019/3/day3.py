import numpy as np

if __name__ == "__main__":
    the_file = open("input.txt")
    wires = []
    for line in the_file:
        wires.append(line.split(","))

    all_points = []
    for wire in wires:
        x_val = 0
        y_val = 0
        points = []
        for section in wire:
            if section[0] == "R":
                number = int(section[1:])
                for i in range(x_val,x_val+number+1):
                    points.append([i,y_val])
                x_val += number
            elif section[0] == "L":
                number = int(section[1:])
                for i in range(x_val-1,x_val-number-1,-1):
                    points.append([i,y_val])
                x_val -= number
            elif section[0] == "U":
                number = int(section[1:])
                for i in range(y_val,y_val+number+1):
                    points.append([x_val,i])
                y_val += number
            else:
                number = int(section[1:])
                for i in range(y_val-1,y_val-number-1,-1):
                    points.append([x_val,i])
                y_val -= number
        all_points.append(points)

    wire1_points = all_points[0]
    wire2_points = all_points[1]
    final_points = []
    intersections = [list(x) for x in set(tuple(x) for x in wire1_points).intersection(set(tuple(x) for x in wire2_points))]
    min_dist = 100000000
    for point in intersections:
        dist = abs(point[0])+abs(point[1])
        if ((dist < min_dist) and (dist != 0))  :
            min_dist = dist
    print(min_dist)
