filename="input-ex.txt"
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

def highest_pressure(valve,best,opened,total,minutes,total_valves,get_flow,get_connections):
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
            if action == "MOVE":
                child_total = highest_pressure(child_valve,best,opened,total,minutes-1,total_valves,get_flow,get_connections)
            elif action == "OPEN":
                if valve not in opened:
                    opened.append(valve)
                child_total = highest_pressure(valve,best,opened,total,minutes-1,total_valves,get_flow,get_connections)
            if child_total > best:
                best = child_total
    return best
#best = 0 
best = highest_pressure("AA",0,[],0,30,total_valves,get_flow,get_connections)
print(best)

# def heur(flowrate,time):
#     return flowrate*time

# #def calc_pressure(scenario):



# move_cost = 1
# open_cost = 1
# steps = {}
# minutes = range(1,30+1)
# scenarios = [[["AA","MOVE"],[]]]
# log = True
# actions = ["MOVE","OPEN"]
# break_at = 2
# counter = 0 


# def find_path(cur_valve,opened_valves,current_best,all_flow,all_connections,cur_minutes,total_pressure):
#     cur_flow = all_flow[cur_valve]
#     cur_connections = all_connections[cur_valve]
#     actions = ["MOVE","OPEN"]
#     pressure = total_pressure
#     opened = opened_valves.clone()
#     if cur_flow == 0:
#         actions = ["MOVE"]
#     if cur_valve in opened_valves:
#         actions = ["MOVE"]
#     # Calc current score 
#     for valve in opened_valves:
#         flow = all_flow[valve]
#         pressure += flow*cur_minutes
    
#     for valv in cur_connections:
#         value = find_path(valv,opened_valves)
#         #connections = all_connections[valv]
#         #for connection in connections:
#         #    value = find_path()
#     if cur_minutes == 0:
#         return pressure

# find_path("AA",[],0,flow_rates,paths,2,0)