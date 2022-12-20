filename="input-ex.txt"
with open(filename) as f:
    lines = [line.rstrip().split(";") for line in f.readlines()]
    for i in range(len(lines)):
        line = lines[i]
        lines[i][0] = [line[0][:8][-2:],int(line[0].split("=")[1])]
        lines[i][1] = line[1].replace(" tunnels lead to valves ","").split(", ")

for line in lines:
    print(line)