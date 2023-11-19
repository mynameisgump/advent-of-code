def double_char_2(string):
    string = str(string)
    for num in string:
        total = string.count(num)
        if (total == 2):
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
    if (double_char_2(i) and ascend(i)):
        list_of_passwords.append(i)
print(len(list_of_passwords))
