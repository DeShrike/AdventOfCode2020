from aochelper import *
import math
import re

#########################################
#########################################

# Day 21
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("mxmxvkd kfcds sqjhc nhms (contains dairy, fish)")
	inputdata.append("trh fvjkl sbzzf mxmxvkd (contains dairy)")
	inputdata.append("sqjhc fvjkl (contains soy)")
	inputdata.append("sqjhc mxmxvkd sbzzf (contains fish)")

#########################################
#########################################

def Parse():
	combinations = []
	allergens = set()
	foods = set()
	foodslist = []
	for line in inputdata:
		ix = line.index("(")
		ingredients = line[0:ix].strip().split(" ")
		for i in ingredients:
			foods.add(i)
			foodslist.append(i)
		cont = [c.strip() for c in line[ix + 9:-1].split(",")]
		for a in cont:
			allergens.add(a)
		combinations.append( (ingredients, cont) )
	return combinations, allergens, foods, foodslist

#########################################
#########################################

def FindKnownAllergensAndNotUsed():
	combinations, allergens, foods, foodslist = Parse()

	# This is a bit of a mess
	
	foodswith = {}
	for a in allergens:
		ff = []
		for f in combinations:
			if a in f[1]:
				ff.append(f[0])
		foodswith[a] = ff

	foodcommon = {}
	for f in foodswith:
		foodwith = foodswith[f]
		common = set(foodwith[0])
		for fw in foodwith:
			common = common & set(fw)
		foodcommon[f] = common

	knownallergens = {}
	toremove = set()
	hasOne = True
	while hasOne:
		hasOne = False
		for f in foodcommon:
			fc = foodcommon[f]
			if len(fc) == 1:
				hasOne = True
				known = list(fc)[0]
				knownallergens[f] = known
				toremove.add(known)
				for ff in foodcommon:
					ffcc = foodcommon[ff]
					if known in ffcc:
						ffcc.remove(known)
				break

	notused = foods - toremove

	for torem in toremove:
		while torem in foodslist:
			foodslist.remove(torem)

	return knownallergens, foodslist

#########################################
#########################################

def PartA():
	StartPartA()
	#TestData()

	known, notused = FindKnownAllergensAndNotUsed()

	ShowAnswer(len(notused))

#########################################
#########################################

def PartB():
	StartPartB()
	#TestData()

	known, notused = FindKnownAllergensAndNotUsed()

	answer = ""
	for i in sorted(known.keys()):
		answer += known[i] + ","
	answer = answer[:-1]

	ShowAnswer(answer)

#########################################
#########################################

def Main():
	StartDay(21)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
