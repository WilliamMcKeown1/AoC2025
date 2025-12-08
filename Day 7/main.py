def count_timelines(grid_lines):
    grid = [list(line.rstrip("\n")) for line in grid_lines]
    height = len(grid)
    width = max(len(row) for row in grid)

    start_col = None, None
    for c in range(width):
        if grid[0][c] == 'S':
            start_col = c
            break

    num = [[0] * width for _ in range(height)]
    num[0][start_col] = 1
    for r in range(0, height - 1):
        for c in range(width):
            if num[r][c] == 0:
                continue
            count = num[r][c]
            if grid[r+1][c] == '^':
                if c - 1 >= 0:
                    num[r+1][c-1] += count
                if c + 1 < width:
                    num[r+1][c+1] += count
            else:
                num[r+1][c] += count

    total = sum(num[height - 1])
    return total

if __name__ == "__main__":
    with open("input.txt") as f:
        grid_input = [line.rstrip("\n") for line in f]
    timelines = count_timelines(grid_input)
    print(timelines)