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
	for a, b in itertools.product(inputdata, inputdata):
		if int(a) + int(b) == 2020:
			answer = int(a) * int(b)
			break

	ShowAnswer(answer)

#########################################
#########################################

def PartB():
	StartPartB()

	answer = None
	for a, b, c in itertools.product(inputdata, inputdata, inputdata):
		if int(a) + int(b) + int(c) == 2020:
			answer = int(a) * int(b) * int(c)
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

