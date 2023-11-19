with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def calc_trees(input_file,y_step,x_step):
    trees = 0
    x = 0
    y = 0
    height = len(input_file)
    width = len(input_file[0])
    while y < height:
        char = input_file[y][x]
        if char == "#":
            trees += 1
        x += x_step
        y += y_step
        if x >= width:
            x -= width
    return trees

total_trees = calc_trees(lines,1,1) * calc_trees(lines,1,3) * calc_trees(lines,1,5) * calc_trees(lines,1,7) * calc_trees(lines,2,1)

print(total_trees)
