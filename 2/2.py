with open("input.txt") as f:
    INPUT = f.read().strip()

result = 0
ranges = INPUT.split(",")


def is_repeated(number):
    s = str(number)
    n = len(s)
    i = 1
    while i <= n // 2:
        c = s[:i]
        count = s.count(c)
        if count >= 2 and len(c) * count == n:
            return True
        i += 1

for r in ranges:
    start, end = map(int, r.split("-"))
    
    for number in range(start, end + 1):
        if is_repeated(number):
            result += number


print(result)
