import sys

def find_start():
	global map
	for y, yel in enumerate(map):
		for x, xel in enumerate(yel):
			if (xel == "S"):
				return [y,x]

def find_valid_next(coords):
	global map
	if coords[0] > 0:
		to_check = map[coords[0] - 1][coords[1]]
		if to_check == "|" or to_check == "7" or to_check == "F":
			return [coords[0] - 1, coords[1]]
		
	if coords[0] < len(map):
		to_check = map[coords[0] + 1][coords[1]]
		if to_check == "|" or to_check == "J" or to_check == "L":
			return [coords[0] + 1, coords[1]]

	if coords[1] > 0:
		to_check = map[coords[0]][coords[1] - 1]
		if to_check == "-" or to_check == "L" or to_check == "F":
			return [coords[0], coords[1] - 1]

	if coords[1] < len(map[0]):
		to_check = map[coords[0]][coords[1] + 1]
		if to_check == "-" or to_check == "J" or to_check == "7":
			return [coords[0], coords[1] + 1]

def next_step(old, new):
	global map
	if map[new[0]][new[1]] == "|":
		if old[0] < new[0]:
			return [new[0] + 1, new[1]]
		else:
			return [new[0] - 1, new[1]]

	if map[new[0]][new[1]] == "J":
		if old[0] < new[0]:
			return [new[0], new[1] - 1]
		else:
			return [new[0] - 1, new[1]]
		
	if map[new[0]][new[1]] == "L":
		if old[0] < new[0]:
			return [new[0], new[1] + 1]
		else:
			return [new[0] - 1, new[1]]
		
	if map[new[0]][new[1]] == "F":
		if old[0] > new[0]:
			return [new[0], new[1] + 1]
		else:
			return [new[0] + 1, new[1]]
		
	if map[new[0]][new[1]] == "7":
		if old[0] > new[0]:
			return [new[0], new[1] - 1]
		else:
			return [new[0] + 1, new[1]]
	
	if map[new[0]][new[1]] == "-":
		if old[1] > new[1]:
			return [new[0], new[1] - 1]
		else:
			return [new[0], new[1] + 1]

def paint_map(coords, c):
	global map2
	global outside
	if map2[coords[0]][coords[1]] == "S":
		return
	if coords[0] == 0 or coords[0] == len(map2) - 1 or coords[1] == 0 or coords[1] == len(map2[0]) - 1:
		outside = c
	if map2[coords[0]][coords[1]] == c:
		return
	map2[coords[0]][coords[1]] = c
	if coords[0] > 0:
		paint_map([coords[0] - 1, coords[1]], c)
	if coords[0] + 1 < len(map2):
		paint_map([coords[0] + 1, coords[1]], c)
	if coords[1] > 0:
		paint_map([coords[0], coords[1] - 1], c)
	if coords[1] + 1 < len(map2[0]):
		paint_map([coords[0], coords[1] + 1], c)

	# diagonals
	if coords[0] > 0 and coords[1] > 0 and map2[coords[0] - 1][coords[1] - 1] != "S":
		paint_map([coords[0] - 1, coords[1] - 1], c)
	if coords[0] + 1 < len(map2) and coords[1] > 0 and map2[coords[0] + 1][coords[1] - 1] != "S":
		paint_map([coords[0] + 1, coords[1] - 1], c)
	if coords[0] > 0 and coords[1] + 1 < len(map2[0]) and map2[coords[0] - 1][coords[1] + 1] != "S":
		paint_map([coords[0] - 1, coords[1] + 1], c)
	if coords[0] + 1 < len(map2) and coords[1] + 1 < len(map2[0]) and map2[coords[0] + 1][coords[1] + 1] != "S":
		paint_map([coords[0] + 1, coords[1] + 1], c)

def case_straight_south(y, x):
	global map2
	if x > 0 and map2[y][x - 1] != "S":
		map2[y][x - 1] = "R"
	if x + 1 < len(map2[0]) and map2[y][x + 1] != "S":
		map2[y][x + 1] = "L"

def case_straight_north(y, x):
	global map2
	if x > 0 and map2[y][x - 1] != "S":
		map2[y][x - 1] = "L"
	if x + 1 < len(map2[0]) and map2[y][x + 1] != "S":
		map2[y][x + 1] = "R"

def case_J_south(y, x):
	global map2
	if x + 1 < len(map2[0]) and map2[y][x + 1] != "S":
		map2[y][x + 1] = "L"
	if y + 1 < len(map2) and map2[y + 1][x] != "S":
		map2[y + 1][x] = "L"

def case_J_east(y, x):
	global map2
	if x + 1 < len(map2[0]) and map2[y][x + 1] != "S":
		map2[y][x + 1] = "R"
	if y + 1 < len(map2) and map2[y + 1][x] != "S":
		map2[y + 1][x] = "R"

def case_L_south(y, x):
	global map2
	if x > 0 and map2[y][x - 1] != "S":
		map2[y][x - 1] = "R"
	if y + 1 < len(map2) and map2[y + 1][x] != "S":
		map2[y + 1][x] = "R"

def case_L_west(y, x):
	global map2
	if x > 0 and map2[y][x - 1] != "S":
		map2[y][x - 1] = "L"
	if y + 1 < len(map2) and map2[y + 1][x] != "S":
		map2[y + 1][x] = "L"

def case_7_north(y, x):
	global map2
	if x + 1 < len(map[0]) and map2[y][x + 1] != "S":
		map2[y][x + 1] = "R"
	if y > 0 and map2[y - 1][x] != "S":
		map2[y - 1][x] = "R"

def case_7_east(y, x):
	global map2
	if x + 1 < len(map[0]) and map2[y][x + 1] != "S":
		map2[y][x + 1] = "L"
	if y > 0 and map2[y - 1][x] != "S":
		map2[y - 1][x] = "L"

def case_F_north(y, x):
	global map2
	if x > 0 and map2[y][x - 1] != "S":
		map2[y][x - 1] = "L"
	if y > 0 and map2[y - 1][x] != "S":
		map2[y - 1][x] = "L"

def case_F_west(y, x):
	global map2
	if x > 0 and map2[y][x - 1] != "S":
		map2[y][x - 1] = "R"
	if y > 0 and map2[y - 1][x] != "S":
		map2[y - 1][x] = "R"

def case_straight_east(y, x):
	global map2
	if y > 0 and map2[y - 1][x] != "S":
		map2[y - 1][x] = "L"
	if y + 1 < len(map) and map2[y + 1][x] != "S":
		map2[y + 1][x] = "R"

def case_straight_west(y, x):
	global map2
	if y > 0 and map2[y - 1][x] != "S":
		map2[y - 1][x] = "R"
	if y + 1 < len(map) and map2[y + 1][x] != "S":
		map2[y + 1][x] = "L"

def write_left_right(old, new):
	global map
	global map2
	symbol = map[new[0]][new[1]]
	if symbol == "|":
		if old[0] < new[0]:
			case_straight_south(new[0], new[1])
		else:
			case_straight_north(new[0], new[1])
	elif symbol == "J":
		if old[0] < new[0]:
			case_J_south(new[0], new[1])
		else:
			case_J_east(new[0], new[1])
	elif symbol == "L":
		if old[0] < new[0]:
			case_L_south(new[0], new[1])
		else:
			case_L_west(new[0], new[1])
	elif symbol == "7":
		if old[0] > new[0]:
			case_7_north(new[0], new[1])
		else:
			case_7_east(new[0], new[1])
	elif symbol == "F":
		if old[0] > new[0]:
			case_F_north(new[0], new[1])
		else:
			case_F_west(new[0], new[1])
	elif symbol == "-":
		if old[1] > new[1]:
			case_straight_west(new[0], new[1])
		else:
			case_straight_east(new[0], new[1])

def is_surrounded(y, x):
	global map2
	if y == 0 or y == len(map2) or x == 0 or x == len(map2[0]):
		return False
	if map2[y - 1][x - 1] == "S" and map2[y - 1][x] == "S" and map2[y - 1][x + 1] == "S" and map2[y][x - 1] == "S" and map2[y][x + 1] == "S" and map2[y + 1][x - 1] == "S" and map2[y + 1][x] == "S" and map2[y + 1][x + 1] == "S":
		return True
	return False

sys.setrecursionlimit(5000)

map = [[c for c in line] for line in open("input", "r").read().split("\n")]

map2 = []

for line in map:
	newline = []
	for c in line:
		newline.append('.')
	map2.append(newline)

previous = find_start()
next = find_valid_next(previous)

while map[next[0]][next[1]] != "S":
	write_left_right(previous, next)
	map2[previous[0]][previous[1]] = "S"
	temp = next
	next = next_step(previous, next)
	previous = temp

map2[previous[0]][previous[1]] = "S"

outside = '?'

for y in range(len(map2)):
	for x in range(len(map2[0])):
		if map2[y][x] == "L" or map2[y][x] == "R":
			c = map2[y][x]
			map2[y][x] = "."
			paint_map([y, x], c)

if outside == "R":
	inside = "L"
else:
	inside = "R"

count = 0

for y, line in enumerate(map2):
	for x, c in enumerate(line):
		if c == inside:
			count += 1

print(count)
