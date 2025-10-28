#!/usr/bin/env python3
kata = (0, 4, 132.42222, 10000, 12345.67)

import sys

if not isinstance(kata, tuple):
	print("Error: kata must be a tuple.")
	sys.exit()

if len(kata) != 5:
	print(f"Error: kata must contain exactly 5 elements, not {len(kata)}.")
	sys.exit()

expected_types = (int, int, float, int, float)
for i, (value, expected_type) in enumerate(zip(kata, expected_types), start=1):
	if not isinstance(value, expected_type):
		print(f"Error: element {i} must be of type {expected_type.__name__}, not {type(value).__name__}.")
		sys.exit()

if any((isinstance(x, (int, float)) and x < 0) for x in kata):
	print("Error: all numeric values must be non-negative.")
	sys.exit()

if kata[0] > 99 or kata[1] > 99:
	print("Error: the first two integers must contain up to 2 digits (0–99).")
	sys.exit()


print("module_0{}, ex_0{} : {:.2f}, {:.2e}, {:.2e}".format(kata[0], kata[1], kata[2], kata[3], kata[4]))