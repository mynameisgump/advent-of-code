with open('input.txt') as f:
    lines = [line.rstrip() for line in f]


valid = 0
for line in lines:
    parts = line.split()
    policy = parts[0].split("-")
    key = parts[1].replace(":","")
    password = parts[2]
    pos1 = int(policy[0])-1
    pos2 = int(policy[1])-1
    if (password[pos1] == key) ^ (password[pos2] == key):
        valid += 1

print(valid)
