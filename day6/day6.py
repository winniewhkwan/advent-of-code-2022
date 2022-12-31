# Day 6 info here https://adventofcode.com/2022/day/6
# How many characters need to be processed before the first start-of-packet marker is detected?

with open('day6/input.txt') as file:
  line = file.readline()
  packet = []
  progress = 0

  for letterNum in range(0, len(line)):
    packet.append(line[letterNum])
    if (len(packet) > 4):
      packet.pop(0)

    progress += 1
    if (len(packet) == 4):
      notMatching = True
      for i, letter in enumerate(packet):
        for j in range(len(packet)):
          if (i == j):
            continue
          elif (letter == packet[j]):
            notMatching = False

      if (notMatching):
        print('Packet is', packet)
        print('Progress is', progress)
        break
