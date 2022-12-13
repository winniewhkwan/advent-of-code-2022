# Day 2 info here https://adventofcode.com/2022/day/2
# What would your total score be if everything goes exactly according to your strategy guide?

from enum import Enum

class ResultGuide(Enum):
	LOSS = 0
	DRAW = 3
	WIN = 6

class OptionGuide(Enum):
	A = 1 # Rock
	B = 2 # Paper
	C = 3 # Scissors
	X = 1 # Rock
	Y = 2 # Paper
	Z = 3 # Scissors

totalScore = 0
with open('day2/input.txt') as file:
	allLines = file.readlines()
	for line in allLines:
		opponent = OptionGuide[line.split()[0]].value
		player = currentScore = OptionGuide[line.split()[1]].value
		if opponent == player:
			currentScore += ResultGuide.DRAW.value
		elif player == OptionGuide.X.value and opponent == OptionGuide.C.value\
			or player == OptionGuide.Y.value and opponent == OptionGuide.A.value\
			or player == OptionGuide.Z.value and opponent == OptionGuide.B.value:
				currentScore += ResultGuide.WIN.value
		totalScore += currentScore

print('Total score is', totalScore)
