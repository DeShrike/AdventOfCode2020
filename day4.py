from aochelper import *
import math
import re

#########################################
#########################################

# Day 4
# https://adventofcode.com/2020

#########################################
#########################################

def TestDataA():
	inputdata.clear()
	inputdata.append("ecl:gry pid:860033327 eyr:2020 hcl:#fffffd")
	inputdata.append("byr:1937 iyr:2017 cid:147 hgt:183cm")
	inputdata.append("")
	inputdata.append("iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884")
	inputdata.append("hcl:#cfa07d byr:1929")
	inputdata.append("")
	inputdata.append("hcl:#ae17e1 iyr:2013")
	inputdata.append("eyr:2024")
	inputdata.append("ecl:brn pid:760753108 byr:1931")
	inputdata.append("hgt:179cm")
	inputdata.append("")
	inputdata.append("hcl:#cfa07d eyr:2025 pid:166559648")
	inputdata.append("iyr:2011 ecl:brn hgt:59in")

def TestDataB():
	inputdata.clear()

#########################################
#########################################

class Passport():
	fieldnames = [ "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid" ]
	regexes = [re.compile(f"{fn}\:(?P<field>[#a-z0-9]*)") for fn in fieldnames]
	optional_field = "cid"

	def __init__(self, line: str):
		self.fields = {}
		for regex, fn in zip(self.regexes, self.fieldnames):
			match = regex.search(line)
			if match:
				self.fields[fn] = match["field"]

	def __str__(self) -> str:
		value = ""
		for f in self.fields:
			value += f"{f} = {self.fields[f]} "
		return value

	def is_complete(self) -> bool:
		return len(self.fields) == len(self.fieldnames)

	def is_only_missing_optional_field(self) -> bool:
		return len(self.fields) == len(self.fieldnames) - 1 and self.optional_field not in self.fields

	def is_valid(self) -> bool:
		return self.is_complete() or self.is_only_missing_optional_field()

#########################################
#########################################

def CreatePassports():
	passports = []
	current = ""
	for line in inputdata:
		if line == "":
			p = Passport(current)
			passports.append(p)
			current = ""
		else:
			current = current + " " + line
	
	if current != "":
		p = Passport(current)
		passports.append(p)

	return passports

#########################################
#########################################

def PartA():
	StartPartA()
	passports = CreatePassports()

	valid_passwords = 0
	for p in passports:
		print(p)
		if p.is_valid():
			valid_passwords += 1

	ShowAnswer(valid_passwords)

#########################################
#########################################

def PartB():
	StartPartB()

	ShowAnswer("?")

#########################################
#########################################

def Main():
	StartDay(4)
	ReadInput()
	# TestDataA()
	PartA()
	TestDataB()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
