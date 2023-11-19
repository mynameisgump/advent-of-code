with open('input.txt') as f:
    lines = [line.rstrip() for line in f]


valid = 0
for line in lines:
    parts = line.split()
    policy = parts[0].split("-")
    key = parts[1].replace(":","")
    password = parts[2]
    key_total = password.count(key)
    if key_total >= int(policy[0]) and key_total <= int(policy[1]):
        valid += 1

print(valid)
