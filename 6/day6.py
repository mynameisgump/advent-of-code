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
            
            

orbit_dict = defaultdict(list)
for orbit in line_list:
    locations = orbit.split(")")
    orbit_dict[locations[0]].append(locations[1])

print(recursive_orbit("COM",0,orbit_dict))





