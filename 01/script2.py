import re

def get_lines(filename):
    with open(filename, "r") as file:
        data = file.read()
        lines = data.split('\n')
    return lines

def turn_to_digits(array):
    numdict = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    for idx, el in enumerate(array):
        if el in numdict:
            array[idx] = numdict[el]


lines = get_lines("input")
sum = 0
for line in lines:
    numbers = re.findall(
        r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    turn_to_digits(numbers[1::-1])
    
    calibration_value = numbers[0] + numbers[-1]
    sum += int(calibration_value)

print(sum)
