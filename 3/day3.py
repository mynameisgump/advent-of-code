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
                for i in range(x_val,number+1):
                    points.append([i,y_val])
                x_val += number
            elif section[0] == "L":
                number = int(section[1:])
                for i in range(-(number),x_val+1):
                    points.append([i,y_val])
                x_val -= number
            elif section[0] == "U":
                number = int(section[1:])
                for i in range(y_val,number+1):
                    points.append([x_val,i])
                y_val = number
            else:
                number = int(section[1:])
                for i in range(-(number),y_val+1):
                    points.append([x_val,i])
                y_val = number
        all_points.append(points)

    array1 = all_points[0]
    array2 = all_points[1]
    final_points = []
    print(set(array1))
    print(array1&array2)
