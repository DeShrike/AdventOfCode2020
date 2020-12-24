from aochelper import *
import math
import re

#########################################
#########################################

# Day 24
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("sesenwnenenewseeswwswswwnenewsewsw")
	inputdata.append("neeenesenwnwwswnenewnwwsewnenwseswesw")
	inputdata.append("seswneswswsenwwnwse")
	inputdata.append("nwnwneseeswswnenewneswwnewseswneseene")
	inputdata.append("swweswneswnenwsewnwneneseenw")
	inputdata.append("eesenwseswswnenwswnwnwsewwnwsene")
	inputdata.append("sewnenenenesenwsewnenwwwse")
	inputdata.append("wenwwweseeeweswwwnwwe")
	inputdata.append("wsweesenenewnwwnwsenewsenwwsesesenwne")
	inputdata.append("neeswseenwwswnwswswnw")
	inputdata.append("nenwswwsewswnenenewsenwsenwnesesenew")
	inputdata.append("enewnwewneswsewnwswenweswnenwsenwsw")
	inputdata.append("sweneswneswneneenwnewenewwneswswnese")
	inputdata.append("swwesenesewenwneswnwwneseswwne")
	inputdata.append("enesenwswwswneneswsenwnewswseenwsese")
	inputdata.append("wnwnesenesenenwwnenwsewesewsesesew")
	inputdata.append("nenewswnwewswnenesenwnesewesw")
	inputdata.append("eneswnwswnwsenenwnwnwwseeswneewsenese")
	inputdata.append("neswnwewnwnwseenwseesewsenwsweewe")
	inputdata.append("wseweeenwnesenwwwswnew")

#########################################
#########################################

# 2 3
# 7 1 4
#   6 5

directions = ["e", "se", "sw", "w", "nw", "ne"]
deltas = [(2, 0), (1, 1), (-1, 1), (-2, 0), (-1, -1), (1, -1)]

def FlipTile(floor, floorsize: int, instructions: str):
	ix = 0
	posx = posy = floorsize // 2
	while ix < len(instructions):
		for dix, direc in enumerate(directions):
			if instructions[ix:ix+len(direc)] == direc:
				posx += deltas[dix][0]
				posy += deltas[dix][1]
				ix += len(direc)
				# floor[posy][posx] = True
	floor[posy][posx] = not floor[posy][posx]

def CountNeighbours(floor, x: int, y: int) -> int:
	count = 0
	for d in deltas:
		if floor[y + d[1]][x + d[0]]:
			count += 1
	return count

def Evolve(floor, floorsize: int):
	newfloor = [[False for _ in range(floorsize)] for _ in range(floorsize)]
	for y in range(1, floorsize - 1):
		for x in range((y % 2) + 2, floorsize - 2, 2):
			newfloor[y][x] = floor[y][x]
			n = CountNeighbours(floor, x, y)
			if floor[y][x] and (n == 0 or n > 2):
				newfloor[y][x] = False
			elif floor[y][x] == False and n == 2:
				newfloor[y][x] = True
	return newfloor

#########################################
#########################################

def PartA():
	StartPartA()
	#TestData()

	floorsize = 100
	floor = [[False for _ in range(floorsize)] for _ in range(floorsize)]

	for line in inputdata:
		FlipTile(floor, floorsize, line)

	black = 0
	for y in floor:
		#for x in y:
		#	print("#" if x else ".", end = "")
		#print("")
		black += y.count(True)

	ShowAnswer(black)

#########################################
#########################################

def PartB():
	StartPartB()
	#TestData()

	floorsize = 250
	floor = [[False for _ in range(floorsize)] for _ in range(floorsize)]

	for line in inputdata:
		FlipTile(floor, floorsize, line)

	for d in range(100):
		floor = Evolve(floor, floorsize)
		black = 0
		for y in floor:
			black += y.count(True)
		print(f"Day {d + 1}: {black}   ", end = "\r")
	print("")

	black = 0
	for y in floor:
		black += y.count(True)

	ShowAnswer(black)

#########################################
#########################################

def Main():
	StartDay(24)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
