import argparse
import re
import math 

parser = argparse.ArgumentParser()
parser.add_argument("solution", choices=["p1","p2"])
parser.add_argument("input", choices=["i1","ex1","ex2"])
args = parser.parse_args();

def part1(filename):
    with open(filename) as f:
        lines = f.read().split("\n");
        # field[row][column]
        field = []
        field_string = ""
        row_length = len(lines[0])
        col_length = len(lines);
        for line in lines:
            field.append([*line])
            field_string += line
            #print(field_string)

        digit_w_pos = []
        cur_num = "";
        cur_pos = 0;

        # Get all digits with pos
        num_col = 0;
        num_row = 0;
        for char in field_string:
            if char.isdigit():
                if cur_num == "":
                    num_col = cur_pos % col_length;
                    num_row = math.floor(cur_pos/row_length);
                cur_num += char;
            else:
                if cur_num != "":
                    spaces = []
                    for i in range(len(cur_num)):
                        spaces.append([num_row,num_col+i])
                    digit_w_pos.append((cur_num,spaces))
                    cur_num = ""
            
            cur_pos += 1
        print(digit_w_pos)

        symbol_w_pos = []
        cur_num = "";
        cur_pos = 0;

        # Get all digits with pos
        sym_col = 0;
        sym_row = 0;
        for char in field_string:
            if not char.isdigit() and char != ".":
                sym_col = cur_pos % col_length;
                sym_row = math.floor(cur_pos/row_length);
                sym_positions = []
                for col in range(-1,2):
                    for row in range(-1,2):
                        cur_sym_col = sym_col+col
                        cur_sym_row = sym_row+row
                        if cur_sym_col >= 0 and cur_sym_col < row_length:
                            if cur_sym_row >= 0 and col_length:
                                sym_positions.append([cur_sym_row,cur_sym_col])
                symbol_w_pos.append([char, sym_positions])
            
            cur_pos += 1
        #print(symbol_w_pos)
        all_symbol_pos = []
        for pair in symbol_w_pos:
            all_symbol_pos.append(pair[1])
        all_symbol_pos = sum(all_symbol_pos,[])
        #print(all_symbol_pos)

        print()
        summable_numbers = []
        for number_pair in digit_w_pos:
            number = number_pair[0]
            positions = number_pair[1]
            intersections = [i for i in positions if i in all_symbol_pos]
            if len(intersections) > 0:
                summable_numbers.append(int(number))
                print(number, positions)
                        #print(number,positions)
        print(sum(summable_numbers))
def part2(filename):
    with open(filename) as f:
        lines = f.read().split("\n");

def part1fixed(filename):
    with open(filename) as f:
        lines = f.read().split("\n");
        field = []
        field_string = ""

        total_col = len(lines[0])
        total_rows = len(lines)
        for line in lines:
            field.append([*line])
            field_string += line

        digit_w_pos = []
        cur_num = "";
        cur_pos = 0;

        # Get all digits with pos
        num_col = 0;
        num_row = 0;
        for i in range(len(field_string)):
            char = field_string[i]
        # for char in field_string:
            if char.isdigit():
                if cur_num == "":
                    num_row = math.floor(cur_pos/total_col);
                    num_col = cur_pos % total_col;
                cur_num += char;
                if i+1==len(field_string):
                    spaces = []
                    for i in range(len(cur_num)):
                        spaces.append([num_row,num_col+i])
                    digit_w_pos.append((cur_num,spaces))
                    cur_num = ""
                            
            else:
                if cur_num != "":
                    spaces = []
                    for i in range(len(cur_num)):
                        spaces.append([num_row,num_col+i])
                    digit_w_pos.append((cur_num,spaces))
                    cur_num = ""
            
            cur_pos += 1

        symbol_w_pos = []
        cur_num = "";
        cur_pos = 0;

        # Get all digits with pos
        sym_col = 0;
        sym_row = 0;
        for char in field_string:
            if not char.isdigit() and char != ".":
                sym_row = math.floor(cur_pos/total_col);
                sym_col = cur_pos % total_col;

                sym_positions = []
                for col in range(-1,2):
                    for row in range(-1,2):
                        cur_sym_row = sym_row+row
                        cur_sym_col = sym_col+col
                        # print(cur_sym_col, cur_sym_row)
                        if cur_sym_col >= 0 and cur_sym_col < total_col:
                            if cur_sym_row >= 0 and cur_sym_row < total_rows:
                                sym_positions.append([cur_sym_row,cur_sym_col])
                symbol_w_pos.append([char, sym_positions])
            
            cur_pos += 1
        all_symbol_pos = []
        for pair in symbol_w_pos:
            all_symbol_pos.append(pair[1])
        all_symbol_pos = sum(all_symbol_pos,[])

        summable_numbers = []
        for number_pair in digit_w_pos:
            number = number_pair[0]
            positions = number_pair[1]
            intersections = [i for i in all_symbol_pos if i in positions]
            if len(intersections) > 0:
                summable_numbers.append(int(number))
        print(summable_numbers);
        print("Sum :",sum(summable_numbers))


def testing(filename):
    with open(filename) as f:
        # Test case 1 and 2 are done 
        test_cases = f.read().split("\n\n");
        for case in test_cases:
            lines = case.split("\n");
            # print("")
            print("New Test Case: ", lines)

            # field[row][column]
            field = []
            field_string = ""
            # row_length = len(lines[0])
            # col_length = len(lines);

            total_col = len(lines[0])
            total_rows = len(lines)
            # print(total_col)
            # print(total_rows)
            for line in lines:
                field.append([*line])
                field_string += line
                #print(field_string)

            digit_w_pos = []
            cur_num = "";
            cur_pos = 0;

            # Get all digits with pos
            num_col = 0;
            num_row = 0;
            for i in range(len(field_string)):
                char = field_string[i]
            # for char in field_string:
                if char.isdigit():
                    # print(char)
                    if cur_num == "":
                        num_row = math.floor(cur_pos/total_col);
                        num_col = cur_pos % total_col;
                    cur_num += char;
                    if i+1==len(field_string):
                        spaces = []
                        for i in range(len(cur_num)):
                            spaces.append([num_row,num_col+i])
                        digit_w_pos.append((cur_num,spaces))
                        cur_num = ""
                             
                else:
                    if cur_num != "":
                        spaces = []
                        for i in range(len(cur_num)):
                            spaces.append([num_row,num_col+i])
                        digit_w_pos.append((cur_num,spaces))
                        cur_num = ""
                
                cur_pos += 1
            # print(digit_w_pos)

            symbol_w_pos = []
            cur_num = "";
            cur_pos = 0;

            # Get all digits with pos
            sym_col = 0;
            sym_row = 0;
            for char in field_string:
                if not char.isdigit() and char != ".":
                    # print("CHARACTER:", char)
                    # print("CUR POS: ", cur_pos)
                    # Correct
                    sym_row = math.floor(cur_pos/total_col);
                    sym_col = cur_pos % total_col;

                    # print("SYM ROW:", sym_row)
                    # print("SYM COL:", sym_col)
                    sym_positions = []
                    for col in range(-1,2):
                        for row in range(-1,2):
                            cur_sym_row = sym_row+row
                            cur_sym_col = sym_col+col
                            # print(cur_sym_col, cur_sym_row)
                            if cur_sym_col >= 0 and cur_sym_col < total_col:
                                if cur_sym_row >= 0 and cur_sym_row < total_rows:
                                    sym_positions.append([cur_sym_row,cur_sym_col])
                    symbol_w_pos.append([char, sym_positions])
                
                cur_pos += 1
            # print(symbol_w_pos)
            all_symbol_pos = []
            for pair in symbol_w_pos:
                all_symbol_pos.append(pair[1])
            all_symbol_pos = sum(all_symbol_pos,[])
            #print(all_symbol_pos)

            summable_numbers = []
            for number_pair in digit_w_pos:
                number = number_pair[0]
                positions = number_pair[1]
                intersections = [i for i in all_symbol_pos if i in positions]
                # print("Number+Inter", number, intersections, all_symbol_pos)
                if len(intersections) > 0:
                    summable_numbers.append(int(number))
                    #print(number, positions)
                            #print(number,positions)
            print(summable_numbers);
            print("Sum :",sum(summable_numbers))

def testing_part2(filename):
    with open(filename) as f:
        # Test case 1 and 2 are done 
        test_cases = f.read().split("\n\n");
        for case in test_cases:
            lines = case.split("\n");
            # print("")
            print("New Test Case: ", lines)

            # field[row][column]
            field = []
            field_string = ""
            # row_length = len(lines[0])
            # col_length = len(lines);

            total_col = len(lines[0])
            total_rows = len(lines)
            # print(total_col)
            # print(total_rows)
            for line in lines:
                field.append([*line])
                field_string += line
                #print(field_string)

            digit_w_pos = []
            cur_num = "";
            cur_pos = 0;

            # Get all digits with pos
            num_col = 0;
            num_row = 0;
            for i in range(len(field_string)):
                char = field_string[i]
            # for char in field_string:
                if char.isdigit():
                    # print(char)
                    if cur_num == "":
                        num_row = math.floor(cur_pos/total_col);
                        num_col = cur_pos % total_col;
                    cur_num += char;
                    if i+1==len(field_string):
                        spaces = []
                        for i in range(len(cur_num)):
                            spaces.append([num_row,num_col+i])
                        digit_w_pos.append((cur_num,spaces))
                        cur_num = ""
                             
                else:
                    if cur_num != "":
                        spaces = []
                        for i in range(len(cur_num)):
                            spaces.append([num_row,num_col+i])
                        digit_w_pos.append((cur_num,spaces))
                        cur_num = ""
                
                cur_pos += 1
            # print(digit_w_pos)

            symbol_w_pos = []
            cur_num = "";
            cur_pos = 0;

            # Get all digits with pos
            sym_col = 0;
            sym_row = 0;
            for char in field_string:
                if char == "*":
                    # print("CHARACTER:", char)
                    # print("CUR POS: ", cur_pos)
                    # Correct
                    sym_row = math.floor(cur_pos/total_col);
                    sym_col = cur_pos % total_col;

                    # print("SYM ROW:", sym_row)
                    # print("SYM COL:", sym_col)
                    sym_positions = []
                    for col in range(-1,2):
                        for row in range(-1,2):
                            cur_sym_row = sym_row+row
                            cur_sym_col = sym_col+col
                            # print(cur_sym_col, cur_sym_row)
                            if cur_sym_col >= 0 and cur_sym_col < total_col:
                                if cur_sym_row >= 0 and cur_sym_row < total_rows:
                                    sym_positions.append([cur_sym_row,cur_sym_col])
                    symbol_w_pos.append([char, sym_positions])
                
                cur_pos += 1

            print(symbol_w_pos)

            total_sum = 0
            for symbol_pair in symbol_w_pos:
                total_inter = []
                for digit_pair in digit_w_pos:
                    intersections = [i for i in symbol_pair[1] if i in digit_pair[1]]
                    if len(intersections) > 0:
                        total_inter.append(digit_pair[0])
                    if len(total_inter) > 1:
                        break
                if len(total_inter) > 1:
                    gear_sum = int(total_inter[0])*int(total_inter[1])
                    total_sum += gear_sum
                print(total_inter)
            print(total_sum)
                
            # print(symbol_w_pos)
            # all_symbol_pos = []
            # for pair in symbol_w_pos:
            #     all_symbol_pos.append(pair[1])
            # all_symbol_pos = sum(all_symbol_pos,[])
            #print(all_symbol_pos)

            # summable_numbers = []
            # for number_pair in digit_w_pos:
            #     number = number_pair[0]
            #     positions = number_pair[1]
            #     intersections = [i for i in all_symbol_pos if i in positions]
                # print("Number+Inter", number, intersections, all_symbol_pos)
                # if len(intersections) > 0:
                #     summable_numbers.append(int(number))
                    #print(number, positions)
                            #print(number,positions)
            # print(summable_numbers);
            # print("Sum :",sum(summable_numbers))

if __name__ == "__main__":
    input_selection = args.input
    solution_selection = args.solution;
    filename = ""
    match input_selection:
        case "i1":
            filename="input.txt"
        case "ex1":
            filename="example1.txt"
    match solution_selection:
        case "p1":
            #part1(filename)
            #testing("test1.txt")
            part1fixed("input.txt")
            #part1fixed("example1.txt")
        case "p2":
            testing_part2("test1.txt")