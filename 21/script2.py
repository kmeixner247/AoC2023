# not pretty but it works. 
# I realized that the step number is exactly 202300 * 131 + 65, 
# which will get you exactly to the corner of the 202300th copy of the map in each direction.
# After scribbling around a bit I realized that any iteration of this problem that reaches the exact end
# in every direction is composed of the exact same map tile results, just different numbers of them.
# so I calculate the simplest case (5x5 tiles) that has all the result types and then interpolated that
# I was actually a bit surprised when it worked

import copy
def find_start(my_map):
	for y in range(len(my_map)):
		for x in range(len(my_map[y])):
			if my_map[y][x] == "S":
				return (y, x)

def do_steps(start, depth, max):
	global my_map
	if depth > max:
		return
	(y, x) = start
	if y < 0 or x < 0 or y >= len(my_map) or x >= len(my_map[y]) or my_map[y][x] == "#":
		return
	if my_map[y][x] == "S" or my_map[y][x] == ".":
		my_map[y][x] = depth
	else:
		if depth >= my_map[y][x]:
			return
		my_map[y][x] = depth
	do_steps((y - 1, x), depth + 1, max)
	do_steps((y + 1, x), depth + 1, max)
	do_steps((y, x - 1), depth + 1, max)
	do_steps((y, x + 1), depth + 1, max)

def count_section(my_map, y, x, size):
	count = 0
	for iy in range(y, y + size):
		for ix in range(x, x + size):
			c = my_map[iy][ix]
			if type(c) is int and int(c) % 2 == 1:
				count += 1
	return count

def count_sections(my_map, maplen):
	sections = []
	for i in range(5):
		section = []
		for j in range(5):
			section.append(count_section(my_map, i * maplen, j * maplen, maplen))
		sections.append(section)
	return sections

def gardens_reached(steps, smallresult, maplen):
	n = int(steps / maplen)
	result = 0
	result += n * n * smallresult[2][3]
	result += (n - 1) * (n - 1) * smallresult[2][2]
	result += n * smallresult[0][1]
	result += n * smallresult[0][3]
	result += n * smallresult[3][0]
	result += n * smallresult[3][4]
	result += (n - 1) * smallresult[1][1]
	result += (n - 1) * smallresult[1][3]
	result += (n - 1) * smallresult[3][1]
	result += (n - 1) * smallresult[3][3]
	result += smallresult[0][2]
	result += smallresult[2][0]
	result += smallresult[2][4]
	result += smallresult[4][2]
	return(result)


my_map = [[c for c in line] for line in open("input", "r").read().split('\n')]
maplen = len(my_map)
maxsteps = 26501365
rest = maxsteps % maplen
small_maxsteps = 2 * maplen + rest

start = find_start(my_map)

my_map[start[0]][start[1]] = '.'

for y in range(maplen):
	my_map[y] += copy.deepcopy(my_map[y]) + copy.deepcopy(my_map[y]) + copy.deepcopy(my_map[y]) + copy.deepcopy(my_map[y])
my_map += copy.deepcopy(my_map) + copy.deepcopy(my_map) + copy.deepcopy(my_map) + copy.deepcopy(my_map)
start = (int(len(my_map)/2), int(len(my_map)/2))

do_steps(start, 0, small_maxsteps)
sections = (count_sections(my_map, maplen))

print(gardens_reached(maxsteps, sections, maplen))
