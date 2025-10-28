#!/usr/bin/env python3
kata = "The right format"

import sys

if len(kata) <= 42:
	print(kata.rjust(42, "-"), end="%")
	# s = (42 - len(kata)) * "-"
	# print(s + kata, end="")
else:
	print("Variable content is too long (more than 42 len).")