with open("input.txt") as f:
    INPUT = f.read().strip()

result = 0

ranges = INPUT.split(",")


def is_repeated(number):
    s = str(number)
    n = len(s) // 2
    return s[:n] == s[n:]


for r in ranges:
    start, end = map(int, r.split("-"))
    
    for number in range(start, end + 1):
        if is_repeated(number):
            result += number


print(result)
