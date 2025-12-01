import re

combs = []
cur = 50
zeroes = 0
MIN_VAL = 0
MAX_VAL = 99
RANGE_SIZE = MAX_VAL - MIN_VAL + 1

with open("input.txt", 'r') as f:
    combs = f.readlines()

for line in combs:
    match = re.match(r"(^\D*)(\d+)(.*)", line.strip())
    if match:
        direction = match.group(1).strip()
        add = int(match.group(2))
        
        for i in range(add):
            if direction == "R":
                cur += 1
                if cur > MAX_VAL:
                    cur = MIN_VAL
            elif direction == "L":
                cur -= 1
                if cur < MIN_VAL:
                    cur = MAX_VAL

            if cur == MIN_VAL:
                zeroes += 1

print(f"Zeroes: {zeroes}")