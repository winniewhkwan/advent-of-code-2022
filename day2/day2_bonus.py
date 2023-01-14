# Day 2 info here https://adventofcode.com/2022/day/2
# Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

from enum import Enum

class OptionGuide(Enum):
	A = 1 # Rock
	B = 2 # Paper
	C = 3 # Scissors

class ResultGuide(Enum):
	LOSS = 0,
	DRAW = 1,
	WIN = 2

class ResultMap(Enum):
	A = ['B', 'A', 'C']
	B = ['C', 'B', 'A']
	C = ['A', 'C', 'B']

def get_outcome(opponent_choice, result):
	player_options = ResultMap[opponent_choice].value
	player_choice = player_options[result]
	return OptionGuide[player_choice].value

total_score = 0
with open('day2/test_input.txt') as file:
	all_lines = file.readlines()
	for line in all_lines:
		opponent, result = line.split()
		current_score = 0

		match result:
			case 'X': # Lose
				current_score = 0 + get_outcome(opponent, 0)
			case 'Y': # Draw
				current_score = 3 + get_outcome(opponent, 1)
			case 'Z': # Win
				current_score = 6 + get_outcome(opponent, 2)

		total_score += current_score

print('Total score is', total_score)
# 7951 is wrong :(
