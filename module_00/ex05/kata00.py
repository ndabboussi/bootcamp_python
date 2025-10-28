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



# kata04
# The kata variable is always a tuple that contains, in the following order:
# • 2 non-negative integers containing up to 2 digits
# • 1 decimal
# • 1 integer
# • 1 decimal
# # Put this at the top of your kata04.py file
# kata = (0, 4, 132.42222, 10000, 12345.67)
# Write a program that displays this variable content according to the format shown below:
# $> python3 kata04.py
# module_00, ex_04 : 132.42, 1.00e+04, 1.23e+04
# $> python3 kata04.py | cut -c 10,18
# ,: