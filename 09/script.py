import re

def find_next_number(array):
	arrays = [array]
	while any(x != 0 for x in arrays[-1]):
		arrays.append([arrays[-1][idx] - arrays[-1][idx - 1] for idx in range(1, len(arrays[-1]))])
	arrays[-1].insert(0, 0)
	arrays[-1].append(0)
	i = len(arrays) - 2
	while i >= 0:
		arrays[i].insert(0, arrays[i][0] - arrays[i+1][0])
		arrays[i].append(arrays[i][-1] + arrays[i+1][-1])
		i -= 1
	return (arrays[0][0], arrays[0][-1])

lines = [[int(n) for n in re.findall(r"-?\d+", line)] for line in open("input", "r").read().split("\n")]

extrapolated_values = [find_next_number(line) for line in lines]
previous_values = [tp[0] for tp in extrapolated_values]
after_values = [tp[1] for tp in extrapolated_values]

print(sum(previous_values))
print(sum(after_values))