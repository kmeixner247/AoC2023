# shoelace formula, but the problem is that our coordinates are not points, but 1x1 squares
# we "lose" the following sqm for every coordinate: 1/2 for edge pieces, 3/4 for outer corners, 1/4 for inner corners
# most basic case would be a rectangle - 4 outer corners, rest edges, which gives a "compensation" of half the circumference plus 1/4 * 4
# I don't have the proof for it, but intuitively, additional inner corners can only come in pairs and are always counteracted by a pair of outer corners
# ..which balances the offset
# so the "compensation" stays half the circumference plus one.. always
# this took me way longer than I feel it should have tbh

def parse_part_1():
	return [line.split()[:-1] for line in open("input", 'r').read().split("\n")]

def parse_part_2():
	instructions = ["R", "D", "L", "U"]
	return [[instructions[int(c[-1])], int(c[:-1], 16)] for c in [line.split()[-1][2:-1] for line in open("input", 'r').read().split("\n")]]

# lines = parse_part_1()
lines = parse_part_2()
x = 0
y = 0
vertices = [(0, 0)]
circumference = 0
for line in lines:
	circumference += int(line[1])
	if line[0] == "R":
		x += int(line[1])
	elif line[0] == "L":
		x -= int(line[1])
	elif line[0] == "U":
		y += int(line[1])
	elif line[0] == "D":
		y -= int(line[1])
	vertices.append((x,y))

area = 0
for i in range(1, len(vertices)):
	area += (vertices[i - 1][0] + vertices[i][0]) * (vertices[i-1][1] - vertices[i][1])

print(int(((area + circumference) / 2) + 1))