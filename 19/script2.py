import re

def reverse_condition(condition):
	if ">" in condition[0]:
		[symbol, value] = condition[0].split(">")
		value = str(int(value) + 1)
		return "<".join([symbol, value])
	elif "<" in condition[0]:
		[symbol, value] = condition[0].split("<")
		value = str(int(value) - 1)
		return ">".join([symbol, value])
	print("this should never print")

def check_part_for_condition(part, conditions):
	for condition in conditions:
		if len(condition) == 1:
			return condition[0]
		elif ">" in condition[0]:
			[attribute, value] = condition[0].split(">")
			if part[attribute] > int(value):
				return condition[1]
		elif "<" in condition[0]:
			[attribute, value] = condition[0].split("<")
			if part[attribute] < int(value):
				return condition[1]
	print("this should never print")

def traverse_instructions(cases, path):
	global instructions
	global finalpaths
	for case in cases:
		if len(case) == 2:
			if case[1] == "R" or case[1] == "A":
				if case[1] == "A":
					finalpaths.append(path + case)
				# return
			else:
				traverse_instructions(instructions[case[1]], path + [case[0]])
			path.append(reverse_condition(case))
		else:
			if case[0] == "R" or case[0] == "A":
				if case[0] == "A":
					finalpaths.append(path + case)
				return
			traverse_instructions(instructions[case[0]], path)



[instructions_raw, parts_raw] = [part.split('\n') for part in open("input", "r").read().split("\n\n")]


instructions = {}
for line in instructions_raw:
	[name, remainder] = line.split('{')
	remainder = remainder[:-1]
	cases = [case.split(":") for case in remainder.split(',')]
	instructions.update({name: cases})

parts = [{"x" : numbers[0],"m": numbers[1], "a": numbers[2], "s": numbers[3]}for numbers in [[int(n) for n in re.findall(r"\d+", object_raw)] for object_raw in parts_raw]]

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