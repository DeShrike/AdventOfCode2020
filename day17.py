from aochelper import *
import math

#########################################
#########################################

# Day 17
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append(".#.")
	inputdata.append("..#")
	inputdata.append("###")

#########################################
#########################################

deltas_3d = []
deltas_4d = []

def ShowWorldA(world, size: int, offset: int):
	for z in range(size):
		c = 0
		for y in range(size):
			for x in range(size):
				c += world[z][y][x]
		if c > 0:
			print(f"z = {z - offset}")
			for y in range(size):
				for x in range(size):
					print("#" if world[z][y][x] == 1 else ".", end = "")
				print("")

def ShowWorldB(hyperworld, size: int, offset: int):
	for w in range(size):
		for z in range(size):
			c = 0
			for y in range(size):
				for x in range(size):
					c += hyperworld[w][z][y][x]
			if c > 0:
				print(f"z = {z - offset}, w = {w - offset}")
				for y in range(size):
					for x in range(size):
						print("#" if hyperworld[w][z][y][x] == 1 else ".", end = "")
					print("")

def CountActiveA(world, size: int) -> int:
	count = 0
	for z in range(size):
		for y in range(size):
			for x in range(size):
				count += world[z][y][x]
	return count	

def CountActiveB(hyperworld, size: int) -> int:
	count = 0
	for w in range(size):
		for z in range(size):
			for y in range(size):
				for x in range(size):
					count += hyperworld[w][z][y][x]
	return count	

def CountNeigboursA(world, size: int, x: int, y: int, z: int) -> int:
	count = 0
	for d in deltas_3d:
		xx = x + d[0]
		yy = y + d[1]
		zz = z + d[2]
		if 0 <= xx < size and 0 <= yy < size and 0 <= zz < size:
			count += world[zz][yy][xx]

	return count

def CountNeigboursB(hyperworld, size: int, x: int, y: int, z: int, w: int) -> int:
	count = 0
	for d in deltas_4d:
		xx = x + d[0]
		yy = y + d[1]
		zz = z + d[2]
		ww = w + d[3]
		if 0 <= xx < size and 0 <= yy < size and 0 <= zz < size and 0 <= ww < size:
			count += hyperworld[ww][zz][yy][xx]

	return count

def EvolveA(world, size: int):
	newworld = [ [ [0 for _ in range(size)] for _ in range(size)] for _ in range(size)]
	for z in range(size):
		for y in range(size):
			for x in range(size):
				state = world[z][y][x]
				n = CountNeigboursA(world, size, x, y, z)
				if state == 1:
					if n == 2 or n == 3:
						newworld[z][y][x] = 1
					else:
						newworld[z][y][x] = 0
				elif n == 3:
					if x == 0 or y == 0 or z == 0 or x == size - 1 or y == size - 1 or z == size - 1:
						print("World too small")
					newworld[z][y][x] = 1
	return newworld

def EvolveB(hyperworld, size: int):
	newworld = [ [ [ [0 for _ in range(size)] for _ in range(size)] for _ in range(size)] for _ in range(size)]
	for w in range(size):
		for z in range(size):
			for y in range(size):
				for x in range(size):
					state = hyperworld[w][z][y][x]
					n = CountNeigboursB(hyperworld, size, x, y, z, w)
					if state == 1:
						if n == 2 or n == 3:
							newworld[w][z][y][x] = 1
						else:
							newworld[w][z][y][x] = 0
					elif n == 3:
						if x == 0 or y == 0 or z == 0 or w == 0 or x == size - 1 or y == size - 1 or z == size - 1 or w == size - 1:
							print("HyperWorld too small")
						newworld[w][z][y][x] = 1
	return newworld

#########################################
#########################################

def PartA():
	StartPartA()
	# TestData()

	for z in range(3):
		for y in range(3):
			for x in range(3):
				if (x - 1) != 0 or (y - 1) != 0 or (z - 1) != 0:
					deltas_3d.append( (x - 1, y - 1, z - 1) )

	size: int = 25
	offset: int = size // 2
	world = [ [ [0 for _ in range(size)] for _ in range(size)] for _ in range(size)]

	for y, line in enumerate(inputdata):
		for x, pos in enumerate(line):
			if pos == "#":
				world[0 + offset][y + offset][x + offset] = 1

	# ShowWorld(world, size, offset)

	for i in range(6):
		print(f"Gen {i}", end = "\r")
		world = EvolveA(world, size)

	print(" " * 20, end = "\r")
	answer = CountActiveA(world, size)

	# Attempt 1 : 246 too low

	ShowAnswer(answer)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestData()

	for w in range(3):
		for z in range(3):
			for y in range(3):
				for x in range(3):
					if (x - 1) != 0 or (y - 1) != 0 or (z - 1) != 0 or (w - 1) != 0:
						deltas_4d.append( (x - 1, y - 1, z - 1, w - 1) )

	size: int = 26
	offset: int = (size // 2) - 1
	hyperworld = [ [ [ [0 for _ in range(size)] for _ in range(size)] for _ in range(size)] for _ in range(size)]

	for y, line in enumerate(inputdata):
		for x, pos in enumerate(line):
			if pos == "#":
				hyperworld[0 + offset][0 + offset][y + offset][x + offset] = 1

	for i in range(6):
		print(f"Gen {i}", end = "\r")
		hyperworld = EvolveB(hyperworld, size)

	print(" " * 20, end = "\r")
	answer = CountActiveB(hyperworld, size)

	# Attempt 1 : 1915 Too high

	ShowAnswer(answer)

#########################################
#########################################

def Main():
	StartDay(17)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
