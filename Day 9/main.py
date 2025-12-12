def largest_rectangle(red_tiles):
    max_area = 0
    n = len(red_tiles)

    for i in range(n):
        x1, y1 = red_tiles[i]
        for j in range(i + 1, n):
            x2, y2 = red_tiles[j]

            dx = abs(x2 - x1)
            dy = abs(y2 - y1)

            if dx == 0 or dy == 0:
                continue
            area = (dx + 1) * (dy + 1)

            if area > max_area:
                max_area = area

    return max_area


red_tiles = []

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        x, y = map(int, line.split(","))
        red_tiles.append((x, y))

print(largest_rectangle(red_tiles))