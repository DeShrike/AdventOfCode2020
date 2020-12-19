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

	rx1 = re.compile(f"(?P<id>[0-9]*): \"(?P<letter>[a-z])\"")
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
		self.built = False

		self.line = line

		self.subrulesA = []
		self.subrulesB = []

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

	def __str__(self):
		msg = f"Rule #{self.id}\n"
		msg += f"\"{self.line}\"\n"
		if self.letter is not None:
			msg += f"Letter: {self.letter}"
		else:
			msg += f"A1: {self.a1} A2: {self.a2} A3: {self.a3}\n"
			msg += f"B1: {self.b1} B2: {self.b2}\n"
			msg += f"len(subrulesA) = {len(self.subrulesA)}\n"
			msg += f"len(subrulesB) = {len(self.subrulesB)}"
		return msg

	def BuildTree(self, rules):
		if self.built:
			return
		if self.letter is not None:
			return
		if self.a1 is not None:
			subrule = rules[self.a1]
			subrule.BuildTree(rules)
			self.subrulesA.append(subrule)
		if self.a2 is not None:
			subrule = rules[self.a2]
			subrule.BuildTree(rules)
			self.subrulesA.append(subrule)
		if self.a3 is not None:
			subrule = rules[self.a3]
			subrule.BuildTree(rules)
			self.subrulesA.append(subrule)
		if self.b1 is not None:
			subrule = rules[self.b1]
			subrule.BuildTree(rules)
			self.subrulesB.append(subrule)
		if self.b2 is not None:
			subrule = rules[self.b2]
			subrule.BuildTree(rules)
			self.subrulesB.append(subrule)
		self.built = True

	def Validate(self, message):
		# print(f"Validate Rule {self.id} for '{message}'")

		if self.letter is not None:
			if message[0] == self.letter:
				return True, 1
			return False, 0

		progresslength = 0
		rule = self.subrulesA[0]
		valid, l = rule.Validate(message[progresslength:])
		if valid:
			progresslength += l
			if len(self.subrulesA) >= 2:
				rule = self.subrulesA[1]
				valid, l = rule.Validate(message[progresslength:])
				if valid:
					progresslength += l
					if len(self.subrulesA) >= 3:
						rule = self.subrulesA[2]
						valid, l = rule.Validate(message[progresslength:])
						if valid:
							progresslength += l

		if valid == False and len(self.subrulesB) > 0:
			progresslength = 0
			rule = self.subrulesB[0]
			valid, l = rule.Validate(message[progresslength:])
			if valid:
				progresslength += l
				if len(self.subrulesB) >= 2:
					rule = self.subrulesB[1]
					valid, l = rule.Validate(message[progresslength:])
					if valid:
						progresslength += l

		# print(f"Rule {self.id}", valid, progresslength)
		return valid, progresslength

def Parse():
	messages = []
	rules = {}

	inrules = True
	for line in inputdata:
		if line == "":
			inrules = False
			continue
		if inrules:
			rule = Rule(line)
			rules[rule.id] = rule
		else:
			messages.append(line)

	return rules, messages

#########################################
#########################################

def PartA():
	StartPartA()
	# TestDataA()

	rules, messages = Parse()
	root = rules[0]
	root.BuildTree(rules)

	""""
	for rule in rules:
		print(rules[rule])
		print("")

	valid, _ = root.Validate(messages[0])
	"""
	answer = 0
	for msg in messages:
		valid, l = root.Validate(msg)
		if valid and l == len(msg):
			answer += 1

	# Attempt 1 : 165 Too high

	ShowAnswer(answer)

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
