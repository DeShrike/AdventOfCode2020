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

AnswerA = None

def PartA():
	global AnswerA
	StartPartA()
	TestData()

	numbers = [int(line) for line in inputdata]
	AnswerA = None

	for ix in range(preamble, len(numbers)):
		validrange = numbers[ix - preamble:ix]
		if SumExists(numbers[ix], validrange) == False:
			AnswerA = numbers[ix]
			break

	ShowAnswer(AnswerA)

#########################################
#########################################

def PartB():
	StartPartB()
	TestData()

	answer = None
	numbers = [int(line) for line in inputdata]
	for ix in range(len(numbers)):
		sum = 0
		ix2 = ix
		while sum <= AnswerA:
			sum += numbers[ix2]
			ix2 += 1
		if sum == AnswerA:
			answer = numbers[ix] + numbers[ix2 - 1]
			break

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
