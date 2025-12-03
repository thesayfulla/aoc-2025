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
            for k in range(j + 1, N):
                for l in range(k + 1, N):
                    for m in range(l + 1, N):
                        for n in range(m + 1, N):
                            for o in range(n + 1, N):
                                for p in range(o + 1, N):
                                    for q in range(p + 1, N):
                                        for r in range(q + 1, N):
                                            for s in range(r + 1, N):
                                                for t in range(s + 1, N):
                                                    tmp.append(int(f"{numbers[i]}{numbers[j]}{numbers[k]}{numbers[l]}{numbers[m]}{numbers[n]}{numbers[o]}{numbers[p]}{numbers[q]}{numbers[r]}{numbers[s]}{numbers[t]}"))
    
    result += max(tmp)

print(result)
assert result == 3121910778619