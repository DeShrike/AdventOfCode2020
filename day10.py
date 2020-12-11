from aochelper import *
import math
import re

#########################################
#########################################

# Day 10
# https://adventofcode.com/2020

#########################################
#########################################

def TestData1():
	inputdata.clear()
	inputdata.append("16")
	inputdata.append("10")
	inputdata.append("15")
	inputdata.append("5")
	inputdata.append("1")
	inputdata.append("11")
	inputdata.append("7")
	inputdata.append("19")
	inputdata.append("6")
	inputdata.append("12")
	inputdata.append("4")

def TestData2():
	inputdata.clear()
	inputdata.append("28")
	inputdata.append("33")
	inputdata.append("18")
	inputdata.append("42")
	inputdata.append("31")
	inputdata.append("14")
	inputdata.append("46")
	inputdata.append("20")
	inputdata.append("48")
	inputdata.append("47")
	inputdata.append("24")
	inputdata.append("23")
	inputdata.append("49")
	inputdata.append("45")
	inputdata.append("19")
	inputdata.append("38")
	inputdata.append("39")
	inputdata.append("11")
	inputdata.append("1")
	inputdata.append("32")
	inputdata.append("25")
	inputdata.append("35")
	inputdata.append("8")
	inputdata.append("17")
	inputdata.append("7")
	inputdata.append("9")
	inputdata.append("4")
	inputdata.append("2")
	inputdata.append("34")
	inputdata.append("10")
	inputdata.append("3")

#########################################
#########################################

def PartA():
	StartPartA()
	# TestData1()
	# TestData2()

	joltages = [int(line) for line in inputdata]
	builtin = max(joltages) + 3
	joltages.append(builtin)
	joltages.sort()
	joltages.reverse()

	order = []
	rating = 0
	diff1count = 0
	diff2count = 0
	diff3count = 0
	while len(joltages) > 0:
		nex = joltages.pop()
		diff = nex - rating
		if diff == 1:
			diff1count += 1
		if diff == 2:
			diff2count += 1
		if diff == 3:
			diff3count += 1
		rating = nex

	ShowAnswer(diff1count * diff3count)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestData1()
	# TestData2()

	joltages = [int(line) for line in inputdata]
	builtin = max(joltages) + 3
	joltages.append(0)
	joltages.append(builtin)
	joltages.sort()

	result = 1
	ix = 0
	while ix < len(joltages):
		current = joltages[ix]
		count = 1
		while ix + count < len(joltages) and joltages[ix + count] == current + count:
			count += 1
		if count == 5:
			result *= 7
		if count == 4:
			result *= 4
		if count == 3:
			result *= 2
		ix += count

	# Attempt 1 : 274877906944 Too Low

	ShowAnswer(result)

#########################################
#########################################

def Main():
	StartDay(10)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
