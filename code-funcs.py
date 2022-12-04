def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

# Divide Chunk By Two
def splitstring(str):
    str1, str2 = str[:len(str)//2], str[len(str)//2:]
    return str1, str2