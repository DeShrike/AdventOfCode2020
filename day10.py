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
"""
(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10,     12, 15, 16, 19, (22)
(0), 1, 4, 5,    7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5,    7, 10,     12, 15, 16, 19, (22)
(0), 1, 4,    6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4,    6, 7, 10,     12, 15, 16, 19, (22)
(0), 1, 4,       7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4,       7, 10,     12, 15, 16, 19, (22)



(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, (52)
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47,     49, (52)
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46,     48, 49, (52)
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46,         49, (52)
(0), 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45,     47, 48, 49, (52)
(0),       3, 4, 7,       10, 11, 14, 17,         20, 23,     25, 28, 31,         34, 35, 38, 39, 42, 45, 46,     48, 49, (52)
(0),       3, 4, 7,       10, 11, 14, 17,         20, 23,     25, 28, 31,         34, 35, 38, 39, 42, 45, 46,         49, (52)
(0),       3, 4, 7,       10, 11, 14, 17,         20, 23,     25, 28, 31,         34, 35, 38, 39, 42, 45,     47, 48, 49, (52)
(0),       3, 4, 7,       10, 11, 14, 17,         20, 23,     25, 28, 31,         34, 35, 38, 39, 42, 45,     47,     49, (52)
(0),       3, 4, 7,       10, 11, 14, 17,         20, 23,     25, 28, 31,         34, 35, 38, 39, 42, 45,         48, 49, (52)
"""
def PartB():
	StartPartB()
	# TestData1()
	TestData2()

	joltages = [int(line) for line in inputdata]
	builtin = max(joltages) + 3
	joltages.append(0)
	joltages.append(builtin)
	joltages.sort()

	print(joltages)

	result = 1
	i = 0
	while i < len(joltages):
		num = joltages[i]
		possibilities = [x for x in joltages if num < x <= (num + 3)]
		if len(possibilities) == 0:
			break
		if len(possibilities) == 3:
			result *= 4
		if len(possibilities) == 2:
			result *= 2
		print(num, possibilities, result)
		i += len(possibilities)

	print(result)
	
	#orders = [[0]]
	#addedSome = True
	#while addedSome:
	#	addedSome = False
	#	oo = len(orders)
	#	print(oo, end = "\r")
	#	for ix in range(oo):
	#		o = orders[ix]
	#		possibilities = [x for x in joltages if o[-1] < x <= (o[-1] + 3)]
	#		if len(possibilities) > 0:
	#			addedSome = True
	#			first = possibilities.pop()
	#			for ix2 in possibilities:
	#				newo = [ooo for ooo in o]
	#				newo.append(ix2)
	#				orders.append(newo)
	#			o.append(first)

	#ShowAnswer(len(orders))

	# Attempt 1 : 274877906944 Too Low

	ShowAnswer("?")

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
