with open("input", "r") as file:
	lines = [[list(filter(None, set.split(' '))) for set in line.split(":")[1].split("|")] for line in file.read().split('\n')]

sum = 0

for line in lines:
	intersection = [num for num in line[0] if num in line[1]]
	if len(intersection) > 0:
		sum += 2 ** (len(intersection) - 1)

print(sum)