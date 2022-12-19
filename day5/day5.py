# Day 5 info here https://adventofcode.com/2022/day/5
# After the rearrangement procedure completes, what crate ends up on top of each stack?

numStacks = 9

with open('day5/input.txt') as file:
	allLines = file.readlines()
	stacks = [[]] * 9

	for i, line in enumerate(allLines):
		if (i < 8):
			unsortedCrates = [ line[i : i + 4] for i in range(0, len(line), 4) ]
			for i, crate in enumerate(unsortedCrates):
				print(i, crate)

