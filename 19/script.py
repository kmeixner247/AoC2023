import re

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

[instructions_raw, parts_raw] = [part.split('\n') for part in open("input", "r").read().split("\n\n")]


instructions = {}
for line in instructions_raw:
	[name, remainder] = line.split('{')
	remainder = remainder[:-1]
	cases = [case.split(":") for case in remainder.split(',')]
	instructions.update({name: cases})

parts = [{"x" : numbers[0],"m": numbers[1], "a": numbers[2], "s": numbers[3]}for numbers in [[int(n) for n in re.findall(r"\d+", object_raw)] for object_raw in parts_raw]]

total = 0
for part in parts:
	result = check_part_for_condition(part, instructions["in"])
	while result != "A" and result != "R":
		result = check_part_for_condition(part, instructions[result])
	if result == "A":
		total += (sum(part.values()))
		
print(total)