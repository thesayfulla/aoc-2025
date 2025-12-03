with open('input.txt') as f:
    INPUT = f.read()

# INPUT = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """

result = 0

for line in INPUT.splitlines():
    tmp = []
    numbers = [int(x) for x in line]
    N = len(numbers)
    
    for i in range(N):
        for j in range(i + 1, N):
            tmp.append(int(f"{numbers[i]}{numbers[j]}"))
    
    result += max(tmp)

print(result)
# assert result == 357