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

	def ToOriginal(self):
		self.lines = self.original[:]

	def Reset(self):
		self.ToOriginal()
		self.fliph = False
		self.flipv = False
		self.rotation = 0

	def NextConfiguation(self) -> bool:
		if self.fliph and self.flipv:
			self.rotation += 1
			self.fliph = False
			self.flipv = False
			if self.rotation > 3:
				self.Reset()
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

		# print(f"Rotate: {self.rotation}  FlipH: {self.fliph}  FlipV: {self.flipv}")
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
	tiles = {}
	currenttile = None
	for line in inputdata:
		if line[0:5] == "Tile ":
			tileid = int(line[5:-1])
			currenttile = Tile(tileid)
			tiles[tileid] = currenttile
		elif line == "":
			continue
		else:
			currenttile.AddLine(line)

	return tiles

class Solver():
	def __init__(self, tiles):
		self.tiles = tiles
		self.squaresize = int(math.sqrt(len(self.tiles)))
		self.picture = [ [None for _ in range(self.squaresize)] for _ in range(self.squaresize) ]
		self.stack = []
		self.popped = False
		self.done = False

		"""
		for t in self.tiles:
			tile = self.tiles[t]
			tile.Reset()
			tile.Print()
		qq = input()
		"""

	def Advance(self, item):
		tileid = self.picture[item[1]][item[0]]
		tile = self.tiles[tileid]
		if tile.NextConfiguation() == False:
			return None
		return item

	def FindSpot(self):
		for y in range(self.squaresize):
			for x in range(self.squaresize):
				if self.picture[y][x] == None:
					for t in self.tiles:
						tile = self.tiles[t]
						if tile.used:
							continue
						#print(f"Checking tile {tile.id} for {x},{y}")
						tile.Reset()
						self.picture[y][x] = tile.id
						print(f"Finding tile for {x},{y}")
						while True:
							if self.IsValid():
								print(f"Set {x},{y} to {tile.id}")
								tile.used = True
								# qq = input()
								return (x, y)
							# print("Next ?")
							# q = input()
							if tile.NextConfiguation() == False:
								# print("No Next")
								break
								# return None
							# q = input()

						self.picture[y][x] = None
						# q = input()
					return None
		return None

	def IsValidHorizontal(self, x: int, y: int) -> bool:
		leftid = self.picture[y][x]
		rightid = self.picture[y][x + 1]
		if leftid is None or rightid is None:
			return True
		left = self.tiles[leftid]
		right = self.tiles[rightid]
		for l, r in zip(left.lines, right.lines):
			if l[-1] != r[0]:
				return False

		return True

	def IsValidVertical(self, x: int, y: int) -> bool:
		topid = self.picture[y][x]
		bottomid = self.picture[y + 1][x]
		if topid is None or bottomid is None:
			return True
		top = self.tiles[topid]
		bottom = self.tiles[bottomid]

		print(topid, bottomid)
		top.Print()
		bottom.Print()
		print(top.lines[-1] == bottom.lines[0])
		q  = input()

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

	def GetTile(self, ix):
		return list(self.tiles.values())[ix]	

	def Solve(self):
		initial = 0
		while self.done == False:
			if len(self.stack) == 0:
				item = (0, 0)
				tile = self.GetTile(initial)
				initial += 1
				tile.used = True
				self.picture[0][0] = tile.id
			else:
				item = self.FindSpot()
			if item == None:
				if len(self.stack) == 0:
					print("No solution")
					return
				item = self.stack[-1]
				while True:
					if self.Advance(item):
						if self.IsValid():
							break
					else:
						self.Pop()
						break
			else: 
				self.Push(item)

			print(len(self.stack))	
			if self.AllDone():
				self.done = True

	def SolveX(self):
		while True:
			print("Solve")
			if self.popped:
				print("A")
				self.popped = False
				if len(self.stack) == 0:
					self.done = True

					if self.AllDone():
						print("Found a solution !")
						return

					print("No solution")
					return
				item = self.stack[-Solve]
				item = self.Advance(item)
				if item == None:
					print("Pop 1")
					self.Pop()
					self.popped = True
			else:
				print("B")
				item = self.FindSpot()
				if item == None:
					print("Pop 2")
					item = self.Pop()
					

					tileid = self.picture[item[1]][item[0]]
					tile = self.tiles[tileid]


					self.popped = True
				else:
					print("Push", item)
					self.Push(item)

			for y in self.picture:
				for x in y:
					print(f"{x} ", end = "")
				print("")
			q = input()

	def Push(self, item):
		self.stack.append(item)
		tileid = self.picture[item[1]][item[0]]
		tile = self.tiles[tileid]
		tile.used = True
		# self.picture[item[1]][item[0]] = item

	def Pop(self):
		if len(self.stack) == 0:
			return None
		item = self.stack.pop()
		tileid = self.picture[item[1]][item[0]]
		tile = self.tiles[tileid]
		tile.used = False
		self.picture[item[1]][item[0]] = None
		return item

	def AnswerA(self):
		tl = self.picture[0][0]
		tr = self.picture[0][-1]
		bl = self.picture[-1][0]
		br = self.picture[-1][-1]
		return tl * tr * bl * br

#########################################
#########################################

def PartA():
	StartPartA()
	TestDataA()

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
