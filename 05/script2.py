import re

def parse_map(block):
	blocklines = block.split('\n')
	return [[int(n) for n in blocklines[i].split()] for i in range(1, len(blocklines))]
	
def is_in_ranges(n, ranges):
	for range in ranges:
		if n >= range[0] and n < range[1]:
			return True
	return False

def find_reverse_in_map(n, map):
	for line in map:
		if n >= line[0] and n < line[0] + line[2]:
			return line[1] + (n - line[0])
	return n

def reverse_traverse(n, maps):
	for m in list(reversed(maps)):
		n = find_reverse_in_map(n, m)
	return n

with open("input", "r") as file:
	blocks = file.read().split('\n\n')

initial = [int(c) for c in re.findall(r'\d+', blocks[0])]

maps = [parse_map(blocks[i]) for i in range(1, len(blocks))]

initialranges = [[initial[i], initial[i] + initial[i+1]] for i in range(0, len(initial), 2)]

n = 0
while (is_in_ranges(reverse_traverse(n, maps), initialranges) == False):
	n += 1

print(n)