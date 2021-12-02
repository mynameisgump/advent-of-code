if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        depth = 0
        pos = 0
        for line in lines:
            command = line.split(" ")
            if command[0] == "forward":
                pos += int(command[1])
            elif command[0] == "down":
                depth += int(command[1])
            elif command[0] == "up":
                depth -= int(command[1])
        print("Depth: "+str(depth))
        print("Pos: "+str(pos))
        print("Solution: "+str(depth*pos))