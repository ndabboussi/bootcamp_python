#!/usr/bin/env python3
kata = (19, 20, 35, 100)

import sys

if not isinstance(kata, tuple):
	print("Error: Kata is not a tuple.")
	sys.exit()

if len(kata) == 0:
	print("Kata contains 0 numbers, nothing to print.")
	sys.exit()

for i in kata:
	if not isinstance(i, int):
		print("Kata does not only contain intergers.")
		sys.exit()


print(f"The {len(kata)} numbers are: ", end="")
print(", ".join(map(str, kata)))
# for i, value in enumerate(kata):
# 	sep = ", " if i < len(kata) - 1 else "\n"
# 	print(value, end=sep)