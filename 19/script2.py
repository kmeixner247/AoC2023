def reverse_condition(condition):
	if ">" in condition[0]:
		[symbol, value] = condition[0].split(">")
		value = str(int(value) + 1)
		return "<".join([symbol, value])
	elif "<" in condition[0]:
		[symbol, value] = condition[0].split("<")
		value = str(int(value) - 1)
		return ">".join([symbol, value])

def traverse_instructions(cases, path):
	global instructions
	global finalpaths
	for case in cases:
		if len(case) == 2:
			if case[1] == "R" or case[1] == "A":
				if case[1] == "A":
					finalpaths.append(path + case)
			else:
				traverse_instructions(instructions[case[1]], path + [case[0]])
			path.append(reverse_condition(case))
		else:
			if case[0] == "R" or case[0] == "A":
				if case[0] == "A":
					finalpaths.append(path + case)
				return
			traverse_instructions(instructions[case[0]], path)

instructions_raw = open("input", "r").read().split("\n\n")[0].split('\n')

instructions = {}
for line in instructions_raw:
	[name, remainder] = line.split('{')
	remainder = remainder[:-1]
	cases = [case.split(":") for case in remainder.split(',')]
	instructions.update({name: cases})

finalpaths = []

traverse_instructions(instructions["in"], [])

combos = 0

for path in finalpaths:
	finalranges = {"x" : [1, 4000], "m" : [1, 4000], "a" : [1, 4000], "s" : [1, 4000]}
	for condition in path[:-1]:
		if ">" in condition:
			[attribute, value] = condition.split(">")
			if int(value) + 1 > finalranges[attribute][0]:
				finalranges[attribute][0] = int(value) + 1
		if "<" in condition:
			[attribute, value] = condition.split("<")
			if int(value) - 1 < finalranges[attribute][1]:
				finalranges[attribute][1] = int(value) - 1
	localcombos = 1
	for i in finalranges.values():
		localcombos *= (i[1] - i[0] + 1)
	combos += localcombos

print(combos)