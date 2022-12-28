# Day 5 info here https://adventofcode.com/2022/day/5
# After the rearrangement procedure completes, what crate ends up on top of each stack?

import re
from itertools import islice

numStacks = 9

with open('day5/input.txt') as file:
	allLines = file.readlines()
	stacks = [''] * 9

	allCrates = islice(allLines, 8)
	for unsortedCrates in allCrates:
		unsortedCratesArray = [ unsortedCrates[i : i + 4] for i in range(0, len(unsortedCrates), 4) ]

		for i, crate in enumerate(unsortedCratesArray):
			stacks[i] += re.sub(r'[][\n ]', '', crate)

	movements = islice(allLines, 10, None)
	for move in movements:
		moveInfo = re.sub(r'[a-z]', '', move).split()
		for i in range(0, int(moveInfo[0])):
			startStackNum, endStackNum = int(moveInfo[1]) - 1, int(moveInfo[2]) - 1
			letter = stacks[startStackNum][0]
			stacks[startStackNum] = stacks[startStackNum][1:]
			stacks[endStackNum] = letter + stacks[endStackNum]

	topCrates = ''
	for stack in stacks:
		topCrates += stack[0]
	print(topCrates)
