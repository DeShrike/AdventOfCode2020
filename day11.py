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

def CountNeighbours(grid, x: int, y: int) -> int:
	deltas = [ (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1) ]
	occupied = 0
	for d in deltas:
		nx = x + d[0]
		ny = y + d[1]
		if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
			occupied += (1 if grid[ny][nx] == 1 else 0)
	return occupied

def Evolve(grid):
	newgrid = [[x for x in y] for y in grid]
	stable = True

	for y in range(len(grid)):
		for x in range(len(grid[0])):
			this = grid[y][x]
			if this == -1:
				continue
			n = CountNeighbours(grid, x, y)
			if n == 0 and this == 0:
				newgrid[y][x] = 1
				stable = False
			elif this == 1 and n >= 4:
				newgrid[y][x] = 0
				stable = False

	return newgrid, stable

def PrintGrid(grid):
	for y in grid:
		for x in y:
			print("#" if x == 1 else ("L" if x == 0 else "."), end = "")
		print("")
	print("")

#########################################
#########################################

def PartA():
	StartPartA()
	# TestDataA()
	
	gen = 0
	grid = BuildGrid()
	# PrintGrid(grid)
	stable = False
	while stable == False:
		gen += 1
		grid, stable = Evolve(grid)
		# PrintGrid(grid)

	occupied = sum([y.count(1) for y in grid])

	ShowAnswer(occupied)

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
