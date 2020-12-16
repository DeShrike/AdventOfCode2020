from aochelper import *
import math
import re

#########################################
#########################################

# Day 16
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("class: 1-3 or 5-7")
	inputdata.append("row: 6-11 or 33-44")
	inputdata.append("seat: 13-40 or 45-50")
	inputdata.append("")
	inputdata.append("your ticket:")
	inputdata.append("7,1,14")
	inputdata.append("")
	inputdata.append("nearby tickets:")
	inputdata.append("7,3,47")
	inputdata.append("40,4,50")
	inputdata.append("55,2,20")
	inputdata.append("38,6,12")

def TestDataB():
	inputdata.clear()
	inputdata.append("class: 0-1 or 4-19")
	inputdata.append("row: 0-5 or 8-19")
	inputdata.append("seat: 0-13 or 16-19")
	inputdata.append("")
	inputdata.append("your ticket:")
	inputdata.append("11,12,13")
	inputdata.append("")
	inputdata.append("nearby tickets:")
	inputdata.append("3,9,18")
	inputdata.append("15,1,5")
	inputdata.append("5,14,9")

#########################################
#########################################

def Parse():
	rules = {}	# field: ( (min1, max1), (min2, max2) )
	your = None
	nearby = []
	nextyour = False
	nextnearby = False
	rx = re.compile(f"(?P<field>[a-z ]*): (?P<min1>[0-9]*)-(?P<max1>[0-9]*) or (?P<min2>[0-9]*)-(?P<max2>[0-9]*)")
	for line in inputdata:
		match = rx.match(line)
		if match:
			field = match["field"]
			min1 = int(match["min1"])
			max1 = int(match["max1"])
			min2 = int(match["min2"])
			max2 = int(match["max2"])
			rules[field] = ( (min1, max1), (min2, max2) )
		elif line == "your ticket:":
			nextyour = True
		elif line == "nearby tickets:":
			nextnearby = True
		elif nextyour:
			your = [int(x) for x in line.split(",")]
			nextyour = False
		elif nextnearby:
			nearby.append([int(x) for x in line.split(",")])

	return rules, your, nearby

def IsValidForRule(value, rule):
	valid = rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]  
	# print(f"Value: {value} : {rule} : {valid}")
	return valid

def IsValidAny(value, rules):
	for rule in rules:
		if IsValidForRule(value, rules[rule]):
			return True
	return False

#########################################
#########################################

def PartA():
	StartPartA()
	#TestDataA()

	rules, your, nearby = Parse()

	# print(rules)
	# print(your)
	# print(nearby)

	error_rate = 0

	for near in nearby:
		for val in near:
			if IsValidAny(val, rules) == False:
				error_rate += val

	ShowAnswer(error_rate)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestDataB()

	rules, your, nearby = Parse()

	nearbyvalid = []
	for near in nearby:
		valid = True
		for val in near:
			if IsValidAny(val, rules) == False:
				valid = False
		if valid:
			nearbyvalid.append(near)

	# print(nearbyvalid)

	valid_col_per_field = {} # {field: [columnindex, columnindex, ...]}

	for fix in range(len(nearbyvalid[0])):
		for key in rules:
			rule = rules[key]
			validforallnearby = True
			for near in nearbyvalid:
				value = near[fix]
				if IsValidForRule(value, rule) == False:
					validforallnearby = False
					break
			if validforallnearby: 
				if key not in valid_col_per_field:
					valid_col_per_field[key] = []
				valid_col_per_field[key].append(fix)

	# print(valid_col_per_field)

	done = []
	while True:
		one = None
		value = None
		for v in valid_col_per_field:
			a = valid_col_per_field[v]
			if len(a) == 1 and v not in done:
				one = v
				done.append(one)
				value = a[0]

		if one is None:
			break

		for v in valid_col_per_field:
			if v != one:
				a = valid_col_per_field[v]
				if value in a:
					a.remove(value)

	# print("After clean:")
	# print(valid_col_per_field)

	answer = 1
	for v in valid_col_per_field:
		rule = valid_col_per_field[v]
		if v[0:9] == "departure":
			myvalue = your[rule[0]]
			answer *= myvalue

	ShowAnswer(answer)

#########################################
#########################################

def Main():
	StartDay(16)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()


"""
{
'departure date': [0, 1, 3, 4, 8, 9, 10, 11, 12, 13, 17, 18, 19], 
'arrival station': [0, 1, 2, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19], 
'class': [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19], 
'price': [0, 1, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 17, 18, 19], 
'route': [0, 1, 3, 4, 6, 8, 9, 10, 11, 12, 13, 17, 18, 19], 
'row': [0, 1, 3, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19], 
'type': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 
'zone': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19], 
'departure location': [1, 3, 4, 8, 9, 10, 11, 12, 13, 17, 18], 
'departure station': [1, 3, 4, 8, 9, 10, 12, 13, 18], 
'departure platform': [1, 3, 4, 9, 10, 12, 13, 18], 
'departure track': [1, 3, 4, 8, 9, 10, 11, 12, 13, 18], 
'departure time': [1, 3, 4, 8, 9, 10, 11, 12, 13, 17, 18, 19], 
'arrival platform': [1, 3, 4, 9, 12, 13, 18], 
'arrival track': [1, 3, 4, 12, 13, 18], 
'arrival location': [3, 12, 13, 18], 
'duration': [3, 4, 12, 13, 18], 
'seat': [12, 18], 
'wagon': [12, 13, 18], 
'train': [18]
}
"""
