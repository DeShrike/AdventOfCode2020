from aochelper import *
import math
import re
from collections import deque

#########################################
#########################################

# Day 23
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("389125467")

#########################################
#########################################

def RemoveCW(numbers, current):
	pos = numbers.index(current) + 1
	if pos < len(numbers):
		num = numbers[pos]
		numbers.remove(num)
		return num
	else:
		num = numbers[0]
		numbers.remove(num)
		return num

def ShowNumbers(numbers, current):
	for num in numbers:
		if num == current:
			print(BrightYellow, end = "")
		print(f"{num}{Reset} ", end = "")
	print("")

def Play(numberss, turns: int):
	numbers = []
	for i in numberss:
		numbers.append(i)

	hist = {}

	current = numbers[0]
	for i in range(turns):
		print(f"{i}", end = "\r")
		# ShowNumbers(numbers, current)
		c1 = RemoveCW(numbers, current)
		c2 = RemoveCW(numbers, current)
		c3 = RemoveCW(numbers, current)
		# print(f"Pickup {c1} {c2} {c3}")
		# ShowNumbers(numbers, current)
		dest = current - 1
		while dest not in numbers:
			dest -= 1
			if dest <= 0:
				dest = max(numbers)
		destix = numbers.index(dest)
		# print(f"Target: {dest} {destix}")
		numbers.insert(destix + 1, c3)
		numbers.insert(destix + 1, c2)
		numbers.insert(destix + 1, c1)
		cix = numbers.index(current)
		cix = (cix + 1) % len(numbers)
		current = numbers[cix]
		# ShowNumbers(numbers, current)
		# qq = input()
		# print("")

		ix1 = numbers.index(1)
		if ix1 < len(numbers) - 2:
			deze = (numbers[ix1 + 1], numbers[ix1 + 2])
			if deze in hist:
				hist[deze] += 1
				print(deze, hist[deze])
			else:
				hist[deze] = 1


	answerA = ""
	ix = numbers.index(1) + 1
	while numbers[ix] != 1:
		answerA += str(numbers[ix])
		ix = (ix + 1) % len(numbers)

	ix1 = numbers.index(1)
	answerB = numbers[ix1 + 1] * numbers[ix1 + 2]
	return answerA, answerB

#########################################
#########################################

def PartA():
	StartPartA()
	# TestData()

	numbers = [int(c) for c in inputdata[0]]
	answer, _ = Play(numbers, 100)
	ShowAnswer(answer)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestData()

	numbers = [int(c) for c in inputdata[0]]
	m = max(numbers) + 1
	for num in range(m, 1_000_000 + 1):
		numbers.append(num)
	_, answer, = Play(numbers, 10_000_000)
	ShowAnswer(answer)

#########################################
#########################################

def Main():
	StartDay(23)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
