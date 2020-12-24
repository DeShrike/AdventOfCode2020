from aochelper import *
import math
import re

#########################################
#########################################

# Day 20
# https://adventofcode.com/2020

#########################################
#########################################

with_fancy_display = True

def TestDataA():
	inputdata.clear()
	inputdata.append("Tile 2311:")
	inputdata.append("..##.#..#.")
	inputdata.append("##..#.....")
	inputdata.append("#...##..#.")
	inputdata.append("####.#...#")
	inputdata.append("##.##.###.")
	inputdata.append("##...#.###")
	inputdata.append(".#.#.#..##")
	inputdata.append("..#....#..")
	inputdata.append("###...#.#.")
	inputdata.append("..###..###")
	inputdata.append("")
	inputdata.append("Tile 1951:")
	inputdata.append("#.##...##.")
	inputdata.append("#.####...#")
	inputdata.append(".....#..##")
	inputdata.append("#...######")
	inputdata.append(".##.#....#")
	inputdata.append(".###.#####")
	inputdata.append("###.##.##.")
	inputdata.append(".###....#.")
	inputdata.append("..#.#..#.#")
	inputdata.append("#...##.#..")
	inputdata.append("")
	inputdata.append("Tile 1171:")
	inputdata.append("####...##.")
	inputdata.append("#..##.#..#")
	inputdata.append("##.#..#.#.")
	inputdata.append(".###.####.")
	inputdata.append("..###.####")
	inputdata.append(".##....##.")
	inputdata.append(".#...####.")
	inputdata.append("#.##.####.")
	inputdata.append("####..#...")
	inputdata.append(".....##...")
	inputdata.append("")
	inputdata.append("Tile 1427:")
	inputdata.append("###.##.#..")
	inputdata.append(".#..#.##..")
	inputdata.append(".#.##.#..#")
	inputdata.append("#.#.#.##.#")
	inputdata.append("....#...##")
	inputdata.append("...##..##.")
	inputdata.append("...#.#####")
	inputdata.append(".#.####.#.")
	inputdata.append("..#..###.#")
	inputdata.append("..##.#..#.")
	inputdata.append("")
	inputdata.append("Tile 1489:")
	inputdata.append("##.#.#....")
	inputdata.append("..##...#..")
	inputdata.append(".##..##...")
	inputdata.append("..#...#...")
	inputdata.append("#####...#.")
	inputdata.append("#..#.#.#.#")
	inputdata.append("...#.#.#..")
	inputdata.append("##.#...##.")
	inputdata.append("..##.##.##")
	inputdata.append("###.##.#..")
	inputdata.append("")
	inputdata.append("Tile 2473:")
	inputdata.append("#....####.")
	inputdata.append("#..#.##...")
	inputdata.append("#.##..#...")
	inputdata.append("######.#.#")
	inputdata.append(".#...#.#.#")
	inputdata.append(".#########")
	inputdata.append(".###.#..#.")
	inputdata.append("########.#")
	inputdata.append("##...##.#.")
	inputdata.append("..###.#.#.")
	inputdata.append("")
	inputdata.append("Tile 2971:")
	inputdata.append("..#.#....#")
	inputdata.append("#...###...")
	inputdata.append("#.#.###...")
	inputdata.append("##.##..#..")
	inputdata.append(".#####..##")
	inputdata.append(".#..####.#")
	inputdata.append("#..#.#..#.")
	inputdata.append("..####.###")
	inputdata.append("..#.#.###.")
	inputdata.append("...#.#.#.#")
	inputdata.append("")
	inputdata.append("Tile 2729:")
	inputdata.append("...#.#.#.#")
	inputdata.append("####.#....")
	inputdata.append("..#.#.....")
	inputdata.append("....#..#.#")
	inputdata.append(".##..##.#.")
	inputdata.append(".#.####...")
	inputdata.append("####.#.#..")
	inputdata.append("##.####...")
	inputdata.append("##..#.##..")
	inputdata.append("#.##...##.")
	inputdata.append("")
	inputdata.append("Tile 3079:")
	inputdata.append("#.#.#####.")
	inputdata.append(".#..######")
	inputdata.append("..#.......")
	inputdata.append("######....")
	inputdata.append("####.#..#.")
	inputdata.append(".#...#.##.")
	inputdata.append("#.#####.##")
	inputdata.append("..#.###...")
	inputdata.append("..#.......")
	inputdata.append("..#.###...")

def TestDataB():
	inputdata.clear()

#########################################
#########################################

class Tile():
	def __init__(self, id: int):
		self.id = id
		self.original = []
		self.lines = []
		self.rotation = 0	# 0-3
		self.fliph = False
		self.flipv = False
		self.used = False
		self.mode = 0
		self.numconfiurations = 0
		self.bottoms = []
		self.tops = []
		self.rights = []
		self.lefts = []

	def CurrentLeft(self):
		return self.lefts[self.mode]

	def CurrentRight(self):
		return self.rights[self.mode]

	def CurrentTop(self):
		return self.tops[self.mode]

	def CurrentBottom(self):
		return self.bottoms[self.mode]

	def CalculateValueHor(self, lineindex:int) -> int:
		l = self.lines[lineindex]
		l = l.replace(".", "0").replace("#", "1")
		return int(l, 2)

	def CalculateValueVer(self, colindex:int) -> int:
		s = ""
		for i in self.lines:
			s += i[colindex]
		s = s.replace(".", "0").replace("#", "1")
		return int(s, 2)

	def Prepare(self):
		self.ResetReal()
		while True:
			self.numconfiurations += 1

			# Calculating top border
			top = self.CalculateValueHor(0)
			self.tops.append(top)

			# Calculating bottom border
			bottom = self.CalculateValueHor(-1)
			self.bottoms.append(bottom)

			# Calculating left border
			left = self.CalculateValueVer(0)
			self.lefts.append(left)

			# Calculating right border
			right = self.CalculateValueVer(-1)
			self.rights.append(right)

			if self.NextConfigurationReal() == False:
				break

		"""
		self.Print()
		print(self.numconfiurations)
		print(f"Tops:    {self.tops}")
		print(f"Bottoms: {self.bottoms}")
		print(f"Lefts:   {self.lefts}")
		print(f"Rights:  {self.rights}")
		q = input()
		"""

	def ToOriginal(self):
		self.lines = self.original[:]

	def Reset(self):
		self.mode = 0

	def ResetReal(self):
		self.ToOriginal()
		self.fliph = False
		self.flipv = False
		self.rotation = 0
		self.mode = 0

	def NextConfiguration(self) -> bool:
		self.mode += 1
		if self.mode >= self.numconfiurations:
			return False
		return True

	def NextConfigurationReal(self) -> bool:
		self.mode += 1
		if self.fliph and self.flipv:
			self.rotation += 1
			self.fliph = False
			self.flipv = False
			if self.rotation > 3:
				# self.Reset()
				#print("No advance")
				return False
		elif not self.fliph and self.flipv:
			self.flipv = False
			self.fliph = True
		elif self.fliph and not self.flipv:
			self.flipv = True
			self.fliph = True
		else:
			self.flipv = True
			self.fliph = False

		self.ToOriginal()
		for r in range(self.rotation):
			self.Rotate()
		if self.flipv:
			self.FlipVertical()
		if self.fliph:
			self.FlipHorizontal()

		#print(f"Rotate: {self.rotation}  FlipH: {self.fliph}  FlipV: {self.flipv}")
		# self.Print()

		return True

	def Print(self):
		print(f"Tile {self.id}")
		for line in self.lines:
			print(line)
		print("")

	def Rotate(self):
		grid = [ [ x for x in line ] for line in self.lines ]
		N = len(grid)
		for x in range(0, int(N / 2)): 
			for y in range(x, N - x - 1): 
				temp = grid[x][y] 
				grid[x][y] = grid[y][N - 1 - x] 
				grid[y][N - 1 - x] = grid[N - 1 - x][N - 1 - y] 
				grid[N - 1 - x][N - 1 - y] = grid[N - 1 - y][x] 
				grid[N - 1 - y][x] = temp 
		self.lines.clear()
		for y in grid:
			s = ""
			for c in y:
				s += c
			self.lines.append(s)

	def FlipHorizontal(self):
		self.lines.reverse()
	
	def FlipVertical(self):
		self.lines = [line[::-1] for line in self.lines]

	def AddLine(self, line: str):
		self.original.append(line)

def Parse():
	tiles = []
	currenttile = None
	for line in inputdata:
		if line[0:5] == "Tile ":
			tileid = int(line[5:-1])
			currenttile = Tile(tileid)
			tiles.append(currenttile)
		elif line == "":
			continue
		else:
			currenttile.AddLine(line)

	for tile in tiles:
		tile.Prepare()

	return tiles

class Item():
	def __init__(self, x: int, y: int, tileix: int):
		self.x = x
		self.y = y
		self.tileindex = tileix

class Solver():
	def __init__(self, tiles):
		self.tiles = tiles
		self.tilecount = len(self.tiles)
		self.squaresize = int(math.sqrt(self.tilecount)) * 2 + 1
		self.picture = [ [None for _ in range(self.squaresize)] for _ in range(self.squaresize) ]

	def UpdateFancyDisplay(self, x: int, y: int, flush: bool = True ):
		item = self.picture[y][x]
		print(MoveCursor(x + 1, y + 5), end = "")
		if item is None:
			print(".", end = "")
		else:
			tile = self.tiles[item.tileindex]
			print(chr(65 + tile.mode), end = "")
		if flush:
			Flush()

	def InitFancyDisplay(self):
		print(HideCursor, end = "")
		for y in reversed(range(self.squaresize)):
			for x in reversed(range(self.squaresize)):
				self.UpdateFancyDisplay(x, y, False)
		Flush()

	def Solve(self):
		if with_fancy_display:
			self.InitFancyDisplay()

		x = self.squaresize // 2
		y = self.squaresize // 2
		stap = 0
		done = False
		item = Item(x, y, 0)
		self.picture[y][x] = item
		self.UpdateFancyDisplay(x, y)
		circlesize = 1
		while done == False:
			stap += 1

			if with_fancy_display:
				pass

	def AnswerA(self):
		tl_index = self.picture[0][0].tileindex
		tr_index = self.picture[0][-1].tileindex
		bl_index = self.picture[-1][0].tileindex
		br_index = self.picture[-1][-1].tileindex
		tl = self.tiles[tl_index]
		tr = self.tiles[tr_index]
		bl = self.tiles[bl_index]
		br = self.tiles[br_index]
		return tl.id * tr.id * bl.id * br.id

#########################################
#########################################

def Helper(name, kant):
	print(name, len(kant))
	for l in kant:
		print(f"{l}", end = "\t")
	print("")
	for l in kant:
		print(f"{kant[l]}", end = "\t")
	print("")

def PartA():
	StartPartA()
	TestDataA()		# 9.5 seconds

	tiles = Parse()
	solver = Solver(tiles)
	solver.Solve()

	if with_fancy_display:
		print(MoveCursor(1, solver.squaresize + 6), end = "")
		print(ShowCursor, end = "")

	answer = solver.AnswerA()
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
	if with_fancy_display:
		print(ClearScreen, end = "")
		print(MoveCursor(1, 1), end = "")
	StartDay(20)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
