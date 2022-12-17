# Day 4 info here https://adventofcode.com/2022/day/4
# In how many assignment pairs does one range fully contain the other?

import re

with open('day4/input.txt') as file:
	allLines = file.readlines()
	totalContainedPairs = 0

	for line in allLines:
		numArray = [int(num) for num in re.split(r'[,-]', line)]

		if numArray[0] >= numArray[2] and numArray[1] <= numArray[3]\
			or numArray[0] <= numArray[2] and numArray[1] >= numArray[3]:
				totalContainedPairs += 1

	print('Total contained pairs are', totalContainedPairs)
