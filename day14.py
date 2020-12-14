from aochelper import *
import itertools
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
	inputdata.append("inputdata.clear()")
	inputdata.append("mask = 000000000000000000000000000000X1001X")
	inputdata.append("mem[42] = 100")
	inputdata.append("mask = 00000000000000000000000000000000X0XX")
	inputdata.append("mem[26] = 1")

#########################################
#########################################

class Instruction():
	def __init__(self, mask):
		self.mask = mask
		self.mems = [] # List of (mem, value) tupples
		self.m0 = int(self.mask.replace("X", "1"), 2)
		self.m1 = int(self.mask.replace("X", "0"), 2)
		self.ixen = self.mask.count("X")
		self.floating = [(36 - ix - 1) for ix, l in enumerate(mask) if l == "X"]

	def add(self, mem, value):
		self.mems.append( (mem, value) )
	
	def __repr__(self):
		msg = f"mask = {self.mask}\n"
		for mem in self.mems:
			msg += f"mem[{mem[0]}] {mem[1]}\n"
		msg += f"Floating: {self.ixen}: {self.floating}\n"
		return msg

	def SetMemory(self, memory, address, value):
		memory[address] = value
		
	def ApplyMaskA(self, value):
		value = value | self.m1
		value = value & self.m0
		return value

	def ApplyMaskB(self, value):
		value = value | self.m1
		return value

	def ModifyBit(self, n,  p,  b): 
		m = 1 << p 
		return (n & ~m) | ((b << p) & m) 

	def MutateAddr(self, addr, mutation):
		for value, bit in zip(mutation, self.floating):
			# change bit {bit} to {value}
			addr = self.ModifyBit(addr, bit, value)
		return addr

	def ExecuteA(self, memory):
		for mem in self.mems:
			value = self.ApplyMaskA(mem[1])
			self.SetMemory(memory, mem[0], value)

	def ExecuteB(self, memory):
		for mem in self.mems:
			addr = mem[0]
			value = mem[1]
			addr = self.ApplyMaskB(addr)
			for a in itertools.product([0, 1], repeat = self.ixen):
				newaddr = self.MutateAddr(addr, a)
				# print(f"Set [{newaddr}] to {value}")
				self.SetMemory(memory, newaddr, value)

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

	for instruction in instructions:
		# print(instruction)
		instruction.ExecuteA(memory)

	som = 0
	for k in memory:
		som += memory[k]

	ShowAnswer(som)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestDataB()

	memory = {}
	instructions = Parse()

	for instruction in instructions:
		# print(instruction)
		instruction.ExecuteB(memory)

	som = 0
	for k in memory:
		som += memory[k]

	ShowAnswer(som)

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
