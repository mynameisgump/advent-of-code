from collections import defaultdict
line_list = [line.rstrip("\n") for line in open("test.txt")]

orbit_dict = defaultdict(list)
for orbit in line_list:
    locations = orbit.split(")")
    print(locations)
    orbit_dict[locations[0]].append(locations[1])

print(orbit_dict)
