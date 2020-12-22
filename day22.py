from aochelper import *
import math
import functools

#########################################
#########################################

# Day 22
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("Player 1:")
	inputdata.append("9")
	inputdata.append("2")
	inputdata.append("6")
	inputdata.append("3")
	inputdata.append("1")
	inputdata.append("")
	inputdata.append("Player 2:")
	inputdata.append("5")
	inputdata.append("8")
	inputdata.append("4")
	inputdata.append("7")
	inputdata.append("10")

#########################################
#########################################

def Parse():
	p = 0
	players = ([], [])
	for line in inputdata:
		if line == "":
			continue
		if line == "Player 1:":
			p = 0
			continue
		if line == "Player 2:":
			p = 1
			continue
		players[p].append(int(line))
	players[0].reverse()
	players[1].reverse()
	return players

def PlayGame(players):
	turn = 0
	while len(players[0]) > 0 and len(players[1]) > 0:
		turn += 1
		c1 = players[0].pop()
		c2 = players[1].pop()
		if c1 > c2:
			players[0].insert(0, c1)
			players[0].insert(0, c2)
		else:
			players[1].insert(0, c2)
			players[1].insert(0, c1)

	return 0 if len(players[0]) > 0 else 1, turn

totalturns = 0
gamecounter = 0

def PlayRecursiveGame(players):
	global totalturns, gamecounter
	winner = None
	history = [ [], [] ]

	gamecounter += 1
	game = gamecounter

	while winner is None:
		#print(f"Game {game}")
		#print(f"Player 1: {players[0]}")
		#print(f"Player 2: {players[1]}")

		totalturns += 1

		c1 = players[0].pop()
		c2 = players[1].pop()

		# print(f"Player 1 plays: {c1}")
		#print(f"Player 2 plays: {c2}")

		if len(players[0]) >= c1 and len(players[1]) >= c2:

			newcards = [ players[0][-c1:], players[1][-c2:] ]

			subwinner, _ = PlayRecursiveGame(newcards)
			if subwinner == 0:
				# print("Player 1 wins subgame")
				players[0].insert(0, c1)
				players[0].insert(0, c2)
			else:
				# print("Player 2 wins subgame")
				players[1].insert(0, c2)
				players[1].insert(0, c1)

		else:
			if c1 > c2:
				# print("Player 1 wins")
				players[0].insert(0, c1)
				players[0].insert(0, c2)
			else:
				# print("Player 2 wins")
				players[1].insert(0, c2)
				players[1].insert(0, c1)

		if players[0] in history[0] or players[1] in history[1]:
			winner = 0
			break

		history[0].append(players[0][:])
		history[1].append(players[1][:])

		if len(players[0]) == 0:
			winner = 1

		if len(players[1]) == 0:
			winner = 0

	return winner, totalturns

#########################################
#########################################

def PartA():
	StartPartA()
	#TestData()

	players = Parse()
	winner, turns = PlayGame(players)
	score = 0
	for ix, v in enumerate(players[0] + players[1]):
		score += (ix + 1) * v

	print(f"Turns: {turns}")

	ShowAnswer(score)

#########################################
#########################################

def PartB():
	StartPartB()
	#TestData()

	players = Parse()
	winner, turns = PlayRecursiveGame(players)
	score = 0
	for ix, v in enumerate(players[0] + players[1]):
		score += (ix + 1) * v

	print(f"Turns: {turns}")

	ShowAnswer(score)

#########################################
#########################################

def Main():
	StartDay(22)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
