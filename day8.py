from aochelper import *
import math
import re

#########################################
#########################################

# Day 8
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
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

#########################################
#########################################

def BuildInstructions():
	instructions = [ [ line.split(" ")[0], int(line.split(" ")[1]), False ] for line in inputdata]
	return instructions

def Run(program):
	accumulator = 0
	ip = 0
	loop = False
	while True:
		if ip >= len(program):
			break
		if program[ip][2]:
			loop = True
			break
		program[ip][2] = True
		if program[ip][0] == "nop":
			ip += 1
		elif program[ip][0] == "acc":
			accumulator += program[ip][1]
			ip += 1
		elif program[ip][0] == "jmp":
			ip += program[ip][1]
		else:
			print("Unknown instruction: ", program[ip][0])

	return (accumulator, loop)

#########################################
#########################################

def PartA():
	StartPartA()
	# TestData()

	instructions = BuildInstructions()
	accumulator, _ = Run(instructions)

	ShowAnswer(accumulator)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestData()

	# Brute forcing it
	accumulator = 0
	ix = 0
	while True:
		instructions = BuildInstructions()
		while instructions[ix][0] != "nop" and instructions[ix][0] != "jmp":
			ix += 1
		if instructions[ix][0] == "nop":
			instructions[ix][0] = "jmp"
		else:
			instructions[ix][0] = "nop"
		ix += 1
		accumulator, loop = Run(instructions)
		if loop == False:
			break

	ShowAnswer(accumulator)

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
