import math

lines = open("input", "r").read().split("\n")

instructions = lines[0]

myMap = {}

for line in lines[2:]:
	nodes = [c.strip("(),") for c in line.split()]
	myMap.update({ nodes[0] : {"L" : nodes[-2], "R" : nodes[-1]}})

nodes = [node for node in myMap if node.endswith("A")]

allSteps = []

for node in nodes:
	steps = 0
	while not node.endswith("Z"):
		for c in instructions:
			node = myMap[node][c]
			steps += 1
			if node.endswith("Z"):
				break
	allSteps.append(steps)

print(math.lcm(*allSteps))