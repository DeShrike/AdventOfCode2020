from aochelper import *
import math
import re

#########################################
#########################################

# Day 14
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
	inputdata.append("mem[8] = 11")
	inputdata.append("mem[7] = 101")
	inputdata.append("mem[8] = 0")

def TestDataB():
	inputdata.clear()

#########################################
#########################################

class Instruction():
	def __init__(self, mask):
		self.mask = mask
		self.mems = [] # List of (mem, value) tupples
		self.m0 = int(self.mask.replace("X", "1"), 2)
		self.m1 = int(self.mask.replace("X", "0"), 2)
	
	def add(self, mem, value):
		self.mems.append( (mem, value) )
	
	def __repr__(self):
		msg = f"mask = {self.mask}\n"
		for mem in self.mems:
			msg += f"mem[{mem[0]}] {mem[1]}\n"
		return msg

	def SetMemory(self, memory, address, value):
		memory[address] = value
		
	def ApplyMask(self, value):
		value = value | self.m1
		value = value & self.m0
		return value

	def Execute(self, memory):
		for mem in self.mems:
			value = self.ApplyMask(mem[1])
			self.SetMemory(memory, mem[0], value)

def Parse():
	instructions = []
	current = None
	rx1 = re.compile(f"mask = (?P<mask>[01X]*)")
	rx2 = re.compile(f"mem\[(?P<mem>[0-9]*)\] = (?P<value>[0-9]*)")
	for line in inputdata:
		match = rx1.search(line)
		if match:
			mask = match["mask"]
			current = Instruction(mask)
			instructions.append(current)
		else:
			match = rx2.search(line)
			if match:
				mem = int(match["mem"])
				value = int(match["value"])
				current.add(mem, value)

	return instructions

#########################################
#########################################

def PartA():
	StartPartA()
	# TestDataA()

	memory = {}
	instructions = Parse()
	# print(instructions)
	for instruction in instructions:
		instruction.Execute(memory)

	som = 0
	for k in memory:
		# print(f"[{k}] = {memory[k]}")
		som += memory[k]

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
	StartDay(14)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
