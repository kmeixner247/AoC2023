import collections

patterns = [[line for line in pattern.split('\n')] for pattern in open("input", "r").read().split("\n\n")]

def check_pattern(pattern):
	for idx in range(len(pattern) - 1):
		low = idx
		high = idx + 1
		while pattern[low] == pattern[high]:
			if low == 0 or high == len(pattern) - 1:
				return idx + 1
			low -= 1
			high += 1
	return 0

summarized = 0

for pattern in patterns:
	summarized += check_pattern(list(zip(*pattern[::-1])))
	summarized += check_pattern(pattern) * 100

print(summarized)
	