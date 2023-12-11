import itertools

universe = [[c for c in line] for line in open("input", "r").read().split('\n')]

empty_columns = []
empty_rows = []
for x in range(len(universe[0])):
	if all(universe[y][x] == "." for y in range(len(universe))):
		empty_columns.append(x)

for y in range(len(universe)):
	if all(c == "." for c in universe[y]):
		empty_rows.append(y)

galaxies = []

for y in range(len(universe)):
	for x, xel in enumerate(universe[y]):
		if xel == "#":
			galaxies.append((y, x))

distances = 0

for tpl in (list(itertools.combinations(range(len(galaxies)), 2))):
	galaxy1 = galaxies[tpl[0]]
	galaxy2 = galaxies[tpl[1]]
	distance = abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])
	for col in empty_columns:
		if (col > galaxy1[1] and col < galaxy2[1]) or (col > galaxy2[1] and col < galaxy1[1]):
			distance += 999999
	for row in empty_rows:
		if (row > galaxy1[0] and row < galaxy2[0]) or (row > galaxy2[0] and row < galaxy1[0]):
			distance += 999999
	distances += distance

print(distances)
