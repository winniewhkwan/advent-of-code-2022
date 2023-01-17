# Day 3 info here https://adventofcode.com/2022/day/3
# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

with open('day3/input.txt') as file:
	badge_total = 0
	all_lines = file.readlines()

	current_group = []
	for line in all_lines:
		current_group.append(line)
		if len(current_group) == 3:
			pack1, pack2, pack3 = current_group

			for item_type in pack1:
				if item_type in pack2 and item_type in pack3:
					if (item_type.islower()):
						# Use ascii to determine priority number for the item
						badge_total += ord(item_type) - 96
					else:
						badge_total += ord(item_type) - 38
					break
			current_group = []
	print('The sum of the group priorities is', badge_total)
