# Day 2 info here https://adventofcode.com/2022/day/2
# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

from enum import Enum

class ResultGuide(Enum):
	LOSS = 'X'
	DRAW = 'Y'
	WIN = 'Z'

total_score = 0
with open('day2/input.txt') as file:
	all_lines = file.readlines()
	for line in all_lines:
		result = line.split()[1]
		current_score = 1

		match result:
			case ResultGuide.DRAW.value:
				current_score += 3
			case ResultGuide.WIN.value:
				current_score += 6

		total_score += current_score

print('Total score is', total_score)
# 7951 is wrong :(
