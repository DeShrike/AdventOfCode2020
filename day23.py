from aochelper import *
import math
import re

#########################################
#########################################

# Day 23
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("389125467")

def TestDataB():
	inputdata.clear()

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

def Play(numbers):
	current = numbers[0]
	for i in range(100):
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

	answer = ""
	ix = numbers.index(1) + 1
	while numbers[ix] != 1:
		answer += str(numbers[ix])
		ix = (ix + 1) % len(numbers)
	return answer

#########################################
#########################################

def PartA():
	StartPartA()
	#TestDataA()

	numbers = [int(c) for c in inputdata[0]]
	answer = Play(numbers)
	ShowAnswer(answer)

#########################################
#########################################

def PartB():
	StartPartB()
	TestDataB()

	ShowAnswer("?")

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
