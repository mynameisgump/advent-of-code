with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

trees = 0
x = 0
y = 0

trees = 0
height = len(lines)
width = len(lines[0])
while y < height:
    char = lines[y][x]
    if char == "#":
        trees += 1
    x += 3
    y += 1
    if x >= width:
        x -= width
print(trees)
