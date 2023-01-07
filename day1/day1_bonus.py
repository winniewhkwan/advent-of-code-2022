# Day 1 info here https://adventofcode.com/2022/day/1
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

count_limit = 3
highest_counts = []

with open('day1/test_input.txt') as file:
	all_lines = file.readlines()
	current_count = 0

	for line in all_lines:
		if line.strip():
			current_count += int(line)
		else:
			if (len(highest_counts) > count_limit):

				for i in range(0, len(highest_counts)):
					if current_count > highest_counts[i]:
						if (len(highest_counts) > count_limit):
							highest_counts.insert(i, current_count)
							highest_counts.pop()
						else:
							highest_counts.append(current_count)
						break

print('Top three is', highest_counts)
print('Highest number of calories being carried is', sum(highest_counts))