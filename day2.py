from aochelper import *
import math
import re

#########################################
#########################################

# Day 2
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("1-3 a: abcde")
	inputdata.append("1-3 b: cdefg")
	inputdata.append("2-9 c: ccccccccc")

#########################################
#########################################

rules = []

def ParseInput():
	rx = re.compile("(?P<minimum>[0-9]*)\-(?P<maximum>[0-9]*) (?P<letter>[a-z])\: (?P<password>[a-z]*)")

	rules.clear()

	for line in inputdata:
		match = rx.search(line)
		if match:
			mi = int(match["minimum"])
			ma = int(match["maximum"])
			le = match["letter"]
			pa = match["password"]
			rules.append([mi, ma, le, pa])
		else:
			print("No match", line)

#########################################
#########################################

def PartA():
	StartPartA()
	# TestData()

	ParseInput()

	validcount = 0
	for rule in rules:
		c = rule[3].count(rule[2])
		if rule[0] <= c <= rule[1]:
			validcount += 1

	ShowAnswer(validcount)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestData()

	ParseInput()

	validcount = 0
	for rule in rules:
		p1 = rule[3][rule[0] - 1] 
		p2 = rule[3][rule[1] - 1]
		c = (1 if p1 == rule[2] else 0) + (1 if p2 == rule[2] else 0)
		if c == 1:
			validcount += 1

	ShowAnswer(validcount)

#########################################
#########################################

def Main():
	StartDay(2)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
