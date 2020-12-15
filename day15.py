from aochelper import *
import math
import re

#########################################
#########################################

# Day 15
# https://adventofcode.com/2020

#########################################
#########################################

def TestData1():
	inputdata.clear()
	inputdata.append("0,3,6")	# 436

def TestData2():
	inputdata.clear()
	inputdata.append("3,2,1")	# 438

def TestData3():
	inputdata.clear()
	inputdata.append("3,1,2")	# 1836

#########################################
#########################################

def Run(numbers, count):
	his = { num: [ix + 1] for ix, num in enumerate(numbers) }
	# print(his)
	last = numbers[-1]
	for i in range(len(his) + 1, count + 1):
		if i % 50000 == 0:
			print(f"{i} =  {last} ", end = "\r")
		if last not in his:
			last = 0
			his[last] = [i]	
			# print(i, last)
		else:
			numhis = his[last]
			if len(numhis) > 1:
				newnum = numhis[-1] - numhis[-2]
				if newnum not in his:
					his[newnum] = []	

				last = newnum
				if len(his[last]) >= 2:
					his[last][-2] = his[last][-1]
					his[last][-1] = i
				else:	
					his[last].append(i)

				# print(i, last)
			else:
				last = 0
				if last not in his:
					his[last] = []
				if len(his[last]) >= 2:
					his[last][-2] = his[last][-1]
					his[last][-1] = i
				else:	
					his[last].append(i)
				# print(i, last)
	return last

#########################################
#########################################

def PartA():
	StartPartA()
	# TestData1()
	# TestData2()
	# TestData3()

	numbers = [int(n) for n in inputdata[0].split(",")]
	answer = Run(numbers, 2020)

	ShowAnswer(answer)

#########################################
#########################################

def PartB():
	StartPartB()

	numbers = [int(n) for n in inputdata[0].split(",")]
	answer = Run(numbers, 30_000_000)

	ShowAnswer(answer)

#########################################
#########################################

def Main():
	StartDay(15)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
