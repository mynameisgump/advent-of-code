from collections import defaultdict
line_list = [line.rstrip("\n") for line in open("input.txt")]

def recursive_orbit(loc,cur_orbit,path):
    if loc not in path:
        return 0
    else:
        next_orbits = path[loc]
        cur_orbit += 1
        total = 0
        for orbit in next_orbits:
            orbit_sum = cur_orbit + recursive_orbit(orbit,cur_orbit,path)
            total += orbit_sum
        return total


paths = []
def DFS(main_path,start,goal,path=[]): 
    path=path+[start] 
    if start==goal:
        paths.append(path) 
    for node in main_path[start]:
        if node not in path:
            DFS(main_path,node,goal,path)


orbit_dict = defaultdict(list)
for orbit in line_list:
    locations = orbit.split(")")
    orbit_dict[locations[0]].append(locations[1])


DFS(orbit_dict,"COM","SAN")
DFS(orbit_dict,"COM","YOU")
san_p = set(paths[0])
you_p = set(paths[1])
print(len(you_p.symmetric_difference(san_p)))





