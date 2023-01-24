# Day 4 info here https://adventofcode.com/2022/day/4
# In how many assignment pairs do the ranges overlap?

import re

with open('day4/input.txt') as file:
	all_lines = file.readlines()
	total_overlaps = 0

	for line in all_lines:
		num_array = [int(num) for num in re.split(r'[,-]', line)]

		# Also find a more interesting (better) way to solve this

		if num_array[0] >= num_array[2] and num_array[0] <= num_array[3]\
			or num_array[1] >= num_array[2] and num_array[1] <= num_array[3]\
			or num_array[2] >= num_array[0] and num_array[2] <= num_array[1]\
			or num_array[3] >= num_array[0] and num_array[3] <= num_array[1]:
			total_overlaps += 1

	print('Total overlaps are', total_overlaps)
