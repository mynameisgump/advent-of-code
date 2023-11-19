with open('input.txt') as f:
    lines = f.read()

passports = lines.split("\n\n")
passports = [x.replace("\n", " ") for x in passports]

essential = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

total_valid = 0
for passport in passports:
    passport = passport.rstrip()
    pairs = dict(x.split(":") for x in passport.split(" "))
    shared = set(essential)&set(pairs.keys())
    if len(shared) == 7:
        total_valid += 1
print(total_valid)

