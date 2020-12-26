from aochelper import *
import math
import re
from collections import deque

#########################################
#########################################

# Day 23
# https://adventofcode.com/2020

#########################################
#########################################

def TestData():
	inputdata.clear()
	inputdata.append("389125467")

#########################################
#########################################

class Item():
	def __init__(self, value: int):
		self.value = value
		self.next = None
		self.prev = None

class CircularLinkedList():
	def __init__(self):
		self.list = None
		self.length = 0
		self.current = None
		self.saved_current = None
		self.dict = {}

	def Length(self) -> int:
		return self.length

	def Current(self):
		return self.current

	def CurrentValue(self) -> int:
		return self.current.value

	def SaveCurrent(self):
		self.saved_current = self.current

	def RestoreCurrent(self):
		self.current = self.saved_current

	def MoveClockwise(self, count: int = 1):
		for _ in range(count):
			self.current = self.current.next

	def MoveCounterClockwise(self, count: int = 1):
		for _ in range(count):
			self.current = self.current.prev

	def MoveToValue(self, value: int) -> bool:
		item = self.dict[value]
		if item is None:
			return False
		self.current = item
		return True

	def GetItemByOffset(self, offset: int):
		item = self.current
		if offset < 0:
			for _ in range(abs(offset)):
				item = item.pref
		elif offset > 0:
			for _ in range(offset):
				item = item.next
		return item

	def Remove(self, offset: int = 0):
		if self.length == 1:
			item = self.current
			self.dict[item.value] = None
			self.list = None
			self.current = None
			self.length -= 1
			return item

		if offset == 0:
			item = self.current
			self.dict[item.value] = None
			if item == self.list:
				self.list = item.prev
			self.current = self.current.next
			item.prev.next = self.current
			self.current.prev = item.prev
			self.length -= 1
			item.next = item.prev = None
			return item
		else:
			item = self.GetItemByOffset(offset)
			self.dict[item.value] = None
			if item == self.list:
				self.list = item.prev
			item.prev.next = item.next
			item.next.prev = item.prev
			self.length -= 1
			item.next = item.prev = None
			return item

	def Insert(self, value):
		item = Item(value)
		self.dict[value] = item
		if self.list is None:
			self.list = item
			item.next = item
			item.prev = item
			self.current = item
			self.length += 1
		else:
			# 1 <-> 2 <-> C <-> I <-> 3 <-> F
			curr = self.current
			prev = curr
			nexxt = curr.next

			prev.next = item
			item.prev = prev
			item.next = nexxt
			nexxt.prev = item
			self.current = item
			self.length += 1

	def Find(self, value: int):
		return self.dict[value]
		"""
		item = self.current
		while item.value != value:
			item = item.prev
			if item == self.current:
				return None
		return item
		"""

	def MaxValue(self) -> int:
		m = 0
		item = self.current
		while True:
			m = max(m, item.value)
			item = item.next
			if item == self.current:
				break
		return m

	def Print(self):
		item = self.list
		while True:
			if item == self.current:
				print(f"{BrightYellow}{item.value}{Reset} -> ", end = "")
			else:
				print(f"{item.value} -> ", end = "")
			item = item.next
			if item == self.list:
				break
		print("")

		"""
		item = self.list
		while True:
			if item == self.current:
				print(f"{BrightYellow}{item.value}{Reset} -> ", end = "")
			else:
				print(f"{item.value} -> ", end = "")
			item = item.prev
			if item == self.list:
				break
		print("")
		"""

#########################################
#########################################

def Play(ll, turns: int):
	for turn in range(turns):
		if turn % 1000 == 0:
			print(turn, end = "\r")
		# ll.Print()
		#print("Removing")
		c1 = ll.Remove(1).value
		c2 = ll.Remove(1).value
		c3 = ll.Remove(1).value
		# print(f"Picked up: {c1}, {c2}, {c3}")
		targetitem = None
		targetvalue = ll.Current().value
		while targetitem is None:
			targetvalue -= 1
			if targetvalue == 0:
				#print("MaxValue")
				targetvalue = ll.MaxValue()
			#print("Finding")
			targetitem = ll.Find(targetvalue)
		# print(f"Target: {targetvalue}")
		ll.SaveCurrent()
		#print("MovingTo")
		ll.MoveToValue(targetvalue)
		#print("Inserting")
		ll.Insert(c1)
		ll.Insert(c2)
		ll.Insert(c3)
		ll.RestoreCurrent()
		ll.MoveClockwise()

	answera = ""
	ll.MoveToValue(1)
	ll.MoveClockwise()
	while ll.CurrentValue() != 1:
		answera += str(ll.CurrentValue())
		ll.MoveClockwise()

	ll.MoveToValue(1)
	ll.MoveClockwise()
	v1 = ll.CurrentValue()
	ll.MoveClockwise()
	v2 = ll.CurrentValue()
	answerb = v1 * v2

	return answera, answerb

#########################################
#########################################

def PartA():
	StartPartA()
	#TestData()

	ll = CircularLinkedList()	
	for c in inputdata[0]:
		ll.Insert(int(c))
	ll.MoveToValue(int(inputdata[0][0]))

	answer, _ = Play(ll, 100)

	ShowAnswer(answer)

#########################################
#########################################

def PartB():
	StartPartB()
	#TestData()

	ll = CircularLinkedList()	
	for c in inputdata[0]:
		ll.Insert(int(c))

	print("Creating Circular Linked List")
	m = ll.MaxValue() + 1
	for num in range(m, 1_000_000 + 1):			# 1_000_000
		ll.Insert(num)

	ll.MoveToValue(int(inputdata[0][0]))
	print("Starting Game")
	_, answer, = Play(ll, 10_000_000)   # 10_000_000

	ShowAnswer(answer)

#########################################
#########################################

def Main():
	StartDay(23)
	ReadInput()
	PartA()
	PartB()
	print("")

#########################################
#########################################

if __name__ == "__main__":
	Main()
