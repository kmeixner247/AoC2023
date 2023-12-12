import re
import functools

# oof this one was tough, functools be blessed

@functools.cache
def evaluate(line, groups):
	count = 0

	# if all the groups have been 'exhausted', any # left in the string means it's invalid, otherwise valid
	if len(groups) == 0:
		return 0 if "#" in line else 1
		
	# . at the beginning can be ignored
	if line.startswith('.'):
		return count + evaluate(line[1:], groups)

	# for ? at the beginning try both . and #
	elif line.startswith('?'):
		return count + evaluate('.' + line[1:], groups) + evaluate('#' + line[1:], groups)

	# only # possible for first character now
	else:
		first_section = line.split(".")[0]

		# e.g. #?#.# 4,.. is not possible because the first group can be max 3
		if len(first_section) < groups[0]:
			return 0

		# e.g. #?#.# 3,.. the first section can only be the #?# as ### - a . would mean #.#.# which would start with 1
		if len(first_section) == groups[0]:
			return count + evaluate(line[len(first_section):], groups[1:])
		first_continuous_group = first_section.split("?")[0]

		# e.g. ####?.# 3,.. first group would have to be a 4 atleast, so it's invalid
		if len(first_continuous_group) > groups[0]:
			return 0

		# now we replace the first questionmark with both and keep recursioningifying
		first_questionmark = line.find("?")
		return count + evaluate(line[:first_questionmark] + "." + line[first_questionmark+1:], groups) + evaluate(line[:first_questionmark] + "#" + line[first_questionmark+1:], groups)


lines = [l.split() for l in open("input", "r").read().split("\n")]

for i in range(len(lines)):
	lines[i][0] += ("?" + lines[i][0]) * 4
	lines[i][1] += ("," + lines[i][1]) * 4
	lines[i][1] = [int(n) for n in re.findall(r"\d+", lines[i][1])]
	lines[i][1] = tuple(lines[i][1])

print(sum([evaluate(line[0], line[1]) for line in lines]))