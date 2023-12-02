import re

with open("input", "r") as file:
    data = file.read()
    lines = data.split('\n')

sum = 0

for line in lines:
    numbers = re.findall(r'\d|three', line)
    calibration_value = numbers[0] + numbers[-1]
    print(int(calibration_value))
    sum += int(calibration_value)

print(sum)
