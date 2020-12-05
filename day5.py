from aochelper import *
import math

#########################################
#########################################

# Day 5
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("BFFFBBFRRR") # row 70, column 7, seat ID 567.
	inputdata.append("FFFBBBFRRR") # row 14, column 7, seat ID 119.
	inputdata.append("BBFFBBFRLL") # row 102, column 4, seat ID 820.

#########################################
#########################################

def Parse(line):
	rows = line[0:7]
	seats = line[7:10]
	rb = int(rows.replace("B", "1").replace("F", "0"), 2)
	sb = int(seats.replace("R", "1").replace("L", "0"), 2)
	return rb * 8 + sb

#########################################
#########################################

def PartA():
	StartPartA()
	# TestDataA()

	highest = 0
	for line in inputdata:
		seatid = Parse(line)
		highest = max(seatid, highest)

	ShowAnswer(highest)

#########################################
#########################################

def PartB():
	StartPartB()

	answer = None
	seatids = [Parse(line) for line in inputdata]
	seatids.sort()
	for i in range(seatids[-1]):
		if i not in seatids and (i - 1) in seatids and (i + 1) in seatids:
			answer = i
			break

	ShowAnswer(answer)

#########################################
#########################################

def Main():
	StartDay(5)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
