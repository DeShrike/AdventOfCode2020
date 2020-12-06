from aochelper import *
import math

#########################################
#########################################

# Day 6
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("abc")
	inputdata.append("")
	inputdata.append("a")
	inputdata.append("b")
	inputdata.append("c")
	inputdata.append("")
	inputdata.append("ab")
	inputdata.append("ac")
	inputdata.append("")
	inputdata.append("a")
	inputdata.append("a")
	inputdata.append("a")
	inputdata.append("a")
	inputdata.append("")
	inputdata.append("b")

#########################################
#########################################

def GetGroups():
	groups = []
	group = []
	for line in inputdata:
		if line == "":
			groups.append(group)
			group = []
		else:
			group.append(line)

	if len(group) > 0:
		groups.append(group)

	return groups

def CountAnswersAny(group):
	answers = {}
	for person in group:
		for a in person:
			if a in answers:
				answers[a] += 1
			else:
				answers[a] = 1

	return len(answers)

def CountAnswersAll(group):
	answers = {}
	for person in group:
		for a in person:
			if a in answers:
				answers[a] += 1
			else:
				answers[a] = 1

	return sum([1 for c in answers if answers[c] == len(group)])

#########################################
#########################################

def PartA():
	StartPartA()
	# TestData()

	groups = GetGroups()
	answersCount = [CountAnswersAny(g) for g in groups]

	ShowAnswer(sum(answersCount))

#########################################
#########################################

def PartB():
	StartPartB()
	# TestData()

	groups = GetGroups()
	answersCount = [CountAnswersAll(g) for g in groups]

	ShowAnswer(sum(answersCount))

#########################################
#########################################

def Main():
	StartDay(6)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
