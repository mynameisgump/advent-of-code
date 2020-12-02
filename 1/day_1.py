with open('input.txt') as f:
    numbers = [line.rstrip() for line in f]

for num in numbers:
    match = 2020-int(num)
    if str(match) in numbers:
        print(num)
        print(match)
        break
