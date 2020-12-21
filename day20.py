from aochelper import *
import math
import re

#########################################
#########################################

# Day 20
# https://adventofcode.com/2020

#########################################
#########################################

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
		self.Reset()
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

			if self.NextConfiguationReal() == False:
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
		
	def NextConfiguationReal(self) -> bool:
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
		self.squaresize = int(math.sqrt(self.tilecount))
		self.picture = [ [None for _ in range(self.squaresize)] for _ in range(self.squaresize) ]
		self.stack = []
		"""
		for t in self.tiles:
			tile = self.tiles[t]
			tile.Reset()
			tile.Print()
		qq = input()
		"""

	def NextTileIndex(self, item) -> int:
		currentindex = item.tileindex + 1
		if currentindex >= self.tilecount:
			return None
		#print(f"Find NextTile from {item.tileindex} ", end ="")
		while self.tiles[currentindex].used:
			currentindex += 1
			if currentindex >= self.tilecount:
				#print("None Found !")
				return None
		self.tiles[currentindex].Reset()
		self.tiles[currentindex].used = True
		#print(f"Found {currentindex}")
		return currentindex

	def Advance(self, item) -> bool:
		# tileid = self.picture[item[1]][item[0]]
		tile = self.tiles[item.tileindex]
		#print(f"Advancening #{tile.id}")
		if tile.NextConfiguation() == False:
			tile.Reset()
			tile.used = False
			nextindex = self.NextTileIndex(item)
			if nextindex is None:
				return False
			item.tileindex = nextindex

		return True

	def FindSpot(self):
		for y in range(self.squaresize):
			for x in range(self.squaresize):
				item = self.picture[y][x]
				if item == None:
					#print(f"Find tile for {x},{y}     {lastid}")
					for index in range(self.tilecount):
						tile = self.tiles[index]
						if tile.used:
							continue
						#print(f"Checking tile {tile.id} for {x},{y}")
						tile.Reset()
						tile.used = True
						#print(f"Set {x},{y} to #{tile.id}")
						item = Item(x, y, index)
						return item
					return None
		return None

	def IsValidHorizontal(self, x: int, y: int) -> bool:
		leftitem = self.picture[y][x]
		rightitem = self.picture[y][x + 1]
		if leftitem is None or rightitem is None:
			return True
		left = self.tiles[leftitem.tileindex]
		right = self.tiles[rightitem.tileindex]
		for l, r in zip(left.lines, right.lines):
			if l[-1] != r[0]:
				return False
		return True

	def IsValidVertical(self, x: int, y: int) -> bool:
		topitem = self.picture[y][x]
		bottomitem = self.picture[y + 1][x]
		if topitem is None or bottomitem is None:
			return True
		top = self.tiles[topitem.tileindex]
		bottom = self.tiles[bottomitem.tileindex]
		return top.lines[-1] == bottom.lines[0]

	def IsValid(self) -> bool:
		for y in range(self.squaresize - 1):
			for x in range(self.squaresize - 1):
				if self.IsValidVertical(x, y) == False:
					return False
				if self.IsValidHorizontal(x, y) == False:
					return False
		return True

	def AllDone(self) -> bool:
		for row in self.picture:
			if None in row:
				return False 
		return self.IsValid()

	def Solve(self):
		done = False
		lastlen = 0
		popped = False
		item = Item(0, 0, 0)
		self.Push(item)
		while done == False:

			if self.IsValid() == False or popped:
				popped = False
				lastitem = self.stack[-1]
				#print("Advance ?")
				if self.Advance(lastitem) == False:
					#print("No Advance")
					popped = True
					self.Pop()
			else:
				newitem = self.FindSpot()
				if newitem is None:
					#print("No spot found")
					break
				self.Push(newitem)

			if True:
				l = len(self.stack)
				if lastlen != l:
					lastlen = l
					if l <= 70:
						print(("*" * l) + (" " * 5), end = "\r")	
					else:
						print("..." + ("*" * 70) + f"{l}" + (" " * 5), end = "\r")
	
			if self.AllDone():
				done = True

			if False:
				for y in range(self.squaresize):
					for x in range(self.squaresize):
						item = self.picture[y][x]
						if item is None:
							print(".... .. |", end = "")
						else:
							tile = self.tiles[item.tileindex]
							print(f"{tile.id} {tile.mode:2} |", end = "")
					print("")
				print(self.IsValid())
				for ix in range(self.tilecount):
					tile = self.tiles[ix]
					print(f"{BrightGreen if tile.used else ''}{tile.id}{Reset}|", end = "")
				print("")
				qq = input()

	def Push(self, item):
		self.stack.append(item)
		self.picture[item.y][item.x] = item
		tile = self.tiles[item.tileindex]
		tile.Reset()
		tile.used = True

	def Pop(self):
		if len(self.stack) == 0:
			return None
		item = self.stack.pop()
		tile = self.tiles[item.tileindex]
		tile.used = False
		self.picture[item.y][item.x] = None
		return item

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

def PartA():
	StartPartA()
	TestDataA()		# 9.5 seconds

	tiles = Parse()
	solver = Solver(tiles)
	solver.Solve()

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
	StartDay(20)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
