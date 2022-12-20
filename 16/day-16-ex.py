filename="input-ex.txt"
with open(filename) as f:
    lines = [line.rstrip().split(";") for line in f.readlines()]
    for i in range(len(lines)):
        line = lines[i]
        lines[i][0] = [line[0][:8][-2:],int(line[0].split("=")[1])]
        lines[i][1] = line[1].replace(" tunnels lead to valves ","").replace(" tunnel leads to valve ","").split(", ")

flow = {}
paths = {}
for line in lines:
    flow[line[0][0]] = line[0][1]
    paths[line[0][0]] = line[1]
    print(line)
print(flow)
print(paths)



def heur(flowrate,time):
    return flowrate*time

#def calc_pressure(scenario):



move_cost = 1
open_cost = 1
steps = {}
minutes = range(1,30+1)
scenarios = [[["AA","MOVE"],[]]]
log = True
actions = ["MOVE","OPEN"]
break_at = 2
counter = 0 
for minute in minutes:
    new_scenarios = []
    if log:
        print(f"== Minute {minute} ==")
    for i in range(len(scenarios)):
        scenario = scenarios[i][0]
        opened = scenarios[i][1]
        #print(scenario)
        #current_valve = scenario[-2]
        current_action = scenario[-1]
        #options = paths[current_valve]
        if current_action == "MOVE":
            current_valve = scenario[-2]
            options = paths[current_valve]
            for option in options:
                for action in actions:
                    alt_scenario = scenario.copy()
                    alt_opened = opened.copy()
                    if action == "OPEN" and option in opened:
                        break
                    elif action == "OPEN" and option not in opened:
                        alt_opened.append(option)
                    alt_scenario.append(option)
                    alt_scenario.append(action)
                    #print("Alt: ",alt_scenario)
                    new_scenarios.append([alt_scenario,alt_opened])
        elif current_action == "OPEN":
            current_valve = scenario[-2]
            alt_scenario = scenario.copy()
            alt_scenario.append(current_valve)
            alt_scenario.append("MOVE")
            new_scenarios.append([alt_scenario,opened])

    #for scenario in new_scenarios:
        #print(scenario)
        #scenario.append()
        #print(scenario, current_valve, options)
    scenarios = new_scenarios

    #if counter > break_at:
        #break

    counter += 1
    if log:
        print()

print(len(scenarios))