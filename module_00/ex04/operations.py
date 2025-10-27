#!/usr/bin/env python3

import sys

def isInt(input):
	try:
		int(input)
		return True
	except ValueError:
		return False

if len(sys.argv) == 1:
	print("Usage: python operations.py <number1> <number2>")
	print("Example:\fpython operations.py 10 3")
	sys.exit()

elif len(sys.argv) > 3:
	print("AssertionError: too many arguments")
	sys.exit()

elif len(sys.argv) < 3:
	print("AssertionError: too few arguments")
	sys.exit()

elif isInt(sys.argv[1]) and isInt(sys.argv[2]):
	a = int(sys.argv[1])
	b = int(sys.argv[2])

	print(f"{'Sum:':<15}{a + b}")
	print(f"{'Difference:':<15}{a - b}")
	print(f"{'Product:':<15}{a * b}")

	if b == 0:
		print(f"{'Quotient:':<15}{'ERROR (div by zero)'}")
		print(f"{'Remainder:':<15}{'ERROR (mod by zero)'}")
	else:
		print(f"{'Quotient:':<15}{a / b}")
		print(f"{'Remainder:':<15}{a % b}")

else:
	print("AssertionError: only integers")
