import re

with open("input", "r") as file:
    lines = file.read().split("\n")

numbers = []

for Y, line in enumerate(lines):
    line_numbers = re.findall('\d+', line)
    skipped = 0
    line_copy = line
    for line_number in line_numbers:
        start = line_copy.index(line_number) + skipped
        length = len(line_number)
        adjacents = []
        if start > 0:
            adjacents.append(lines[Y][start - 1])
        if start + length < len(line):
            adjacents.append(lines[Y][start + length])
        for X in range(start - 1, start + length + 1):
            if X >= 0 and X < len(line):
                if Y > 0:
                    adjacents.append(lines[Y - 1][X])
                if Y < len(lines) - 1:
                    adjacents.append(lines[Y + 1][X])
        is_part = False
        for c in adjacents:
            if not c.isdigit() and c != '.':
                is_part = True
        numbers.append({
            "num": int(line_number),
            "start": start,
            "row": Y,
            "len": length,
            "adjacents": adjacents,
            "is_part": is_part
        })
        skipped += length
        line_copy = line_copy.replace(line_number, '', 1)

sum = 0
for number in numbers:
    if number["is_part"] == True:
        sum += number["num"]
    else:
        print(number)

print(sum)

