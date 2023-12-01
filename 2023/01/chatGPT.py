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