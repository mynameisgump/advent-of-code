def double_char(string):
    string = str(string)
    string_length = len(string)
    for i in range(string_length-1):
        if string[i] == string[i+1]:
            return True
    return False

def ascend(string):
    str_list = list(str(string))
    if sorted(str_list) == list(str(string)):
        return True
    else:
        return False

list_of_passwords = []

for i in range(168630,718098+1):
    if (double_char(i) and ascend(i)):
        list_of_passwords.append(i)
print(len(list_of_passwords))
