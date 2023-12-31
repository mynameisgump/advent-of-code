import re
import operator

conversion_table = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five":"5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
}

def replace_word(string, word, num):
    return string.replace(word,num)

def negative_index_filter(tuple):
    if tuple[1] == -1:
        return False;
    else:
        return True;

def words_to_num(string):
    conversion_table = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five":"5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for word in conversion_table.keys():
        string = string.replace(word, word[0]+word+word[-1])
    positions = {}
    for key, value in conversion_table.items():
        positions[key] = string.find(key);

    
    #print(positions);
    sorted_positions = sorted(positions.items(), key=operator.itemgetter(1))
    filtered = list(filter(negative_index_filter, sorted_positions))
    print()
    print(string)
    print(filtered)

    for letter_pair in filtered:
        # Attempt 1: Doesn't Work
        # string = string.replace(letter_pair[0], conversion_table[letter_pair[0]])

        # Attempt 2: Doesn't Work
        #word_index = string.find(letter_pair[0])
        # string = string[:word_index]+conversion_table[letter_pair[0]]+string[word_index:]
        
        # attempt 3: Maybe baby:
        string = string.replace(letter_pair[0], conversion_table[letter_pair[0]]+letter_pair[0])
    print(string)
    return string

def remove_letters(string):
    return re.sub("[^0-9]", "", string);

def calc_calibration(string):
    return string[0]+string[-1]

if __name__ == "__main__":
    words = conversion_table.keys()
    filename="input.txt"
    with open(filename) as f:
        input_strings = f.read().replace("\n", " ").split(" ");
        #print(input_strings)
        converted_strings = [words_to_num(item) for item in input_strings]
        print()
        #print(converted_strings)
        digits_list = [remove_letters(item) for item in converted_strings if item != ""]
        calibration_values = [int(calc_calibration(item)) for item in digits_list]
        print()
        print(sum(calibration_values))
        
