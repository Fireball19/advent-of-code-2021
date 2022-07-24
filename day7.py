numbers = []
fuel = []

with open('day7_input.txt') as f:
    numbers = list(map(int, f.read().split(',')))

minValue = min(numbers)
maxValue = max(numbers)

for y in range(minValue, maxValue):
    tmp = 0
    for i in range(0, len(numbers)):
        tmp += abs(numbers[i] - y)
    fuel.append(tmp)

print(min(fuel))