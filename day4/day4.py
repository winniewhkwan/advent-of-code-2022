# Day 4 info here https://adventofcode.com/2022/day/4
# In how many assignment pairs does one range fully contain the other?

import re

with open('day4/input.txt') as file:
	all_lines = file.readlines()
	totalContainedPairs = 0

	for line in all_lines:
		range_array = [int(num) for num in re.split(r'[,-]', line)]

		num_array1 = set(range(range_array[0], range_array[1] + 1))
		num_array2 = set(range(range_array[2], range_array[3] + 1))

		if num_array1.issubset(num_array2) or num_array2.issubset(num_array1):
				totalContainedPairs += 1

	print('Total contained pairs are', totalContainedPairs)
