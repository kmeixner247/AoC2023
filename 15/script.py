def christmas_hash(symbol):
	current_value = 0
	for c in symbol:
		current_value += ord(c)
		current_value *= 17
		current_value %= 256
	return current_value

def test():
	testvalues = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")
	testresults = [30, 253, 97, 47, 14, 180, 9, 197, 48, 214, 231]

	for i in range(len(testvalues)):
		result = christmas_hash(testvalues[i])
		assert result == testresults[i], f"wrong hash value for '{testvalues[i]}' - expected {testresults[i]}, got {result}"

	print("Passed all tests!")

symbols = open("input", "r").read().split(',')

results = [christmas_hash(symbol) for symbol in symbols]
print(sum(results))
