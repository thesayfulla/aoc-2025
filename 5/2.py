with open("input.txt") as f:
    INPUT = f.read().strip()

# INPUT = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32
# """

result = 0
ranges_s, _ = INPUT.split('\n\n')

ranges = []
for line in ranges_s.splitlines():
    start_s, end_s = line.split('-')
    ranges.append(range(int(start_s), int(end_s) + 1))

ranges.sort(key=lambda r: (r.start, r.stop))

new_ranges = [ranges[0]]
for other in ranges[1:]:
    if other.start in new_ranges[-1]:
        new_ranges[-1] = range(
            new_ranges[-1].start,
            max(other.stop, new_ranges[-1].stop),
        )
    else:
        new_ranges.append(other)

result = sum(len(r) for r in new_ranges)
print(result)

# assert result == 14