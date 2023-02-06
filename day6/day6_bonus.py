# Day 6 info here https://adventofcode.com/2022/day/6
# How many characters need to be processed before the first start-of-message marker is detected?

with open('day6/test_input.txt') as file:
	line = file.readline()
	packet = []
	progress = 0

	for letter_num in range(0, len(line)):
		packet.append(line[letter_num])
		if (len(packet) > 4):
			packet.pop(0)

		progress += 1
		if (len(packet) == 4):
			not_matching = True
			for i, letter in enumerate(packet):
				for j in range(len(packet)):
					if (i == j):
						continue
					elif (letter == packet[j]):
						not_matching = False

			if (not_matching):
				print('Packet is', packet)
				print('Progress is', progress)
				break
