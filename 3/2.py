with open('input.txt') as f:
    INPUT = f.read()

# INPUT = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111
# """

result = 0


def max_sub(numbers, k):
    N = len(numbers)
    start = 0
    digits = []
    for pos in range(k):
        end = N - (k - pos) + 1
        best_digit = -1
        best_index = start
        
        for i in range(start, end):
            number = numbers[i]
            if number > best_digit:
                best_digit = number
                best_index = i
                if best_digit == 9:
                    break
        
        digits.append(best_digit)
        start = best_index + 1

    val = 0
    for number in digits:
        val = val * 10 + number
    return val


for line in INPUT.splitlines():
    numbers = [int(x) for x in line]
    result += max_sub(numbers, 12)

print(result)
# assert result == 3121910778619