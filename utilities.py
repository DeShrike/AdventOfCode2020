from math import gcd
import fcntl, struct, termios

def modify_bit(self, number: int, bit: int, value: int) -> int: 
	m = 1 << bit
	return (number & ~m) | ((value << bit) & m) 

def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)

def terminal_size():
    return struct.unpack('HHHH', fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack('HHHH', 0, 0, 0, 0)))[:2]
