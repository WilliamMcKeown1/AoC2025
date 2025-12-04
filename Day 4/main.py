grid = []
dirs = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),  (1, 0), (1, 1)]

with open("input.txt") as f:
    grid = [list(line.strip()) for line in f.read().splitlines() if line.strip()]

total = 0

def accessible(i, j):
    neighbors = 0
    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == '@':
            neighbors += 1
    return neighbors < 4

while True:
    remove = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@" and accessible(i,j):
                remove.append((i,j))
    
    if not remove:
        break
    for i,j in remove:
        grid[i][j] = "."
    
    total += len(remove)

print(total)