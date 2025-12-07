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

ranges, ids = INPUT.split("\n\n")
ranges = ranges.splitlines()
ids = list(map(int, ids.splitlines()))
fresh = set()


for id_ in ids:
    for range_ in ranges:
        start, end = map(int, range_.split("-"))
        if start <= id_ <= end:
            fresh.add(id_)
            break

print(len(fresh))

# assert len(fresh) == 3