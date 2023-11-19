from collections import Counter
if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        gamma = ""
        epsilon = ""
        test = [list(line) for line in lines]
        #test2 = [line[0] for line in lines]
        for i in range(len(lines[0])):
            numbers = [line[i] for line in lines]
            bit = [bit for bit, bit_count, in Counter(numbers).most_common(1)]
            #print(numbers)
            #print(bit)
            gamma += bit[0]
            if bit[0] == "1":
                epsilon += "0"
            else:
                epsilon += "1"

        print("Binary Gamma: " + gamma)
        print("Binary Epsilon: " + epsilon)

        decimal_gamma = int(gamma,2)
        print("Decimal Gama: "+str(decimal_gamma))
        decimal_epsilon = int(epsilon,2)
        print("Decimal Epsilon: "+str(decimal_epsilon))
        power_c = decimal_gamma*decimal_epsilon
        print("D Power Consumption: "+ str(power_c))
        print("B Power Consumption: "+str(bin(power_c)))
            
        

