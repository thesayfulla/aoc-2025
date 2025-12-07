with open('input.txt') as f:
    INPUT = f.read()

# INPUT = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """

DIRECTIONS = {
    "top": (-1, 0),
    "top_right": (-1, 1),
    "right": (0, 1),
    "bottom_right": (1, 1),
    "bottom": (1, 0),
    "bottom_left": (1, -1),
    "left": (0, -1),
    "top_left": (-1, -1),
}

INPUT = [list(line) for line in INPUT.splitlines()]

row = len(INPUT)
col = len(INPUT[0])

def get_neighbors(row_index, col_index, rows, cols):
    global INPUT
    neighbors = {}

    for direction, (dr, dc) in DIRECTIONS.items():
        nr, nc = row_index + dr, col_index + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors[direction] = INPUT[nr][nc]

    return neighbors


result = 0
for r in range(row):
    for c in range(col):
        if INPUT[r][c] == '@':
            neighbors = get_neighbors(r, c, row, col)
            count = sum(1 for v in neighbors.values() if v == '@')
            if count < 4:
                result += 1

print(result)
# assert result == 13
