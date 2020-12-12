from aochelper import *
import math
import re

#########################################
#########################################

# Day 12
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("F10")
	inputdata.append("N3")
	inputdata.append("F7")
	inputdata.append("R90")
	inputdata.append("F11")

#########################################
#########################################

def ExecuteA(instruction, x: int, y: int, f: int):
	letter = instruction[0]
	num = int(instruction[1:])

	if letter == "N":
		y += num
	elif letter == "S":
		y -= num
	elif letter == "E":
		x += num
	elif letter == "W":
		x -= num
	elif letter == "L":
		f -= num
		if f < 0:
			f += 360
	elif letter == "R":
		f += num
		f = f % 360
	elif letter == "F":
		if f == 0:
			x += num
			pass
		elif f == 90:
			y -= num
			pass
		elif f == 180:
			x -= num
			pass
		elif f == 270:
			y += num
			pass

	return x, y, f

#########################################
#########################################

def ExecuteB(instruction, x: int, y: int, wx: int, wy: int):
	letter = instruction[0]
	num = int(instruction[1:])

	if letter == "N":
		wy += num
	elif letter == "S":
		wy -= num
	elif letter == "E":
		wx += num
	elif letter == "W":
		wx -= num
	elif letter == "L":
		while num > 0:
			wx, wy = -wy, wx
			num -= 90
	elif letter == "R":
		while num > 0:
			wx, wy = wy, -wx
			num -= 90
	elif letter == "F":
		x += num * wx
		y += num * wy

	return x, y, wx, wy

#########################################
#########################################

def PartA():
	StartPartA()
	# TestData()

	minx = 10000000000
	maxx = -10000000000
	miny = 10000000000
	maxy = -10000000000
	
	x = y = f = 0
	for instruction in inputdata:
		x, y, f = ExecuteA(instruction, x, y, f)
		minx = min(x,minx)
		miny = min(y,miny)
		maxx = max(x,maxx)
		maxy = max(y,maxy)
	answer = abs(x) + abs(y)

	# print(f"Extent: X: {minx} to {maxx}, Y: {miny} to {maxy}")	
	
	# Attempt 1 : 1055 Too Low

	ShowAnswer(answer)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestData()

	minx = 10000000000
	maxx = -10000000000
	miny = 10000000000
	maxy = -10000000000

	x = y = 0
	wx = 10
	wy = 1
	for instruction in inputdata:
		x, y, wx, wy = ExecuteB(instruction, x, y, wx, wy)
		# print(f"({x}, {y})  WP: ({wx}, {wy})")
		minx = min(x,minx)
		miny = min(y,miny)
		maxx = max(x,maxx)
		maxy = max(y,maxy)

	answer = abs(x) + abs(y)

	# print(f"Extent: X: {minx} to {maxx}, Y: {miny} to {maxy}")	

	# Attempt 1 : 53857 Too low

	ShowAnswer(answer)

#########################################
#########################################

def Main():
	StartDay(12)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
