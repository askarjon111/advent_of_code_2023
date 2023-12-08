"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters:
one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""


def identify_number(input):
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for num in numbers.keys():
        if num in input:
            return numbers.get(num)
    return None


with open('day_1/input.txt', 'r') as txt:
    summa = 0
    for line in txt:
        first_digit, last_digit = 0, 0
        for i in range(len(line)):
            if line[i].isdigit():
                if not first_digit:
                    first_digit = int(line[i])
                else:
                    last_digit = int(line[i])

            elif identify_number(line[i:i+5]):
                if not first_digit:
                    first_digit = identify_number(line[i:i+5])
                else:
                    last_digit = identify_number(line[i:i+5])
        last_digit = first_digit if not last_digit else last_digit
        summa += (first_digit * 10) + last_digit
    print(summa)
