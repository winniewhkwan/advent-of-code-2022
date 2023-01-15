# Day 3 info here https://adventofcode.com/2022/day/3
# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?

with open('day3/test_input.txt') as file:
	sameItemTypeTotal = 0
	allLines = file.readlines()

	# Need to group lines by 3
	# Find common type between lines and store
	# Find priority number and get total

	for line in allLines:
		# Split text in half - the '//' divides the number and rounds down
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
