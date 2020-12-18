from math import gcd

def modify_bit(self, number: int, bit: int, value: int) -> int: 
	m = 1 << bit
	return (number & ~m) | ((value << bit) & m) 

def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)
