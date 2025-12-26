filepath = "input.txt"
grid = []
total = 0

def can_access(x, y, grid) -> bool:
    paper_rolls = -1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not((x + i < 0 or x + i >= len(grid) or (y + j < 0 or y + j >= len(grid[0])))):
                if grid[x+i][y+j] == "@":
                    paper_rolls += 1

    if paper_rolls < 4:
        return True
    return False

with open (filepath) as f:
    lines = f.readlines()
    for line in lines:
        grid.append(line.strip())

# for x in grid:
#     print(x)

for row,line in enumerate(grid):
    for col, char in enumerate(line):
        if char == "@":
            if can_access(row, col, grid):
                total += 1

print(total)
