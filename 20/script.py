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

def push_button():
	global signals_sent
	global modules
	queue = [("broadcaster", False, "button")]
	while len(queue) > 0:
		signal = queue.pop(0)
		if signal[1] == True:
			signals_sent[1] += 1
		else:
			signals_sent[0] += 1
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
signals_sent = [0, 0]
for i in range(1000):
	push_button()
print(signals_sent)
print(signals_sent[0] * signals_sent[1])