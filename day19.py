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
	inputdata.append("42: 9 14 | 10 1")
	inputdata.append("9: 14 27 | 1 26")
	inputdata.append("10: 23 14 | 28 1")
	inputdata.append("1: \"a\"")
	inputdata.append("11: 42 31")
	inputdata.append("5: 1 14 | 15 1")
	inputdata.append("19: 14 1 | 14 14")
	inputdata.append("12: 24 14 | 19 1")
	inputdata.append("16: 15 1 | 14 14")
	inputdata.append("31: 14 17 | 1 13")
	inputdata.append("6: 14 14 | 1 14")
	inputdata.append("2: 1 24 | 14 4")
	inputdata.append("0: 8 11")
	inputdata.append("13: 14 3 | 1 12")
	inputdata.append("15: 1 | 14")
	inputdata.append("17: 14 2 | 1 7")
	inputdata.append("23: 25 1 | 22 14")
	inputdata.append("28: 16 1")
	inputdata.append("4: 1 1")
	inputdata.append("20: 14 14 | 1 15")
	inputdata.append("3: 5 14 | 16 1")
	inputdata.append("27: 1 6 | 14 18")
	inputdata.append("14: \"b\"")
	inputdata.append("21: 14 1 | 1 14")
	inputdata.append("25: 1 1 | 1 14")
	inputdata.append("22: 14 14")
	inputdata.append("8: 42")
	inputdata.append("26: 14 22 | 1 20")
	inputdata.append("18: 15 15")
	inputdata.append("7: 14 5 | 1 21")
	inputdata.append("24: 14 1")
	inputdata.append("")
	inputdata.append("abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa")
	inputdata.append("bbabbbbaabaabba")
	inputdata.append("babbbbaabbbbbabbbbbbaabaaabaaa")
	inputdata.append("aaabbbbbbaaaabaababaabababbabaaabbababababaaa")
	inputdata.append("bbbbbbbaaaabbbbaaabbabaaa")
	inputdata.append("bbbababbbbaaaaaaaabbababaaababaabab")
	inputdata.append("ababaaaaaabaaab")
	inputdata.append("ababaaaaabbbaba")
	inputdata.append("baabbaaaabbaaaababbaababb")
	inputdata.append("abbbbabbbbaaaababbbbbbaaaababb")
	inputdata.append("aaaaabbaabaaaaababaa")
	inputdata.append("aaaabbaaaabbaaa")
	inputdata.append("aaaabbaabbaaaaaaabbbabbbaaabbaabaaa")
	inputdata.append("babaaabbbaaabaababbaabababaaab")
	inputdata.append("aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba")

#########################################
#########################################

class Rule():

	rx1 = re.compile(f"(?P<id>[0-9]*): \"(?P<letter>[a-z])\"")
	rx7 = re.compile(f"(?P<id>[0-9]*): (?P<a1>[0-9]*) (?P<a2>[0-9]*) \| (?P<b1>[0-9]*) (?P<b2>[0-9]*) (?P<b3>[0-9]*)")
	rx2 = re.compile(f"(?P<id>[0-9]*): (?P<a1>[0-9]*) (?P<a2>[0-9]*) \| (?P<b1>[0-9]*) (?P<b2>[0-9]*)")
	rx8 = re.compile(f"(?P<id>[0-9]*): (?P<a1>[0-9]*) \| (?P<b1>[0-9]*) (?P<b2>[0-9]*)")
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
		self.b3 = None
		self.built = False

		self.line = line

		self.subrulesA = []
		self.subrulesB = []

		match = self.rx1.match(line)
		if match:
			self.id = int(match["id"])
			self.letter = match["letter"]
			return

		match = self.rx7.match(line)
		if match:
			self.id = int(match["id"])
			self.a1 = int(match["a1"])
			self.a2 = int(match["a2"])
			self.b1 = int(match["b1"])
			self.b2 = int(match["b2"])
			self.b3 = int(match["b3"])
			return

		match = self.rx2.match(line)
		if match:
			self.id = int(match["id"])
			self.a1 = int(match["a1"])
			self.a2 = int(match["a2"])
			self.b1 = int(match["b1"])
			self.b2 = int(match["b2"])
			return

		match = self.rx8.match(line)
		if match:
			self.id = int(match["id"])
			self.a1 = int(match["a1"])
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
			msg += f"B1: {self.b1} B2: {self.b2} B3: {self.b3}\n"
			msg += f"len(subrulesA) = {len(self.subrulesA)}\n"
			msg += f"len(subrulesB) = {len(self.subrulesB)}"
		return msg

	def BuildTree(self, rules):
		if self.built:
			return
		self.built = True
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
		if self.b3 is not None:
			subrule = rules[self.b3]
			subrule.BuildTree(rules)
			self.subrulesB.append(subrule)

	def Validate(self, message):
		# print(f"Validate Rule {self.id} for '{message}'")

		if message == "":
			return False, 0

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
						if len(self.subrulesB) >= 3:
							rule = self.subrulesB[2]
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

def ValidateRecursive(msg: str, root, rule31, rule42, matching31) -> bool:
	valid, l = root.Validate(msg)
	if valid and l == len(msg):
		return True
	else:
		valid42, l42 = rule42.Validate(msg)
		if valid42:
			newmsg = msg[l42:]
			valid = ValidateRecursive(newmsg, root, rule31, rule42, matching31)
			if valid:
				return True
			else:
				# Check if ends with a rule 31
				for m31 in matching31:
					if msg[-len(m31):] == m31:
						newmsg = msg[0:len(msg) - len(m31)]
						if root.Validate(newmsg):
							return True
	return False

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
	# TestDataB()

	for ix, line in enumerate(inputdata):
		if line[0:2] == "8:":
			inputdata[ix] = "8: 42 | 42 8"
		if line[0:3] == "11:":
			inputdata[ix] = "11: 42 31 | 42 11 31"

	rules, messages = Parse()
	root = rules[0]
	root.BuildTree(rules)

	rule42 = rules[42]
	rule31 = rules[31]

	# find all messages that match rule 31
	matching31 = [] 
	for msg in messages:
		valid, l = rule31.Validate(msg)
		if valid:
			matching31.append(msg)

	answer = 0
	for msg in messages:
		valid = ValidateRecursive(msg, root, rule31, rule42, matching31)
		if valid:
			answer += 1

	# Attempt 1 : 162 Too low
	# Attempt 2 : 315 Too high

	ShowAnswer(answer)

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
