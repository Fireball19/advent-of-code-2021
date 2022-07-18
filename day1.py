count = -1
previous = -1

with open('day1_input.txt') as f:
    for line in f:
        tmp = int(line)
        if tmp > previous:
            count += 1
        previous = tmp

print(count)