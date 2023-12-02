import re

with open("input", "r") as file:
    lines = file.read().split("\n")

games = [[[draw.strip(' ').split(' ') for draw in round.split(',')]
          for round in line.split(":")[1].lstrip().split(";")] for line in lines]

ids = list(range(1, len(games) + 1))

for idx, game in enumerate(games):
    for round in game:
        for draw in round:
            if (draw[1] == 'red' and int(draw[0]) > 12) or (draw[1] == 'green' and int(draw[0]) > 13) or (draw[1] == 'blue' and int(draw[0]) > 14):
                if idx + 1 in ids:
                    ids.remove(idx + 1)


print(sum(ids))
