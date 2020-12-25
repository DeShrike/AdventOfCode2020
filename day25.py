from aochelper import *
import math
import re

#########################################
#########################################

# Day 25
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("5764801")
	inputdata.append("17807724")

def TestDataB():
	inputdata.clear()

#########################################
#########################################

def FindLoopSize(subject_number: int, target: int) -> int:
	val = 1
	ls = 0
	while val != target:
		ls += 1
		val *= subject_number
		val = val % 20201227

	return ls

def Transform(subject_number: int, loopsize: int) -> int:
	val = 1
	for _ in range(loopsize):
		val *= subject_number
		val = val % 20201227

	return val

#########################################
#########################################

def PartA():
	StartPartA()
	# TestDataA()

	card_pk = int(inputdata[0])
	door_pk = int(inputdata[1])

	card_ls = FindLoopSize(7, card_pk)
	door_ls = FindLoopSize(7, door_pk)

	print(card_ls)
	print(door_ls)

	key1 = Transform(door_pk, card_ls)
	key2 = Transform(card_pk, door_ls)

	print(key1)
	print(key2)

	ShowAnswer(key1)

#########################################
#########################################

def PartB():
	StartPartB()
	TestDataB()

	ShowAnswer("?")

#########################################
#########################################

def Main():
	StartDay(25)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
