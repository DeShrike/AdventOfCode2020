from aochelper import *
import math
import re

#########################################
#########################################

# Day 16
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("class: 1-3 or 5-7")
	inputdata.append("row: 6-11 or 33-44")
	inputdata.append("seat: 13-40 or 45-50")
	inputdata.append("")
	inputdata.append("your ticket:")
	inputdata.append("7,1,14")
	inputdata.append("")
	inputdata.append("nearby tickets:")
	inputdata.append("7,3,47")
	inputdata.append("40,4,50")
	inputdata.append("55,2,20")
	inputdata.append("38,6,12")

def TestDataB():
	inputdata.clear()
	inputdata.append("class: 0-1 or 4-19")
	inputdata.append("row: 0-5 or 8-19")
	inputdata.append("seat: 0-13 or 16-19")
	inputdata.append("")
	inputdata.append("your ticket:")
	inputdata.append("11,12,13")
	inputdata.append("")
	inputdata.append("nearby tickets:")
	inputdata.append("3,9,18")
	inputdata.append("15,1,5")
	inputdata.append("5,14,9")

#########################################
#########################################

def Parse():
	rules = {}	# field: ( (min1, max1), (min2, max2) )
	your = None
	nearby = []
	nextyour = False
	nextnearby = False
	rx = re.compile(f"(?P<field>[a-z ]*): (?P<min1>[0-9]*)-(?P<max1>[0-9]*) or (?P<min2>[0-9]*)-(?P<max2>[0-9]*)")
	for line in inputdata:
		match = rx.match(line)
		if match:
			field = match["field"]
			min1 = int(match["min1"])
			max1 = int(match["max1"])
			min2 = int(match["min2"])
			max2 = int(match["max2"])
			rules[field] = ( (min1, max1), (min2, max2) )
		elif line == "your ticket:":
			nextyour = True
		elif line == "nearby tickets:":
			nextnearby = True
		elif nextyour:
			your = [int(x) for x in line.split(",")]
			nextyour = False
		elif nextnearby:
			nearby.append([int(x) for x in line.split(",")])

	return rules, your, nearby

def IsValidForRule(value, rule):
	return rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]  

def IsValidAny(value, rules):
	for rule in rules:
		if IsValidForRule(value, rules[rule]):
			return True
	return False

#########################################
#########################################

def PartA():
	StartPartA()
	#TestDataA()

	rules, your, nearby = Parse()

	# print(rules)
	# print(your)
	# print(nearby)

	error_rate = 0

	for near in nearby:
		for val in near:
			if IsValidAny(val, rules) == False:
				error_rate += val

	ShowAnswer(error_rate)

#########################################
#########################################

def PartB():
	StartPartB()
	TestDataB()

	rules, your, nearby = Parse()

	print(rules)

	nearbyvalid = []
	for near in nearby:
		for val in near:
			if IsValidAny(val, rules):
				nearbyvalid.append(near)
				break

	print(nearbyvalid)

	ShowAnswer("?")

#########################################
#########################################

def Main():
	StartDay(16)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
