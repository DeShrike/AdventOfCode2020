from aochelper import *
import math
import re

#########################################
#########################################

# Day 8
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("nop +0")
	inputdata.append("acc +1")
	inputdata.append("jmp +4")
	inputdata.append("acc +3")
	inputdata.append("jmp -3")
	inputdata.append("acc -99")
	inputdata.append("acc +1")
	inputdata.append("jmp -4")
	inputdata.append("acc +6")

def TestDataB():
	inputdata.clear()

#########################################
#########################################

def BuildInstructions():
	instructions = [ [ line.split(" ")[0], int(line.split(" ")[1]), False ] for line in inputdata]
	return instructions

#########################################
#########################################

def PartA():
	StartPartA()
	# TestDataA()

	instructions = BuildInstructions()
	accumulator = 0
	ip = 0
	while True:
		if instructions[ip][2]:
			break
		instructions[ip][2] = True
		if instructions[ip][0] == "nop":
			ip += 1
		elif instructions[ip][0] == "acc":
			accumulator += instructions[ip][1]
			ip += 1
		elif instructions[ip][0] == "jmp":
			ip += instructions[ip][1]
		else:
			print("Unknown instruction: ", instructions[ip][0])

	ShowAnswer(accumulator)

#########################################
#########################################

def PartB():
	StartPartB()
	TestDataB()

	ShowAnswer("?")

#########################################
#########################################

def Main():
	StartDay(8)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
