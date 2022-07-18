bits = 0
with open('day3_input.txt') as f:
    bits = len(f.readline()) - 1

bitsCount = [[0 for x in range(2)] for y in range(bits)] 

position = 0
while position < bits:
    with open('day3_input.txt') as f:
        for line in f:
            bit = int(line[position])
            if (bit == 0): 
                bitsCount[position][0] += 1
            elif (bit == 1): 
                bitsCount[position][1] += 1
        position += 1

most = ''
least = ''
for x in range(bits):
    if (bitsCount[x][0] > bitsCount[x][1]):
        most += '0'
        least += '1'
    else:
        most += '1'
        least += '0'
mostDec = int(most, 2)
leastDec = int(least, 2)

print(mostDec * leastDec)