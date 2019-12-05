import math

def recursive_mass(mass):
    mass_value = math.floor(int(mass)/3)-2
    if (mass_value <= 0):
        return 0
    else:
        return mass_value + recursive_mass(mass_value)



if __name__ == '__main__':
    line_list = [line.rstrip('\n') for line in open("input.txt")]
    #function = lambda x: (math.floor(int(x)/3)-2)
    print(sum(list(map(recursive_mass, line_list))))        
