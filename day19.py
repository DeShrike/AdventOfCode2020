from aochelper import *
import math
import re

#########################################
#########################################

# Day 19
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("0: 4 1 5")
	inputdata.append("1: 2 3 | 3 2")
	inputdata.append("2: 4 4 | 5 5")
	inputdata.append("3: 4 5 | 5 4")
	inputdata.append("4: \"a\"")
	inputdata.append("5: \"b\"")
	inputdata.append("")
	inputdata.append("ababbb")
	inputdata.append("bababa")
	inputdata.append("abbbab")
	inputdata.append("aaabbb")
	inputdata.append("aaaabbb")

def TestDataB():
	inputdata.clear()

#########################################
#########################################

class Rule():

	rx1 = re.compile(f"(?P<id>[0-9]*): \"(?P<letter>[ab])\"")
	rx2 = re.compile(f"(?P<id>[0-9]*): (?P<a1>[0-9]*) (?P<a2>[0-9]*) \| (?P<b1>[0-9]*) (?P<b2>[0-9]*)")
	rx3 = re.compile(f"(?P<id>[0-9]*): (?P<a1>[0-9]*) (?P<a2>[0-9]*) (?P<a3>[0-9]*)")
	rx4 = re.compile(f"(?P<id>[0-9]*): (?P<a1>[0-9]*) (?P<a2>[0-9]*)")
	rx5 = re.compile(f"(?P<id>[0-9]*): (?P<a1>[0-9]*) \| (?P<b1>[0-9]*)")
	rx6 = re.compile(f"(?P<id>[0-9]*): (?P<a1>[0-9]*)")

	def __init__(self, line):
		self.id = None
		self.letter = None
		self.a1 = None
		self.a2 = None
		self.a3 = None
		self.b1 = None
		self.b2 = None

		match = self.rx1.match(line)
		if match:
			self.id = int(match["id"])
			self.letter = match["letter"]
			return

		match = self.rx2.match(line)
		if match:
			self.id = int(match["id"])
			self.a1 = int(match["a1"])
			self.a2 = int(match["a2"])
			self.b1 = int(match["b1"])
			self.b2 = int(match["b2"])
			return

		match = self.rx5.match(line)
		if match:
			self.id = int(match["id"])
			self.a1 = int(match["a1"])
			self.b1 = int(match["b1"])
			return

		match = self.rx3.match(line)
		if match:
			self.id = int(match["id"])
			self.a1 = int(match["a1"])
			self.a2 = int(match["a2"])
			self.a3 = int(match["a3"])
			return

		match = self.rx4.match(line)
		if match:
			self.id = int(match["id"])
			self.a1 = int(match["a1"])
			self.a2 = int(match["a2"])
			return

		match = self.rx6.match(line)
		if match:
			self.id = int(match["id"])
			self.a1 = int(match["a1"])
			return

		print("Error: No match: ", line)

def Parse():
	messages = []
	rules = []

	inrules = True
	for line in inputdata:
		if line == "":
			inrules = False
		if inrules:
			rule = Rule(line)
			rules.append(rule)
		else:
			messages.append(line)

	return rules, messages

#########################################
#########################################

def PartA():
	StartPartA()
	TestDataA()

	rules, messages = Parse()

	ShowAnswer("?")

#########################################
#########################################

def PartB():
	StartPartB()
	TestDataB()

	ShowAnswer("?")

#########################################
#########################################

def Main():
	StartDay(19)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
