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
	# total: 26406

def TestDataB():
	inputdata.clear()
	inputdata.append("1 + 2 * 3 + 4 * 5 + 6")							# 231
	inputdata.append("1 + (2 * 3) + (4 * (5 + 6))")						# 51
	inputdata.append("2 * 3 + (4 * 5)")									# 46
	inputdata.append("5 + (8 * 3 + 9 + 3 * 4 * 3)")						# 1445
	inputdata.append("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")		# 669060
	inputdata.append("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")	# 23340
	# total: 694173

#########################################
#########################################

class Expression():
	def __init__(self, line: str, advanced: bool = False):
		line = line.replace("(", " ( ")
		line = line.replace(")", " ) ")
		line = line.replace("  ", " ")
		# print(line)
		parts = line.strip().split(" ")

		self.tokens = []
		parencount = 0
		subparts = None
		for part in parts:
			if part == "(":
				if subparts is None:
					subparts = []
				else:
					subparts.append(part)
				parencount += 1
			elif part == ")":
				parencount -= 1
				if parencount == 0:
					subexpression = Expression(" ".join(subparts), advanced)
					self.tokens.append(subexpression)
					subparts = None
				else:
					subparts.append(part)
			elif part == "+":
				if subparts is None:
					self.tokens.append(part)
				else:
					subparts.append(part)
			elif part == "*":
				if subparts is None:
					self.tokens.append(part)
				else:
					subparts.append(part)
			else:
				if subparts is None:
					constant = int(part)
					self.tokens.append(constant)
				else:
					subparts.append(part)

	def EvalPlus(self):
		changed = True
		while changed:
			changed = False
			for ix, token in enumerate(self.tokens):
				if type(token) == int:
					left = token
				elif type(token) == str:
					if token == "+":
						nexttoken = self.tokens[ix + 1]
						if type(nexttoken) == int:
							right = nexttoken
						elif type(nexttoken) == Expression:
							right = nexttoken.Eval(True)
						self.tokens[ix] = left + right
						self.tokens[ix + 1] = None
						self.tokens[ix - 1] = None
						left = self.tokens[ix]
						changed = True
						while None in self.tokens:
							self.tokens.remove(None)
						break
				elif type(token) == Expression:
					left = token.Eval(True)

	def Eval(self, advanced: bool = False) -> int:
		if advanced:
			self.EvalPlus()

		value = 0
		operation = None
		for token in self.tokens:
			if token is None:
				pass
			elif type(token) == int:
				val = token
				if operation is not None:
					if operation == "+":
						value = value + val
					elif operation == "*":
						value = value * val
					operation = None
				else:
					value = val
			elif type(token) == str:
				operation = token
			elif type(token) == Expression:
				val = token.Eval(advanced)
				if operation is not None:
					if operation == "+":
						value = value + val
					elif operation == "*":
						value = value * val
					operation = None
				else:
					value = val

		return value

#########################################
#########################################

def PartA():
	StartPartA()
	# TestDataA()

	som = 0
	for line in inputdata:
		ex = Expression(line)
		som += ex.Eval()

	ShowAnswer(som)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestDataB()

	som = 0
	for line in inputdata:
		ex = Expression(line)
		som += ex.Eval(True)

	ShowAnswer(som)

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
