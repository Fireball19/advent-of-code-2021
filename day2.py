horizontal = 0
depth = 0

with open('day2_input.txt') as f:
    for line in f:
        command = line.split()[0]
        value = int(line.split()[1])
        if command == "forward":
            horizontal += value
        elif command == "up":
            depth -= value
        elif command == "down":
            depth += value

print(horizontal * depth)