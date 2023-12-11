map = [[c for c in line] for line in open("input", "r").read().split("\n")]

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

def next_step(old_coords, new_coords):
	global map
	if map[new_coords[0]][new_coords[1]] == "|":
		if old_coords[0] < new_coords[0]:
			return [new_coords[0] + 1, new_coords[1]]
		else:
			return [new_coords[0] - 1, new_coords[1]]

	if map[new_coords[0]][new_coords[1]] == "J":
		if old_coords[0] < new_coords[0]:
			return [new_coords[0], new_coords[1] - 1]
		else:
			return [new_coords[0] - 1, new_coords[1]]
		
	if map[new_coords[0]][new_coords[1]] == "L":
		if old_coords[0] < new_coords[0]:
			return [new_coords[0], new_coords[1] + 1]
		else:
			return [new_coords[0] - 1, new_coords[1]]
		
	if map[new_coords[0]][new_coords[1]] == "F":
		if old_coords[0] > new_coords[0]:
			return [new_coords[0], new_coords[1] + 1]
		else:
			return [new_coords[0] + 1, new_coords[1]]
		
	if map[new_coords[0]][new_coords[1]] == "7":
		if old_coords[0] > new_coords[0]:
			return [new_coords[0], new_coords[1] - 1]
		else:
			return [new_coords[0] + 1, new_coords[1]]
	
	if map[new_coords[0]][new_coords[1]] == "-":
		if old_coords[1] > new_coords[1]:
			return [new_coords[0], new_coords[1] - 1]
		else:
			return [new_coords[0], new_coords[1] + 1]

previous = find_start()
next = find_valid_next(previous)

count = 1
while map[next[0]][next[1]] != "S":
	temp = next
	next = next_step(previous, next)
	previous = temp
	count += 1

print(count / 2)
