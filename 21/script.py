# to be fair I did have a feeling that part 2 would come along with ridiculous numbers that will make this impossible

def find_start(my_map):
	for y in range(len(my_map)):
		for x in range(len(my_map[y])):
			if my_map[y][x] == "S":
				return (y, x)

def do_steps(start, depth):
	global my_map
	global maxsteps
	if depth > maxsteps:
		return
	(y, x) = start
	if y < 0 or x < 0 or y > len(my_map) or x > len(my_map[y]) or my_map[y][x] == "#":
		return
	if my_map[y][x] == "S" or my_map[y][x] == ".":
		my_map[y][x] = depth
	else:
		if depth >= my_map[y][x]:
			return
		my_map[y][x] = depth
	do_steps((y - 1, x), depth + 1)
	do_steps((y + 1, x), depth + 1)
	do_steps((y, x - 1), depth + 1)
	do_steps((y, x + 1), depth + 1)


my_map = [[c for c in line] for line in open("input", "r").read().split('\n')]

maxsteps = 64

start = find_start(my_map)
do_steps(start, 0)

count = 0
for line in my_map:
	for c in line:
		if type(c) is int and int(c) % 2 == 0:
			count += 1

print(count)
