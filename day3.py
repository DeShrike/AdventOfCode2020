from aochelper import *

#########################################
#########################################

# Day 3
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("..##.......")
	inputdata.append("#...#...#..")
	inputdata.append(".#....#..#.")
	inputdata.append("..#.#...#.#")
	inputdata.append(".#...##..#.")
	inputdata.append("..#.##.....")
	inputdata.append(".#.#.#....#")
	inputdata.append(".#........#")
	inputdata.append("#.##...#...")
	inputdata.append("#...##....#")
	inputdata.append(".#..#...#.#")

#########################################
#########################################

def CountTrees(dx: int, dy: int):
	trees = 0
	x = y = 0
	width = len(inputdata[0])
	while y < len(inputdata):
		trees += 1 if inputdata[y][x % width] == "#" else 0
		x += dx
		y += dy

	return trees

#########################################
#########################################

def PartA():
	StartPartA()

	trees = CountTrees(3, 1)

	ShowAnswer(trees)

#########################################
#########################################

def PartB():
	StartPartB()

	slopes = [ (1, 1), (3, 1), (5, 1), (7, 1), (1, 2) ]
	product = 1
	for slope in slopes:
		product *= CountTrees(slope[0], slope[1])

	ShowAnswer(product)

#########################################
#########################################

def Main():
	StartDay(3)
	ReadInput()
	# TestData()
	PartA()
	# TestData()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
