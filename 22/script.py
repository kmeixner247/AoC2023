# takes a few minutes to run. But hey, it works

import functools
import copy

def fall(bricks, i):
	while(not is_brick_supported(bricks[i], bricks[:i])):
		for idx in range(len(bricks[i])):
			bricks[i][idx][2] -= 1

def is_brick_supported(brick, bricks):
	if lowest_z(brick) > 1 and all(not is_coord_supported(coord, bricks) for coord in brick):
		return False
	return True

def is_coord_supported(coord, bricks):
	supporting_coord = [coord[0], coord[1], coord[2] - 1]
	for brick in bricks:
		if supporting_coord in brick:
			return True
	return False

def lowest_z(a):
	z = a[0][2]
	for coord in a:
		if coord[2] < z:
			z = coord
	return z

def compare(a, b):
	if lowest_z(a) > lowest_z(b):
		return 1
	if lowest_z(a) < lowest_z(b):
		return -1
	return 0

def find_unsupported_brick(bricks):
	for idx, brick in enumerate(bricks):
		if lowest_z(brick) > 1 and all(not is_coord_supported(coord, bricks[:idx]) for coord in brick):
			return idx
	return -1


lines = open("input", "r").read().split("\n")

bricks = list()


for line in lines:
	bounds = [[int(n) for n in bound.split(',')] for bound in line.split('~')]
	brick = list()
	for x in range(bounds[0][0], bounds[1][0] + 1):
		for y in range(bounds[0][1], bounds[1][1] + 1):
			for z in range(bounds[0][2], bounds[1][2] + 1):
				brick.append([x, y, z])
	bricks.append(brick)

bricks = sorted(bricks, key = functools.cmp_to_key(compare))

first_unsupported = find_unsupported_brick(bricks)

while first_unsupported != -1:
	fall(bricks, first_unsupported)
	first_unsupported = find_unsupported_brick(bricks)

count = 0
for i in range(len(bricks)):
	bricks_copy = copy.deepcopy(bricks)
	bricks_copy.pop(i)
	if find_unsupported_brick(bricks_copy) == -1:
		count += 1

print(count)