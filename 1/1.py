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
        POINT -= value
    else:
        POINT += value

    if POINT < 0 or POINT >= MAX:
        POINT %= MAX

    if POINT == 0:
        result += 1

print(result)