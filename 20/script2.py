# This one involved some manual work. 
# I figured out that rx has exactly one conjunction module as input,
# which again has 4 conjunction modules as input.
# so I assumed that all 4 of those restart their entire cycle once they output high
# which means that the first time they all output high is their LCM
# which in this case is simple their multiple

class Module:
	def __init__(self, lst):
		self.outputs = list()
		for item in lst:
			self.outputs.append(item)

class FlipFlopModule(Module):
	def __str__(self):
		return (f"Flip Flop Module - outputs: {self.outputs}; is_on: {self.is_on}")

	def __init__(self, lst):
		self.is_on = False
		super().__init__(lst)

	def switch(self):
		self.is_on = not self.is_on

class ConjunctionModule(Module):
	def __str__(self):
		return (f"Conjunction Module - inputs: {self.inputs}; outputs: {self.outputs}")
	def __init__(self, lst):
		self.inputs = dict()
		super().__init__(lst)

def push_button(partial_results):
	global pushes
	global modules
	pushes += 1
	queue = [("broadcaster", False, "button")]
	while len(queue) > 0:
		signal = queue.pop(0)
		if signal[1] == True and signal[2] in partial_results and partial_results[signal[2]] == 0:
			partial_results[signal[2]] = pushes
			print(f"found {signal[2]}")
		targets = []
		if signal[0] in modules:
			module = modules[signal[0]]
			if type(module) is FlipFlopModule:
				if signal[1] == False:
					out_signal = not module.is_on
					module.switch()
					targets = module.outputs.copy()
			elif type(module) is ConjunctionModule:
				module.inputs.update({signal[2] : signal[1]})
				if all(pair[1] == True for pair in module.inputs.items()):
					out_signal = False
				else:
					out_signal = True
				targets = module.outputs.copy()
			else:
				out_signal = False
				targets = module.outputs.copy()
			for item in targets:
				queue.append((item, out_signal, signal[0]))

lines = [line.split(" -> ") for line in open("input", "r").read().split("\n")]

modules = dict()

for line in lines:
	if line[0].startswith('%'):
		modules.update({line[0][1:] : FlipFlopModule(line[1].split(', '))})
	elif line[0].startswith('&'):
		modules.update({line[0][1:] : ConjunctionModule(line[1].split(', '))})
	else:
		modules.update({line[0] : Module(line[1].split(', '))})

for module in modules.items():
	for item in module[1].outputs:
		if item in modules:
			if type(modules[item]) is ConjunctionModule:
				modules[item].inputs.update({module[0] : False})

partial_results = {"ft" : 0, "jz": 0, "sv": 0, "ng": 0}

pushes = 0

while (any(pair[1] == 0 for pair in partial_results.items())):
	push_button(partial_results)

result = 1
for item in partial_results.items():
	result *= item[1]

print(result)