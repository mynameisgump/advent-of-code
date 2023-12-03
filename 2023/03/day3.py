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
                    num_col = cur_pos % 10;
                    num_row = math.floor(cur_pos/10);
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
                sym_col = cur_pos % 10;
                sym_row = math.floor(cur_pos/10);
                print()
                print("Symbol hit:", char)
                sym_positions = []
                for col in range(-1,2):
                    for row in range(-1,2):
                        cur_sym_col = sym_col+col
                        cur_sym_row = sym_row+row
                        print(cur_sym_row,cur_sym_col)
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
            #print(len(intersections))
            if len(intersections) > 0:
                summable_numbers.append(int(number))
            #print(number,positions)
        print(sum(summable_numbers))
def part2(filename):
    with open(filename) as f:
        lines = f.read().split("\n");

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
            part1(filename)
        case "p2":
            part2(filename)