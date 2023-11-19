import time

with open('input.txt') as f:
    lines = [int(line.rstrip()) for line in f]


def get_sum_3(lines):
    for num1 in lines:
        for num2 in lines:
            match = 2020-num1-num2
            if match in lines:
                print(num1)
                print(num2)
                print(match)
                return

def get_sum_3_sort(des,asc):
    for num1 in des:
        match = 2020 - num1
        for num2 in asc:
            if num2 >= match:
                break
            else:
                match2 = 2020-num1-num2
                if match2 in des:
                    print(num1)
                    print(num2)
                    print(match2)
                    return


start_time = time.time()
get_sum_3(lines)
print("--- %s seconds ---" % (time.time() - start_time))

asc = sorted(lines)
des = sorted(lines,reverse=True)

start_time_2 = time.time()
get_sum_3_sort(des,asc)
print("--- %s seconds ---" % (time.time() - start_time_2))
