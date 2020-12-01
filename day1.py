from aochelper import *
import itertools
import math
import re

#########################################
#########################################

# Day 1
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("1721")
	inputdata.append("979")
	inputdata.append("366")
	inputdata.append("299")
	inputdata.append("675")
	inputdata.append("1456")	

def TestDataB():
	inputdata.clear()
	inputdata.append("1721")
	inputdata.append("979")
	inputdata.append("366")
	inputdata.append("299")
	inputdata.append("675")
	inputdata.append("1456")	

#########################################
#########################################

def PartA():
	StartPartA()

	answer = None
	numbers = [int(line) for line in inputdata]
	for a, b in itertools.product(numbers, numbers):
		if a + b == 2020:
			answer = a * b
			break

	ShowAnswer(answer)

#########################################
#########################################

def PartB():
	StartPartB()

	answer = None
	numbers = [int(line) for line in inputdata]
	for a, b, c in itertools.product(numbers, numbers, numbers):
		if a + b + c == 2020:
			answer = a * b * c
			break

	ShowAnswer(answer)

#########################################
#########################################

if __name__ == "__main__":
	StartDay(1)
	ReadInput()
	# TestDataA()
	PartA()
	# TestDataB()
	PartB()
	print("")

