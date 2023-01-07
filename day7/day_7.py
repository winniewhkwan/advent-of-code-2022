# Day 7 https://adventofcode.com/2022/day/7
# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?

from enum import Enum

class CmdLegend(Enum):
	USER_INPUT = '$'
	HOME = '/'
	CHANGE = 'cd'
	LIST = 'ls'
	MOVE_OUT = '..'
	DIR = 'dir'

def get_directory_names():
	names = []
	with open('day7/test_input.txt') as file:
	# with open('day7/input.txt') as file:
		all_lines = file.readlines()

		for line in all_lines:
			# Find names of all directories
			line_data = line.split()
			if (line_data[0] == CmdLegend.DIR.value):
				names.append(line_data[1])
		return names

def get_directory_size(dirName):
	dir_size = 0
	print('the size of one directory')

directory_names = get_directory_names()
print(directory_names)
