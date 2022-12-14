# Day 3 info here https://adventofcode.com/2022/day/3
# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

with open('day3/input.txt') as file:
	sameItemTypeTotal = 0
	allLines = file.readlines()

	for line in allLines:
		# Split text in half
		pocketOne = line[:len(line)//2]
		pocketTwo = line[len(line)//2:]

		for item in pocketOne:
			if item in pocketTwo:
				if (item.islower()):
					# Use ascii to determine priority number for the item
					sameItemTypeTotal += ord(item) - 96
				else:
					sameItemTypeTotal += ord(item) - 38
				# Leave loop after similar item has been discovered
				break
	print('The sum of the item priorities is', sameItemTypeTotal)
