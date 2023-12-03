import re

with open("input", "r") as file:
    lines = file.read().split("\n")


def add_number_to_gear(Y, X, number):
    global gears
    if not f"X{X}Y{Y}" in gears:
        gears[f"X{X}Y{Y}"] = [number]
    else:
        gears[f"X{X}Y{Y}"].append(number)


numbers = []
gears = dict()

for Y, line in enumerate(lines):
    line_numbers = re.findall('\d+', line)
    skipped = 0
    line_copy = line
    for line_number in line_numbers:
        start = line_copy.index(line_number) + skipped
        length = len(line_number)
        if start > 0 and lines[Y][start - 1] == '*':
            add_number_to_gear(Y, start-1, int(line_number))
        if start + length < len(line) and lines[Y][start+length] == '*':
            add_number_to_gear(Y, start+length, int(line_number))
        for X in range(start - 1, start + length + 1):
            if X >= 0 and X < len(line):
                if Y > 0 and lines[Y - 1][X] == '*':
                    add_number_to_gear(Y - 1, X, int(line_number))
                if Y < len(lines) - 1 and lines[Y + 1][X] == '*':
                    add_number_to_gear(Y + 1, X, int(line_number))
        skipped += length
        line_copy = line_copy.replace(line_number, '', 1)

ratio_sum = 0

for gear in gears:
    if len(gears[gear]) == 2:
        ratio_sum += gears[gear][0] * gears[gear][1]
print(ratio_sum)
