with open("input.txt") as f:
    lines = [ln.rstrip("\n") for ln in f]

height = len(lines)
width = max(len(ln) for ln in lines)
grid = [ln.ljust(width) for ln in lines]
op_row = height - 1

runs = []
col = 0
while col < width:
    if all(grid[r][col] == " " for r in range(height)):
        col += 1
        continue
    start = col
    while col < width and any(grid[r][col] != " " for r in range(height)):
        col += 1
    runs.append((start, col - 1))
total = 0

for start, end in runs:
    for col in range(start, end + 1):
        if grid[op_row][col] in "+*":
            op = grid[op_row][col]
            break

    numbers = []
    for col in range(end, start - 1, -1):
        digits = [grid[r][col] for r in range(op_row) if grid[r][col].isdigit()]
        if digits:
            numbers.append(int("".join(digits)))

    if op == "+":
        val = sum(numbers)
    else:
        val = 1
        for n in numbers:
            val *= n
    total += val

print(total)