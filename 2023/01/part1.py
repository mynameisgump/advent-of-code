import re
def remove_letters(string):
    return re.sub("[^0-9]", "", string);

def calc_calibration(string):
    return string[0]+string[-1]

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        input_string = f.read().replace("\n", " ").split(" ");
        digits_list = [remove_letters(item) for item in input_string if item != ""]
        calibration_values = [int(calc_calibration(item)) for item in digits_list]
        print(sum(calibration_values))
        

        # elves = f.read().replace("\n", " ").split("  ")
        # largest = 0 
        # for elf in elves:
        #     food = elf.split(" ")
        #     print(food)

        #     food = [int(item) for item in food if item != ""]
        #     calories = sum(food)

        #     if calories > largest:
        #         largest = calories
            
        # print(largest)