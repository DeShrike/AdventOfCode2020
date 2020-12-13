from aochelper import *
from functools import reduce
import math
import re

#########################################
#########################################

# Day 13
# https://adventofcode.com/2020

#########################################
#########################################

def TestData1():
	inputdata.clear()
	inputdata.append("939")
	inputdata.append("7,13,x,x,59,x,31,19")	 # Part 2: 1068788

def TestData2():
	inputdata.clear()
	inputdata.append("0")
	inputdata.append("17,x,13,19")	 # Part 2: 3417

def TestData3():
	inputdata.clear()
	inputdata.append("0")
	inputdata.append("67,7,59,61")	 # Part 2: 754018

def TestData4():
	inputdata.clear()
	inputdata.append("0")
	inputdata.append("67,x,7,59,61")	 # Part 2: 779210

def TestData5():
	inputdata.clear()
	inputdata.append("0")
	inputdata.append("67,7,x,59,61")	 # Part 2: 1261476

def TestData6():
	inputdata.clear()
	inputdata.append("0")
	inputdata.append("1789,37,47,1889")	 # Part 2: 1202161486

#########################################
#########################################

def PartA():
	StartPartA()
	#TestData1()

	starttime = int(inputdata[0])
	busses = [int(id) for id in inputdata[1].split(",") if id != "x"]

	time = starttime
	waittime = 1_000_000
	bestbus = None
	while True:
		for b in busses:
			if time % b == 0:
				wt = time - starttime
				if wt < waittime:
					bestbus = b
					waittime = wt
		if bestbus is not None:
			break
		time += 1

	ShowAnswer(bestbus * waittime)

#########################################
#########################################

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def PartB():
	StartPartB()
	#TestData1()
	#TestData2()
	#TestData3()
	#TestData4()
	#TestData5()
	#TestData6()

	busses = [1 if id == "x" else int(id) for id in inputdata[1].split(",")]
	n = []
	a = []
	d = []
	for ix, b in enumerate(busses):
		if b == 1:
			continue
		n.append(b)
		d.append(ix)
		a.append(b - ix)

	a[0] = 0
	
	#print(n)
	#print(d)
	#print(a)
	
	answer = int(chinese_remainder(n, a))
	#print(answer)
	for aa in a:
		if aa < 0:
			answer -= 1

	# Starting Hack - Brute force from the 'Too Low' to the 'Too high'.
	for s in range(775230782877218, 775230782877403):
		found = True
		for ix, nn in enumerate(n):
			if ((s + d[ix]) % nn) != 0:
				found = False
		if found:
			break
	
	answer = s

	# Attempt 1 : 775230782877218 Too Low
	# Attempt 2 : 775230782877403 Too High
	# Attempt 3 : 775230782877399
	# Attempt 4 : 775230782877256
	# Attempt 5 : 775230782877394
	# Attempt 6 : 775230782877242 = Correct !!!

	ShowAnswer(answer)

#########################################
#########################################

def Main():
	StartDay(13)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
