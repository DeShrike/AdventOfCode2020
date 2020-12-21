filename = "testdata.txt"

inputdata = []

file = open(filename, "r")
for line in file:
	inputdata.append(line.strip())
file.close()

for line in inputdata:
	print("\tinputdata.append(\"" + line + "\")")
