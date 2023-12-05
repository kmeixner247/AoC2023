import re

def parse_map(block):
	blocklines = block.split('\n')
	return [[int(n) for n in blocklines[i].split()] for i in range(1, len(blocklines))]
	

def find_in_map(n, map):
	for line in map:
		if n >= line[1] and n < line[1] + line[2]:
				return line[0] + (n - line[1])
	return n

def find_location(n, maps):
	for m in maps:
		n = find_in_map(n, m)
	return n

with open("input", "r") as file:
	blocks = file.read().split('\n\n')

initial = [int(c) for c in re.findall(r'\d+', blocks[0])]

maps = [parse_map(blocks[i]) for i in range(1, len(blocks))]

locations = [find_location(n, maps) for n in initial]

print((min(locations)))