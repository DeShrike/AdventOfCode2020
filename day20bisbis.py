from aochelper import *
import math
import re

#########################################
#########################################

# Day 20
# https://adventofcode.com/2020

#########################################
#########################################

with_fancy_display = False

def TestData():
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

		self.Reset()

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

	def OrientToMode(self, newmode):
		self.ResetReal()
		while self.mode < newmode:
			self.NextConfigurationReal()

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
	def __init__(self, tiles, testmode: bool):
		self.testmode = testmode
		self.tiles = tiles
		self.tilecount = len(self.tiles)
		self.squaresize = int(math.sqrt(self.tilecount)) * 2 - 4
		if self.testmode:
			self.squaresize = 12

		self.picture = [ [None for _ in range(self.squaresize)] for _ in range(self.squaresize) ]
		self.stack = []

		self.minx = 1000
		self.maxx = -1000
		self.miny = 1000
		self.maxy = -1000

		self.path = [ (0, 0) ]
		for radius in range(1, 5 if self.testmode else 13):
			for xx, yy in self.FollowSquareCircle(radius):
				if (xx, yy) not in self.path:
					self.path.append( (xx, yy) )

	def UpdateFancyDisplay(self, x: int, y: int, flush: bool = True):
		item = self.picture[y][x]
		print(MoveCursor(x + 1, y + 5), end = "")
		if item is None:
			print(".", end = "")
		else:
			tile = self.tiles[item.tileindex]
			print(chr(65 + tile.mode), end = "")
		print(MoveCursor(1, 15), end = "")
		if flush:
			Flush()

	def SetFancyDisplayIndicator(self, x: int, y: int):
		print(MoveCursor(x + 1, y + 5), end = "")
		print(f"{BrightRed}?{Reset}", end = "")
		print(MoveCursor(1, 15), end = "")
		Flush()

	def InitFancyDisplay(self):
		print(HideCursor, end = "")
		for y in reversed(range(self.squaresize)):
			for x in reversed(range(self.squaresize)):
				self.UpdateFancyDisplay(x, y, False)
		Flush()

#     12345
#     0   6
#     9 # 1
#     8   2
#     76543

	def FollowSquareCircle(self, size: int):
		for y in range(0, size + 1):
			yield (size, y)
		for x in range(size - 1, -size - 1, -1):
			yield (x, size)
		for y in range(size - 1, -size - 1, -1):
			yield (-size, y)
		for x in range(-size + 1, size + 1):
			yield (x, -size)
		for y in range(-size, 0):
			yield (size, y)		

	def FindTileIndexWithLeftBorder(self, border: int) -> int:
		for ix, t in enumerate(self.tiles):
			if t.used:
				continue
			if border in t.lefts:
				t.mode = t.lefts.index(border)
				return ix
		return None

	def FindTileIndexWithTopBorder(self, border: int) -> int:
		for ix, t in enumerate(self.tiles):
			if t.used:
				continue
			if border in t.tops:
				t.mode = t.tops.index(border)
				return ix
		return None

	def FindTileIndexWithRightBorder(self, border: int) -> int:
		for ix, t in enumerate(self.tiles):
			if t.used:
				continue
			if border in t.rights:
				t.mode = t.rights.index(border)
				return ix
		return None

	def FindTileIndexWithBottomBorder(self, border: int) -> int:
		for ix, t in enumerate(self.tiles):
			if t.used:
				continue
			if border in t.bottoms:
				t.mode = t.bottoms.index(border)
				return ix
		return None
	
	def FindTileIndexWithLeftAndTopBorder(self, leftborder: int, topborder: int) -> int:
		for ix, t in enumerate(self.tiles):
			if t.used:
				continue
			for mode in range(t.numconfiurations):
				if t.lefts[mode] == leftborder and t.tops[mode] == topborder:
					t.mode = mode
					return ix
		return None

	def FindTileIndexWithRightAndTopBorder(self, rightborder: int, topborder: int) -> int:
		for ix, t in enumerate(self.tiles):
			if t.used:
				continue
			for mode in range(t.numconfiurations):
				if t.rights[mode] == rightborder and t.tops[mode] == topborder:
					t.mode = mode
					return ix
		return None

	def FindTileIndexWithRightAndBottomBorder(self, rightborder: int, bottomborder: int) -> int:
		for ix, t in enumerate(self.tiles):
			if t.used:
				continue
			for mode in range(t.numconfiurations):
				if t.rights[mode] == rightborder and t.bottoms[mode] == bottomborder:
					t.mode = mode
					return ix
		return None

	def FindTileIndexWithLeftAndBottomBorder(self, leftborder: int, bottomborder: int) -> int:
		for ix, t in enumerate(self.tiles):
			if t.used:
				continue
			for mode in range(t.numconfiurations):
				if t.lefts[mode] == leftborder and t.bottoms[mode] == bottomborder:
					t.mode = mode
					return ix
		return None

	def FindTileIndexWithLeftAndBottomAndTopBorder(self, leftborder: int, bottomborder: int, topborder: int) -> int:
		for ix, t in enumerate(self.tiles):
			if t.used:
				continue
			for mode in range(t.numconfiurations):
				if t.lefts[mode] == leftborder and t.bottoms[mode] == bottomborder and t.tops[mode] == topborder:
					t.mode = mode
					return ix
		return None

	def FindTileForSpot(self, x: int, y: int):
		n_item = self.picture[y - 1][x]
		s_item = self.picture[y + 1][x]
		e_item = self.picture[y][x + 1]
		w_item = self.picture[y][x - 1]

		n = s = e = w = None
		if n_item is not None:
			n = self.tiles[n_item.tileindex]
		if s_item is not None:
			s = self.tiles[s_item.tileindex]
		if e_item is not None:
			e = self.tiles[e_item.tileindex]
		if w_item is not None:
			w = self.tiles[w_item.tileindex]

		ix = None
		if e is not None and s is None and n is None and w is None:
			# find tile with specific right border 
			ix = self.FindTileIndexWithRightBorder(e.CurrentLeft())
		elif e is None and s is not None and n is None and w is None:
			# find tile with specific bottom border 
			ix = self.FindTileIndexWithBottomBorder(s.CurrentTop())
		elif e is None and s is None and n is not None and w is None:
			# find tile with specific top border 
			ix = self.FindTileIndexWithTopBorder(n.CurrentBottom())
		elif e is None and s is None and n is None and w is not None:
			# find tile with specific left border 
			ix = self.FindTileIndexWithLeftBorder(w.CurrentRight())
		elif e is None and s is None and n is not None and w is not None:
			# find tile with specific left and top border 
			ix = self.FindTileIndexWithLeftAndTopBorder(w.CurrentRight(), n.CurrentBottom())
		elif e is not None and s is None and n is not None and w is None:
			# find tile with specific right and top border 
			ix = self.FindTileIndexWithRightAndTopBorder(e.CurrentLeft(), n.CurrentBottom())
		elif e is not None and s is not None and n is None and w is None:
			# find tile with specific right and bottom border 
			ix = self.FindTileIndexWithRightAndBottomBorder(e.CurrentLeft(), s.CurrentTop())
		elif e is None and s is not None and n is None and w is not None:
			# find tile with specific right and bottom border 
			ix = self.FindTileIndexWithLeftAndBottomBorder(w.CurrentRight(), s.CurrentTop())
		elif e is None and s is not None and n is not None and w is not None:
			# find tile with specific right and bottom and top border 
			ix = self.FindTileIndexWithLeftAndBottomAndTopBorder(w.CurrentRight(), s.CurrentTop(), n.CurrentBottom())
		else:
			return None
		if ix is None:
			return None

		self.tiles[ix].used = True
		item = Item(x, y, ix)
		return item

	def Solve(self):
		if with_fancy_display:
			self.InitFancyDisplay()

		# cx = self.squaresize // 2 + 1
		# cy = self.squaresize // 2 + 1
		cx = 2
		cy = 6
		x, y = self.path[0]
		pathpos = 1
		done = False
		item = Item(x, y, 0)
		self.tiles[item.tileindex].used = True
		self.picture[y + cy][x + cx] = item
		self.stack.append(item)
		if with_fancy_display:
			self.UpdateFancyDisplay(x + cx, y + cy)

		while done == False:
			xx, yy = self.path[pathpos]
			if xx + cx < 0 or yy + cy < 0 or xx + cx >= self.squaresize or yy + cy >= self.squaresize:
				pathpos += 1
				continue
			if with_fancy_display:
				self.SetFancyDisplayIndicator(cx + xx,cy + yy)
			item = self.FindTileForSpot(cx + xx,cy + yy)
			if item is None:
				pass
			else:
				self.minx = min(self.minx, cx + xx)
				self.maxx = max(self.maxx, cx + xx)
				self.miny = min(self.miny, cy + yy)
				self.maxy = max(self.maxy, cy + yy)

				self.picture[cy + yy][cx + xx] = item
				self.stack.append(item)
				if with_fancy_display:
					self.UpdateFancyDisplay(cx + xx, cy + yy)

			pathpos += 1
			if pathpos >= len(self.path):
				done = True

	def AnswerA(self):
		tl_index = self.picture[self.miny][self.minx].tileindex
		tr_index = self.picture[self.miny][self.maxx].tileindex
		bl_index = self.picture[self.maxy][self.minx].tileindex
		br_index = self.picture[self.maxy][self.maxx].tileindex
		tl = self.tiles[tl_index]
		tr = self.tiles[tr_index]
		bl = self.tiles[bl_index]
		br = self.tiles[br_index]
		return tl.id * tr.id * bl.id * br.id

	def BuildImageForPartB(self):
		width = height = int(math.sqrt(self.tilecount)) * (10 - 2)
		image = [[0 for _ in range(width)] for _ in range(height)]
		cy = 0
		for y in range(self.miny, self.maxy + 1):
			cx = 0
			for x in range(self.minx, self.maxx + 1):
				tile = self.tiles[self.picture[y][x].tileindex]
				tile.OrientToMode(tile.mode)
				
				for liney in range(8):
					for linex in range(8):
						image[cy + liney][cx + linex] = tile.lines[liney + 1][linex + 1]
				cx += 8
			cy += 8

		return image

#########################################
#########################################

def RotateImage(image):
	grid = [ [ x for x in line ] for line in image ]
	N = len(grid)
	for x in range(0, int(N / 2)): 
		for y in range(x, N - x - 1): 
			temp = grid[x][y] 
			grid[x][y] = grid[y][N - 1 - x] 
			grid[y][N - 1 - x] = grid[N - 1 - x][N - 1 - y] 
			grid[N - 1 - x][N - 1 - y] = grid[N - 1 - y][x] 
			grid[N - 1 - y][x] = temp 
	image.clear()
	for y in grid:
		s = ""
		for c in y:
			s += c
		image.append(s)

#########################################
#########################################

def PartA():
	StartPartA()
	#TestData()

	tiles = Parse()
	solver = Solver(tiles, False)
	solver.Solve()

	if with_fancy_display:
		print(MoveCursor(1, solver.squaresize + 6), end = "")
		print(ShowCursor, end = "")

	answer = solver.AnswerA()
	ShowAnswer(answer)

def FindMonsters(image, monster_parts):
	monster_height = max([ d[0] for d in monster_parts ])
	monster_width = max([ d[1] for d in monster_parts ])
	found = False
	imagesize = len(image)
	print(imagesize, monster_width, monster_height)
	for y in range(imagesize - monster_height - 2):
		for x in range(imagesize - monster_width - 2):
			match = True
			for delta in monster_parts:
				if image[y + delta[1]][x + delta[0]] != "#":
					match = False
					break
			if match:
				found = True
				for delta in monster_parts:
					image[y + delta[1]][x + delta[0]] = "O"

	return found

#########################################
#########################################

def PartB():
	global with_fancy_display
	StartPartB()
	TestData()

	with_fancy_display = False
	tiles = Parse()
	solver = Solver(tiles, True)
	solver.Solve()

	image = solver.BuildImageForPartB()

	monster = ["                  #",
			   "#    ##    ##    ###",
			   " #  #  #  #  #  #"]

	monster_parts = []
	for y, line in enumerate(monster):
		for x, char in enumerate(line):
			if char == "#":
				monster_parts.append((x, y))

	print(monster_parts)
	a = input()

	while not FindMonsters(image, monster_parts):
		RotateImage(image)

	for iline in image:
		for c in iline:
			print(c, end = "")
		print("")

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
