from aochelper import *
import math
import re

#########################################
#########################################

# Day 11
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
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

#########################################
#########################################

def BuildGrid():
	grid = []
	for line in inputdata:
		grid.append( [0 if c == "L" else -1 for c in line] )
	return grid

deltas = [ (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1) ]

def CountNeighboursA(grid, x: int, y: int) -> int:
	occupied = 0
	for d in deltas:
		nx = x + d[0]
		ny = y + d[1]
		if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
			occupied += (1 if grid[ny][nx] == 1 else 0)
	return occupied

def CountNeighboursB(grid, x: int, y: int) -> int:
	occupied = 0
	for d in deltas:
		nx = x
		ny = y
		while True:
			nx = nx + d[0]
			ny = ny + d[1]
			if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
				if grid[ny][nx] == 0:
					break
				if grid[ny][nx] == 1:
					occupied += 1
					break
			else:
				break



	return occupied

def EvolveA(grid):
	newgrid = [[x for x in y] for y in grid]
	stable = True

	for y in range(len(grid)):
		for x in range(len(grid[0])):
			this = grid[y][x]
			if this == -1:
				continue
			n = CountNeighboursA(grid, x, y)
			if n == 0 and this == 0:
				newgrid[y][x] = 1
				stable = False
			elif this == 1 and n >= 4:
				newgrid[y][x] = 0
				stable = False

	return newgrid, stable

def EvolveB(grid):
	newgrid = [[x for x in y] for y in grid]
	stable = True

	for y in range(len(grid)):
		for x in range(len(grid[0])):
			this = grid[y][x]
			if this == -1:
				continue
			n = CountNeighboursB(grid, x, y)
			if n == 0 and this == 0:
				newgrid[y][x] = 1
				stable = False
			elif this == 1 and n >= 5:
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
	# TestData()
	
	gen = 0
	grid = BuildGrid()
	stable = False
	while stable == False:
		gen += 1
		grid, stable = EvolveA(grid)
		print(f"Generation: {gen}", end = "\r")

	print("\n")

	occupied = sum([y.count(1) for y in grid])

	ShowAnswer(occupied)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestData()

	gen = 0
	grid = BuildGrid()
	stable = False
	while stable == False:
		gen += 1
		grid, stable = EvolveB(grid)
		print(f"Generation: {gen}", end = "\r")
		# PrintGrid(grid)

	print("\n")

	occupied = sum([y.count(1) for y in grid])

	ShowAnswer(occupied)

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
