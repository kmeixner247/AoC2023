import sys

sys.setrecursionlimit(5000)

def enum_dir(dir):
	if dir[0] == 1:
		return 1
	if dir[0] == -1:
		return 1 << 1
	if dir[1] == 1:
		return 1 << 2
	if dir[1] == -1:
		return 1 << 3
	
def down(pos):
	propagate((pos[0] + 1, pos[1]), (1, 0))

def up(pos):
	propagate((pos[0] - 1, pos[1]), (-1, 0))

def right(pos):
	propagate((pos[0], pos[1] + 1), (0, 1))

def left(pos):
	propagate((pos[0], pos[1] - 1), (0, -1))


def propagate(pos, dir):
	global map
	global energymap
	if pos[0] < 0 or pos[0] >= len(map) or pos[1] < 0 or pos[1] >= len(map[0]):
		return
	dirnum = enum_dir(dir)
	if energymap[pos[0]][pos[1]] & dirnum:
		return
	energymap[pos[0]][pos[1]] += dirnum
	new_symbol = map[pos[0]][pos[1]]
	if new_symbol == '.':
		propagate((pos[0] + dir[0], pos[1] + dir[1]), dir)
	elif new_symbol == '/':
		if dirnum == 1:
			left(pos)
		elif dirnum == 2:
			right(pos)
		elif dirnum == 4:
			up(pos)
		elif dirnum == 8:
			down(pos)
	elif new_symbol == '\\':
		if dirnum == 1:
			right(pos)
		elif dirnum == 2:
			left(pos)
		elif dirnum == 4:
			down(pos)
		elif dirnum == 8:
			up(pos)
	elif new_symbol == '-':
		if dir[0] == 0:
			propagate((pos[0] + dir[0], pos[1] + dir[1]), dir)
		else:
			left(pos)
			right(pos)
	elif new_symbol == '|':
		if dir[1] == 0:
			propagate((pos[0] + dir[0], pos[1] + dir[1]), dir)
		else:
			down(pos)
			up(pos)

map = [[c for c in line] for line in open("input", "r").read().split('\n')]
energymap = [[0 for c in line] for line in map]

propagate((0,0), (0,1))
total = 0
for line in energymap:
	for c in line:
		if c > 0:
			total += 1

print(total)
