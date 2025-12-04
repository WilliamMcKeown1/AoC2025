def max_joltage(bank: str):
    digits = [int(d) for d in bank.strip()]
    best = 0
    chosen = []
    start = 0
    for i in range(12):
        remaining = 12 - i
        end = len(digits) - remaining + 1
        best_digit = max(digits[start:end])
        best_index = digits.index(best_digit, start, end)
        chosen.append(str(best_digit))
        start = best_index + 1
    return int("".join(chosen))

def total_output(lines):
    return sum(max_joltage(line) for line in lines)

with open("input.txt", "r") as f:
    lines = f.readlines()
result = total_output(lines)
print(result)