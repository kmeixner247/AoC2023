lines = open("input", "r").read().split("\n")

instructions = lines[0]

myMap = {}

for line in lines[2:]:
	nodes = [c.strip("(),") for c in line.split()]
	myMap.update({ nodes[0] : {"L" : nodes[-2], "R" : nodes[-1]}})

steps = 0
node = "AAA"
while node != "ZZZ":
	for c in instructions:
		node = myMap[node][c]
		steps += 1
		if node == "ZZZ":
			break

print(steps)