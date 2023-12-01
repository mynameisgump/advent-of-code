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

# GPT 3.5 Solution
# def sum_calibration_values(calibration_document):
#     total_sum = 0

#     # Split the calibration document into lines
#     lines = calibration_document.splitlines()

#     # Iterate through each line in the document
#     for line in lines:
#         # Extract the first and last characters and convert them to integers
#         first_digit = int(line[0])
#         last_digit = int(line[-1])

#         # Combine the digits to form a two-digit number
#         calibration_value = int(str(first_digit) + str(last_digit))

#         # Add the calibration value to the total sum
#         total_sum += calibration_value

#     return total_sum

# # Example calibration document
# calibration_doc = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet"""

# # Calculate the sum of calibration values
# result = sum_calibration_values(calibration_doc)
# print(f"The sum of all calibration values is: {result}")



# GPT 4.0 with the same prompt, is correct
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