# Day 4 info here https://adventofcode.com/2022/day/4
# In how many assignment pairs do the ranges overlap?

import re

with open('day4/input.txt') as file:
	all_lines = file.readlines()
	total_overlaps = 0

	for line in all_lines:
		range_array = [int(num) for num in re.split(r'[,-]', line)]

		num_array1 = set(range(range_array[0], range_array[1] + 1))
		num_array2 = set(range(range_array[2], range_array[3] + 1))

		if num_array1.intersection(num_array2):
			total_overlaps += 1

	print('Total overlaps are', total_overlaps)
