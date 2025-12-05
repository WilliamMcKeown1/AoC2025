ranges = []; ids = []
with open("input.txt") as f:
    lines = f.readlines()
    for line in lines:
        if "-" in line:
            a, b = map(int, line.split('-'))
            ranges.append((a, b))
        elif not line.strip():
            continue
        else:
            ids.append(int(line.strip()))
merged = []
ranges.sort()
for start, end in ranges:
    if not merged or start > merged[-1][1] + 1:
        merged.append([start,end])
    else:
        merged[-1][1] = max(merged[-1][1],end)
total = sum(b - a + 1 for a, b in merged)
count = 0
for i in ids:
    for a, b in merged:
        if a <= i <= b:
            count += 1
            break
print("Part 1: "+str(count)+"\nPart 2: "+str(total))