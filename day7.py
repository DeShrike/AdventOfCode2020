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

	for r in rules:
		print(r, rules[r])
		print("")

	return rules

class Bag():
	def __init__(self, name, count):
		self.parents = []
		self.children = []
		self.name = name
		self.count = count

	def Find(self, name):
		if self.name == name:
			return self
		for c in self.children:
			found = c.Find(name)
			if found is not None:
				return found
		return None

	def __str__(self):
		s = f"'{self.name}' x {self.count}"
		for p in self.parents:
			s += "\n -> " + str(p)
		return s

class Tree():
	def __init__(self):
		self.heads = []

	def Add(self, parent, name, count):
		p = self.Find(parent)
		if p is None:
			p = Bag(name, 0)
			self.heads.append(p)
		c = self.Find(name)
		if c is None:
			c = Bag(name, count)
		p.children.append(c)
		c.parents.append(p)

	def Find(self, name):
		for h in self.heads:
			found = h.Find(name)
			if found is not None:
				return found
		return None

	def __str__(self):
		s = ""
		for h in self.heads:
			s += str(h) + "\n"
		return s

def BuildTree(rules):
	tree = Tree()

	for rule in rules:
		for r in rules[rule]:
			print("Add", rule, r[1], r[0])
			tree.Add(rule, r[1], r[0]) 

	return tree

#########################################
#########################################

def PartA():
	StartPartA()
	# TestDataA()
	
	rules = ParseData()
	# tree = BuildTree(rules)
	# print(tree)
	mybag = "shiny gold"

	bags = []
	colors = []
	for r in rules:
		children = rules[r]
		for c in children:
			if c[1] == mybag:
				if r not in colors:
					colors.append(r)

	print(colors)

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
		print(colors)

	print("Bags", bags)

	ShowAnswer(len(bags))

#########################################
#########################################

def PartB():
	StartPartB()
	TestDataB()

	ShowAnswer("?")

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
