# Day 1 info here https://adventofcode.com/2022/day/1
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

count_limit = 3
all_counts = []

with open('day1/input.txt') as file:
	all_lines = file.readlines()
	current_count = 0

	for line in all_lines:
		if line.strip():
			current_count += int(line)
		else:
			all_counts.append(current_count)
			current_count = 0

highest_count = sum(sorted(all_counts)[-3:])

print('Top three is', highest_count)
