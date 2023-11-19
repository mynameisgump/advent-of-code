

if __name__ == "__main__":
    filename="input.txt"
    open_chars = "[{(<"
    closing_chars = "]})>"
    illegal_char = {"]": 0,"}": 0,")": 0,">": 0}
    valid_pairs = {"[": "]","{": "}","(":")","<":">"}
    illegal_char_vals = {")": 3, "]": 57, "}": 1197, ">": 25137}

    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        errors = []
        for line in lines:
            print()
            bracket_stack = []
            for char in line:
                if char in open_chars:
                    bracket_stack.append(char)
                if char in closing_chars:
                    open_char = bracket_stack.pop()
                    close_char = char
                    if valid_pairs[open_char] != close_char:
                        pair = [open_char,close_char]
                        #print(pair)
                        errors.append(pair)

        #print(errors)
        for pair in errors:
            illegal_char[pair[1]] += 1
        #print(illegal_char)
        final_error_score = 0
        for k,v in illegal_char.items():
            line_score = illegal_char_vals[k]*int(v)
            #print(line_score)
            final_error_score += line_score
            
        print(final_error_score)
                