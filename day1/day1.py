# Day 1 info here https://adventofcode.com/2022/day/1
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

highestCount = 0
with open('day1/input.txt') as file:
	allLines = file.readlines()
	currentCount = 0

	for line in allLines:
		if line.strip():
			currentCount += int(line)
		else:
			if currentCount > highestCount:
				highestCount = currentCount
			currentCount = 0

print('Highest number of calories being carried is', highestCount)