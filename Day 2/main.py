ranges = []

with open("input.txt") as f:
    ranges = f.read().split(",")

def is_repeated(num):
    str_num = str(num)
    for pattern_len in range(1, len(str_num)//2 + 1):
        if len(str_num) % pattern_len == 0:
            pattern = str_num[:pattern_len]
            if pattern * (len(str_num) // pattern_len) == str_num:
                return True
    return False

total = 0

for r in ranges:
    start, end = map(int, r.split("-"))
    for n in range(start, end+1):
        if is_repeated(n):
            total += n

print(total)