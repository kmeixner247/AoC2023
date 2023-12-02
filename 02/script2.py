import re

with open("input", "r") as file:
    lines = file.read().split("\n")

games = [[[draw.strip(' ').split(' ') for draw in round.split(',')]
          for round in line.split(":")[1].lstrip().split(";")] for line in lines]

powers = []

for game in games:
    min  = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for round in game:
        for draw in round:
            if int(draw[0]) > min[draw[1]]:
                min[draw[1]] = int(draw[0])
    powers.append(min['red'] * min['green'] * min['blue'])


print(sum(powers))