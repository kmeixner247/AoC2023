def christmas_hash(symbol):
	current_value = 0
	for c in symbol:
		current_value += ord(c)
		current_value *= 17
		current_value %= 256
	return current_value

def focusing_power(boxidx, focal_length, idx):
	return (1 + boxidx) * (idx + 1) * int(focal_length)

def total_focusing_power(boxes):
	total = 0
	for boxidx in range(len(boxes)):
		for idx, item in enumerate(boxes[boxidx].items()):
			total += focusing_power(boxidx, item[1], idx)
	print(total)

symbols = open("input", "r").read().split(',')

boxes = [dict() for i in range(256)]

for symbol in symbols:
	if '-' in symbol:
		lense = symbol[:-1]
		lense_hash = christmas_hash(lense)
		if lense in boxes[lense_hash]:
			# boxes[lense_hash].remove(lense)
			del boxes[lense_hash][lense]
	else:
		lense = symbol.split('=')
		lense_hash = christmas_hash(lense[0])
		boxes[lense_hash].update({lense[0] : lense[1]})

# for box in boxes:
# 	print(box)
total_focusing_power(boxes)

