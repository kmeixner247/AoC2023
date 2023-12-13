import collections

patterns = [[line for line in pattern.split('\n')] for pattern in open("input", "r").read().split("\n\n")]

def check_pattern(pattern):
	mirrorthingies = []
	for idx in range(len(pattern) - 1):
		low = idx
		high = idx + 1
		while pattern[low] == pattern[high]:
			if low == 0 or high == len(pattern) - 1:
				mirrorthingies.append(idx + 1)
				break
			low -= 1
			high += 1
	return mirrorthingies

def fix(pattern):
	before = check_pattern(pattern)
	before_vert = check_pattern(list(zip(*pattern[::-1])))
	for y in range(len(pattern)):
		for x in range(len(pattern[y])):
			patterncpy = pattern.copy()
			if patterncpy[y][x] == "#":
				patterncpy[y] = patterncpy[y][:x] + "." + patterncpy[y][x + 1:]
			else:
				patterncpy[y] = patterncpy[y][:x] + "#" + patterncpy[y][x + 1:]
			after = check_pattern(patterncpy)
			after_vert = check_pattern(list(zip(*patterncpy[::-1])))
			for n in after:
				if not n in before:
					return n * 100
			for n in after_vert:
				if not n in before_vert:
					return n
	return 0


summarized = 0

for pattern in patterns:
	summarized += fix(pattern)

print(summarized)