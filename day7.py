from aochelper import *
import math
import re

#########################################
#########################################

# Day 7
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("light red bags contain 1 bright white bag, 2 muted yellow bags.")
	inputdata.append("dark orange bags contain 3 bright white bags, 4 muted yellow bags.")
	inputdata.append("bright white bags contain 1 shiny gold bag.")
	inputdata.append("muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.")
	inputdata.append("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.")
	inputdata.append("dark olive bags contain 3 faded blue bags, 4 dotted black bags.")
	inputdata.append("vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.")
	inputdata.append("faded blue bags contain no other bags.")
	inputdata.append("dotted black bags contain no other bags.")

def TestDataB():
	inputdata.clear()
	inputdata.append("shiny gold bags contain 2 dark red bags.")
	inputdata.append("dark red bags contain 2 dark orange bags.")
	inputdata.append("dark orange bags contain 2 dark yellow bags.")
	inputdata.append("dark yellow bags contain 2 dark green bags.")
	inputdata.append("dark green bags contain 2 dark blue bags.")
	inputdata.append("dark blue bags contain 2 dark violet bags.")
	inputdata.append("dark violet bags contain no other bags.")

#########################################
#########################################

def ParseData():

	rules = {}
	rx0 = re.compile("(?P<bagname>[a-z]* [a-z]*) bags")
	rx1 = re.compile("(?P<count>[0-9]*) (?P<bagname>[a-z]* [a-z]*) bag(s)?")
	for line in inputdata:
		line = line.replace(" contain", ",")
		parts = line.split(", ")
		match = rx0.search(parts[0])
		base = ""
		if match:
			base = match["bagname"]
			if base not in rules:
				rules[base] = []
		else:
			print("BAD: ", line)
			continue

		for s in parts[1:]:
			if s != ", no other bags":
				match = rx1.search(s)
				if match:
					c = int(match["count"])
					b = match["bagname"]

					rules[base].append((c, b))

	# for r in rules:
	#	print(r, rules[r])
	#	print("")

	return rules

#########################################
#########################################

def PartA():
	StartPartA()
	# TestDataA()
	
	rules = ParseData()
	mybag = "shiny gold"

	bags = []
	colors = []
	for r in rules:
		children = rules[r]
		for c in children:
			if c[1] == mybag:
				if r not in colors:
					colors.append(r)

	# print(colors)

	while len(colors) > 0:
		current = colors.pop()
		if current not in bags:
			bags.append(current)
		for r in rules:
			children = rules[r]
			for c in children:
				if c[1] == current:
					if r not in colors:
						colors.append(r)
		# print(colors)

	# print("Bags", bags)

	ShowAnswer(len(bags))

#########################################
#########################################

def CountSubBags(rules, name):
	bags = rules[name]
	c = 1
	for bag in bags:
		if bag[1] in rules:
			c += bag[0] * CountSubBags(rules, bag[1])
	
	return c

def PartB():
	StartPartB()
	# TestDataA()
	# TestDataB()

	rules = ParseData()
	mybag = "shiny gold"

	count = CountSubBags(rules, mybag) - 1

	ShowAnswer(count)

#########################################
#########################################

def Main():
	StartDay(7)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
