# Day 5 info here https://adventofcode.com/2022/day/5
# After the rearrangement procedure completes, what crate ends up on top of each stack?

import re
from itertools import islice

num_stacks = 9
# num_stacks = 3

with open('day5/input.txt') as file:
	all_lines = file.readlines()
	stacks = [''] * num_stacks # Top crates are the first letter

	all_crates = islice(all_lines, 8)
	# all_crates = islice(all_lines, 3)
	for unsorted_crates in all_crates:
		unsorted_crates_array = [ unsorted_crates[i : i + 4] for i in range(0, len(unsorted_crates), 4) ]

		for i, crate in enumerate(unsorted_crates_array):
			stacks[i] += re.sub(r'[][\n ]', '', crate)

	movements = islice(all_lines, 10, None)
	# movements = islice(all_lines, 5, None)
	for move in movements:
		move_info = re.sub(r'[a-z]', '', move).split() # move example - [move 1 from 2 to 1]

		stack_move_amt, start_stack_num, end_stack_num = \
			int(move_info[0]), int(move_info[1]) - 1, int(move_info[2]) - 1
		move_stack = stacks[start_stack_num][0:stack_move_amt]
		stacks[start_stack_num] = stacks[start_stack_num][stack_move_amt:]
		stacks[end_stack_num] = move_stack + stacks[end_stack_num]

	top_crates = ''
	for stack in stacks:
		top_crates += stack[0]

	print(top_crates)
	# Answer for test input is MCD
