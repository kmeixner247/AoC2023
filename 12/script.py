import re
import itertools

def check(line, combo):
	cpy = line[0].copy()
	for i in range(len(cpy)):
		if cpy[i] == '?':
			if i in combo:
				cpy[i] = '#'
			else:
				cpy[i] = '.'
	groups = [el for el in "".join(cpy).split(".") if len(el) > 0]
	if len(groups) != len(line[1]):
		return False
	for pair in zip(groups, line[1]):
		if len(pair[0]) != pair[1]:
			return False
	return True


def bruteforce(line):
	missing = sum(line[1]) - line[0].count("#")
	questionmarks = [i for i in range(len(line[0])) if line[0][i] == '?']
	count = 0
	for combo in list(itertools.combinations(questionmarks, missing)):
		if check(line, combo):
			count += 1
	return count


lines = [l.split() for l in open("smolinput", "r").read().split("\n")]

for i in range(len(lines)):
	lines[i][0] = [c for c in lines[i][0]]
	lines[i][1] = [int(n) for n in re.findall(r"\d+", lines[i][1])]

sum = sum([bruteforce(line) for line in lines])
print(sum)


