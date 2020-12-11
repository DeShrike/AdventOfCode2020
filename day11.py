from aochelper import *
import math
import re

#########################################
#########################################

# Day 11
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("L.LL.LL.LL")
	inputdata.append("LLLLLLL.LL")
	inputdata.append("L.L.L..L..")
	inputdata.append("LLLL.LL.LL")
	inputdata.append("L.LL.LL.LL")
	inputdata.append("L.LLLLL.LL")
	inputdata.append("..L.L.....")
	inputdata.append("LLLLLLLLLL")
	inputdata.append("L.LLLLLL.L")
	inputdata.append("L.LLLLL.LL")

def TestDataB():
	inputdata.clear()

#########################################
#########################################

def BuildGrid():
	grid = []
	for line in inputdata:
		grid.append( [0 if c == "L" else -1 for c in line] )
	return grid

def Evolve(grid):
	newgrid = [[x for x in y] for y in grid]
	print(newgrid)

#########################################
#########################################

def PartA():
	StartPartA()
	TestDataA()
	
	grid = BuildGrid()
	Evolve(grid)


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
	StartDay(11)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
