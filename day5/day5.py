# Day 5 info here https://adventofcode.com/2022/day/5
# After the rearrangement procedure completes, what crate ends up on top of each stack?

import re
from itertools import islice

numStacks = 9

with open('day5/input.txt') as file:
	allLines = file.readlines()
	stacks = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

	allCrates = islice(allLines, 8)
	for unsortedCrates in allCrates:
		cratesArray = [ unsortedCrates[i : i + 4] for i in range(0, len(unsortedCrates), 4) ]

		# DON'T USE ZIP
		for crate, stack in zip(cratesArray, stacks):
			letter = re.sub(r'[][\n ]', '', crate)
			if letter != '':
				print(letter, stack)
				stack = stack + letter
	print(stacks)


	# movements = islice(allLines, 10, None)
	# for move in movements:
	# 	print(move)

