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
			if (len(highest_counts) < count_limit):
				is_added = False
				for i, num in enumerate(highest_counts):
					if current_count > num:
						highest_counts.insert(i, current_count)
						is_added = True
						break
				if (not(is_added)):
					highest_counts.append(current_count)
			else:
				for i in range(0, len(highest_counts)):
					if current_count > highest_counts[i]:
						highest_counts.insert(i, current_count)
						highest_counts.pop()
						break
			current_count = 0

print('Top three is', highest_counts)
print('Highest number of calories being carried is', sum(highest_counts))