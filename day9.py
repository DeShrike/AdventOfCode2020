from aochelper import *
import itertools
import math
import re

#########################################
#########################################

# Day 9
# https://adventofcode.com/2020

#########################################
#########################################

preamble = 25

def TestData():
	global preamble
	preamble = 5
	inputdata.clear()
	inputdata.append("35")
	inputdata.append("20")
	inputdata.append("15")
	inputdata.append("25")
	inputdata.append("47")
	inputdata.append("40")
	inputdata.append("62")
	inputdata.append("55")
	inputdata.append("65")
	inputdata.append("95")
	inputdata.append("102")
	inputdata.append("117")
	inputdata.append("150")
	inputdata.append("182")
	inputdata.append("127")
	inputdata.append("219")
	inputdata.append("299")
	inputdata.append("277")
	inputdata.append("309")
	inputdata.append("576")

#########################################
#########################################

def SumExists(num, numbers):

	for a, b in itertools.product(numbers, numbers):
		if a + b == num and a != b:
			return True

	return False

#########################################
#########################################

def PartA():
	StartPartA()
	# TestData()

	numbers = [int(line) for line in inputdata]
	answer = None

	for ix in range(preamble, len(numbers)):
		validrange = numbers[ix - preamble:ix]
		if SumExists(numbers[ix], validrange) == False:
			answer = numbers[ix]
			break

	ShowAnswer(answer)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestData()

	answera = GetAnswerA()

	answer = None
	numbers = [int(line) for line in inputdata]
	for ix in range(len(numbers)):
		sum = 0
		ix2 = ix
		while sum < answera:
			sum += numbers[ix2]
			ix2 += 1
		if sum == answera:
			validrange = numbers[ix:ix2]
			answer = min(validrange) + max(validrange)
			# print(validrange)
			break

	# Attempt 1: 52595509 Too Low
	
	ShowAnswer(answer)

#########################################
#########################################

def Main():
	StartDay(9)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
