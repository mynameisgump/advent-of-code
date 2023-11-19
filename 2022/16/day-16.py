filename="input.txt"
with open(filename) as f:
    lines = [line.rstrip().split(";") for line in f.readlines()]
    for i in range(len(lines)):
        line = lines[i]
        lines[i][0] = [line[0][:8][-2:],int(line[0].split("=")[1])]
        lines[i][1] = line[1].replace(" tunnels lead to valves ","").replace(" tunnel leads to valve ","").split(", ")

get_flow = {}
get_connections = {}
for line in lines:
    get_flow[line[0][0]] = line[0][1]
    get_connections[line[0][0]] = line[1]
    print(line)
non_zero = {k:v for k,v in get_flow.items() if v != 0}
total_valves = len(non_zero.keys())

def highest_pressure(valve,best,opened,total,minutes,total_valves,cur_path,get_flow,get_connections):
    cur_path.append(valve)
    if minutes <= 0:
        return total

    if len(opened) == total_valves:
        while minutes > 0:
            for open_valve in opened:
                open_flow = get_flow[open_valve]
                total += open_flow
            minutes -= 1
        return total

    actions = ["MOVE","OPEN"]
    flow = get_flow[valve]
    children = get_connections[valve]
    if flow == 0 or valve in opened:
        actions = ["MOVE"]
    for open_valve in opened:
        open_flow = get_flow[open_valve]
        total += open_flow
    # print()
    # print("Starting Child Loop:")
    for child_valve in children:
        for action in actions:
            child_total = 0
            if action == "MOVE":
                child_total = highest_pressure(child_valve,best,opened.copy(),total,minutes-1,total_valves,cur_path.copy(),get_flow,get_connections)
            elif action == "OPEN":
                if valve not in opened:
                    opened.append(valve)
                    child_total = highest_pressure(valve,best,opened.copy(),total,minutes-1,total_valves,cur_path.copy(),get_flow,get_connections)
            if child_total > best:
                best = child_total
    return best
#best = 0 
best = highest_pressure("AA",0,[],0,30,total_valves,[],get_flow,get_connections)
print(best)