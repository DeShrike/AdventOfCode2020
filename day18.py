from aochelper import *
import math
import re

#########################################
#########################################

# Day 18
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("1 + 2 * 3 + 4 * 5 + 6")							# 71
	inputdata.append("2 * 3 + (4 * 5)")									# 26
	inputdata.append("5 + (8 * 3 + 9 + 3 * 4 * 3)")						# 437
	inputdata.append("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")		# 12240
	inputdata.append("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")	# 13632

def TestDataB():
	inputdata.clear()

#########################################
#########################################

class Expression():
	def __init__(self, line: str):
		line = line.replace("(", " ( ")
		line = line.replace(")", " ) ")
		line = line.replace("  ", " ")
		parts = line.split(" ")
		pass

	def Eval(self) -> int:
		return 0

#########################################
#########################################

def PartA():
	StartPartA()
	TestDataA()

	som = 0
	for line in inputdata:
		ex = Expression(line)
		som += ex.Eval()

	ShowAnswer(som)

#########################################
#########################################

def PartB():
	StartPartB()
	TestDataB()

	ShowAnswer("?")

#########################################
#########################################

def Main():
	StartDay(18)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
