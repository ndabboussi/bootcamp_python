#!/usr/bin/env python3
kata = (2019, 9, 25, 12, 30)

import sys

if not isinstance(kata, tuple):
	print("Error: kata is not a tuple.")
	sys.exit()

if len(kata) != 5:
	print("Error: kata must contain exactly 5 elements.")
	sys.exit()

for i, value in enumerate(kata):
	if not isinstance(value, int):
		print(f"Error: element {i} is not an integer.")
		sys.exit()
	if value < 0:
		print(f"Error: element {i} is negative.")
		sys.exit()

# if kata[0] > 9999:
# 	print("Error: first element must have up to 4 digits.")
# 	sys.exit()

# for i in range(1, 5):
# 	if kata[i] > 99:
# 		print(f"Error: element {i} must have up to 2 digits.")
# 		sys.exit()

print(f"{kata[1]:02d}/{kata[2]:02d}/{kata[0]} {kata[3]:02d}:{kata[4]:02d}")