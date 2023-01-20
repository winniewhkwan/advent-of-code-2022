# Day 4 info here https://adventofcode.com/2022/day/4
# In how many assignment pairs do the ranges overlap?

import re

with open('day4/test_input.txt') as file:
	all_lines = file.readlines()
	total_overlaps = 0

	for line in all_lines:
		num_array = [int(num) for num in re.split(r'[,-]', line)]
		# [2-8,3-7]
		#  0,1,2,3

		# if [0] is within [2] and [3]
		# or if [1] is within [2] and [3]
		# or [2] is within [0] and [1]
		# or [3] is within [0] and [1]
		# Also find a more interesting (better) way to solve this

		if num_array[0] >= num_array[2] and num_array[0] <= num_array[3]\
			or num_array[1] >= num_array[2] and num_array[1] <= num_array[3]:
			total_overlaps += 1

		# if num_array[0] >= num_array[2] and num_array[1] <= num_array[3]\
		# 	or num_array[0] <= num_array[2] and num_array[1] >= num_array[3]:
		# 		total_overlaps += 1

	print('Total overlaps are', total_overlaps)
