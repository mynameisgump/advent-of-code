# Prompt:
# Write a python script to solve this advent of code problem:
# --- Day 1: Trebuchet?! ---

# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

# X GPT 3.5 Solution
def gpt3_5_p1_solution():
    def sum_calibration_values(calibration_document):
        total_sum = 0

        # Split the calibration document into lines
        lines = calibration_document.splitlines()

        # Iterate through each line in the document
        for line in lines:
            # Extract the first and last characters and convert them to integers
            first_digit = int(line[0])
            last_digit = int(line[-1])

            # Combine the digits to form a two-digit number
            calibration_value = int(str(first_digit) + str(last_digit))

            # Add the calibration value to the total sum
            total_sum += calibration_value

        return total_sum

    # Example calibration document
    calibration_doc = """1abc2
    pqr3stu8vwx
    a1b2c3d4e5f
    treb7uchet"""

    # Calculate the sum of calibration values
    result = sum_calibration_values(calibration_doc)
    print(f"The sum of all calibration values is: {result}")

# O GPT 4.0 with the same prompt 
def gpt4_0_p2_solution():
    def sum_calibration_values(file_path):
        """
        Sums the calibration values from the provided file.
        Each calibration value is determined by combining the first and last digit of each line into a two-digit number.
        """
        total_sum = 0

        with open(file_path, 'r') as file:
            for line in file:
                # Extract digits from the line
                digits = [char for char in line if char.isdigit()]

                if digits:
                    # Combine the first and last digit to form a two-digit number
                    calibration_value = int(digits[0] + digits[-1])
                    total_sum += calibration_value

        return total_sum

    print(sum_calibration_values("input.txt"))

# Prompt:
# can you write me a python script to solve part 2 of this advent of code problem:
# --- Day 1: Trebuchet?! ---

# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet

# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

# --- Part Two ---

# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen

# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

# GPT 3.5
def gpt3_5_p2_solution():
    def sum_calibration_values_with_words(calibration_document):
        digit_words = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }

        total_sum = 0

        for line in calibration_document:
            # Replace word representations with their numerical counterparts
            for word, digit in digit_words.items():
                line = line.replace(word, digit)

            # Find the first and last characters, convert them to integers, and calculate the sum
            first_digit = int(line[0])
            last_digit = int(line[-1])
            value = first_digit * 10 + last_digit
            total_sum += value

        return total_sum

    # Example calibration document
    calibration = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]

    result = sum_calibration_values_with_words(calibration)
    print(f"The sum of all calibration values is: {result}")

# GPT 4.0
def gpt4_0_p2_solution():
    def sum_calibration_values_part_two(file_path):
        """
        Sums the calibration values from the provided file for Part Two of the problem.
        Each calibration value is determined by finding the real first and last digit (or spelled out digit) 
        of each line and combining them into a two-digit number.
        """
        # Mapping of spelled out digits to their numeric values
        digit_mapping = {
            'one': '1', 'two': '2', 'three': '3', 'four': '4', 
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
        }

        total_sum = 0

        with open(file_path, 'r') as file:
            for line in file:
                # Replace spelled out digits with their numeric counterparts
                for word, digit in digit_mapping.items():
                    line = line.replace(word, digit)

                # Extract digits from the line
                digits = [char for char in line if char.isdigit()]

                if digits:
                    # Combine the first and last digit to form a two-digit number
                    calibration_value = int(digits[0] + digits[-1])
                    total_sum += calibration_value

        return total_sum
    print(sum_calibration_values_part_two("example2.txt"))

# Bonus Prompt:
# This solution does not work in some cases. For example, if one of the inputs was "eighthree", 
# he correct calibration value is 83. This solution with replace the "three" with 3, resulting 
# in "eigh3", meaning that it will not correctly add 8 to the beginning of the string. Please fix this
def gpt4_0_p2_solution_bonus():
    def sum_calibration_values_part_two_fixed(file_path):
        """
        Sums the calibration values from the provided file for Part Two of the problem.
        Each calibration value is determined by finding the real first and last digit (or spelled out digit) 
        of each line and combining them into a two-digit number.
        """
        # Mapping of spelled out digits to their numeric values
        digit_mapping = {
            'one': '1', 'two': '2', 'three': '3', 'four': '4', 
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
        }

        total_sum = 0

        with open(file_path, 'r') as file:
            for line in file:
                # Process each line to replace spelled out digits with numeric digits
                for word in line.split():
                    if word in digit_mapping:
                        line = line.replace(word, digit_mapping[word], 1)
                        
                # Extract digits from the line
                digits = [char for char in line if char.isdigit()]

                if digits:
                    # Combine the first and last digit to form a two-digit number
                    calibration_value = int(digits[0] + digits[-1])
                    total_sum += calibration_value

        return total_sum

    # Example usage
    # Assuming the file path is 'calibration_document_part_two_fixed.txt'
    print(sum_calibration_values_part_two_fixed('input.txt')) 

#gpt3_5_p1_solution()
#gpt4_0_p1_solution()
#gpt3_5_p2_solution()
#gpt4_0_p2_solution()
gpt4_0_p2_solution_bonus()