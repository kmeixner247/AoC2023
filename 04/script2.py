with open("input", "r") as file:
	lines = [[list(filter(None, set.split(' '))) for set in line.split(":")[1].split("|")] for line in file.read().split('\n')]

copies = [1] * len(lines)

for idx, line in enumerate(lines):
	intersection = [num for num in line[0] if num in line[1]]
	for i in range(0, len(intersection)):
		if (idx < len(copies)):
			copies[idx + i + 1] += copies[idx]

print(sum(copies))