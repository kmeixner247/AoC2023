import math
import re
import functools

def midnight(a,b,c):
	s1 = (-b + math.sqrt(b**2 - 4*(a*c))) / (2 * a)
	s2 = (-b - math.sqrt(b**2 - 4*(a*c))) / (2 * a)
	return [s1, s2]

data = [re.findall(r'\d+',line) for line in open("input", "r").read().split('\n')]
races = zip(data[0], data[1])

options = []

for race in races:
	solutions = midnight(-1, int(race[0]), -int(race[1]))
	options.append(int(solutions[1] - int(solutions[0])))

print(functools.reduce(lambda a, b: a * b, options))

bigsolutions = midnight(-1, int(''.join(data[0])), -int(''.join(data[1])))

print(int(bigsolutions[1]) - int(bigsolutions[0]))
