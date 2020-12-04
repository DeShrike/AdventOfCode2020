from aochelper import *
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
	# Invalid: 4
	inputdata.append("eyr:1972 cid:100")
	inputdata.append("hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926")
	inputdata.append("")
	inputdata.append("iyr:2019")
	inputdata.append("hcl:#602927 eyr:1967 hgt:170cm")
	inputdata.append("ecl:grn pid:012533040 byr:1946")
	inputdata.append("")
	inputdata.append("hcl:dab227 iyr:2012")
	inputdata.append("ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277")
	inputdata.append("")
	inputdata.append("hgt:59cm ecl:zzz")
	inputdata.append("eyr:2038 hcl:74454a iyr:2023")
	inputdata.append("pid:3556412378 byr:2007")
	inputdata.append("")
	# Valid: 4
	inputdata.append("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980")
	inputdata.append("hcl:#623a2f")
	inputdata.append("")
	inputdata.append("eyr:2029 ecl:blu cid:129 byr:1989")
	inputdata.append("iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm")
	inputdata.append("")
	inputdata.append("hcl:#888785")
	inputdata.append("hgt:164cm byr:2001 iyr:2015 cid:88")
	inputdata.append("pid:545766238 ecl:hzl")
	inputdata.append("eyr:2022")
	inputdata.append("")
	inputdata.append("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719")

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

	def is_valid_A(self) -> bool:
		return self.is_complete() or self.is_only_missing_optional_field()

	def is_valid_byr(self) -> bool:
		value = self.fields["byr"]
		return value.isnumeric() and int(value) >= 1920 and int(value) <= 2002

	def is_valid_iyr(self) -> bool:
		value = self.fields["iyr"]
		return value.isnumeric() and int(value) >= 2010 and int(value) <= 2020

	def is_valid_eyr(self) -> bool:
		value = self.fields["eyr"]
		return value.isnumeric() and int(value) >= 2020 and int(value) <= 2030

	def is_valid_hgt(self) -> bool:
		value = self.fields["hgt"]
		if value[-2:] == "cm":
			height = value[0:-2]
			return height.isnumeric() and int(height) >= 150 and int(height) <= 193
		elif value[-2:] == "in":
			height = value[0:-2]
			return height.isnumeric() and int(height) >= 59 and int(height) <= 76
		else:
			return False
	
	def is_valid_hcl(self) -> bool:
		value = self.fields["hcl"]
		rx = re.compile("#[0-9a-f]{6}")
		return rx.search(value) is not None

	def is_valid_ecl(self) -> bool:
		value = self.fields["ecl"]
		return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	
	def is_valid_pid(self) -> bool:
		value = self.fields["pid"]
		return value.isnumeric() and len(value) == 9

	def is_valid_B(self) -> bool:
		return self.is_valid_A() and self.is_valid_byr() and self.is_valid_iyr() and self.is_valid_eyr() and self.is_valid_hgt() and self.is_valid_hcl() and self.is_valid_ecl() and self.is_valid_pid()

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
	# TestDataA()

	passports = CreatePassports()

	valid_passwords = 0
	for p in passports:
		# print(p)
		if p.is_valid_A():
			valid_passwords += 1

	ShowAnswer(valid_passwords)

#########################################
#########################################

def PartB():
	StartPartB()
	# TestDataB()

	passports = CreatePassports()

	valid_passwords = 0
	for p in passports:
		# print(p)
		if p.is_valid_B():
			valid_passwords += 1

	ShowAnswer(valid_passwords)

#########################################
#########################################

def Main():
	StartDay(4)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
