
lines = []
lines.append("...#.#.#.#")
lines.append("####.#....")
lines.append("..#.#.....")
lines.append("....#..#.#")
lines.append(".##..##.#.")
lines.append(".#.####...")
lines.append("####.#.#..")
lines.append("##.####...")
lines.append("##..#.##..")
lines.append("#.##...##.")


def Rotate():
	grid = [ [ x for x in line ] for line in lines ]
	N = len(grid)
	for x in range(0, int(N / 2)): 
		for y in range(x, N - x - 1): 
			temp = grid[x][y] 
			grid[x][y] = grid[y][N - 1 - x] 
			grid[y][N - 1 - x] = grid[N - 1 - x][N - 1 - y] 
			grid[N - 1 - x][N - 1 - y] = grid[N - 1 - y][x] 
			grid[N - 1 - y][x] = temp 
	lines.clear()
	for y in grid:
		s = ""
		for c in y:
			s += c
		lines.append(s)

def FlipHorizontal():
	lines.reverse()

def FlipVertical():
	global lines
	lines = [line[::-1] for line in lines]

def Print():
	for line in lines:
		print(line)
	print("")




Print()
Rotate()
print("")
Print()
