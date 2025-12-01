POINT = 50
MAX = 100
result = 0

with open("input.txt") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if not line:
        continue

    direction = line[0]
    value = int(line[1:])

    if direction == "L":
        mod = value % 100
        result += value // 100
        if mod >= POINT and POINT != 0:
            result += 1
        POINT = (POINT - mod) % 100

    else:
        mod = value % 100
        result += value // 100
        if mod >= (100 - POINT) and POINT != 0:
            result += 1
        POINT = (POINT + mod) % 100


print(result)
