#!/usr/bin/env python3

import sys
import string

def text_analyzer(text):
	"""This function counts the number of upper characters, 
	lower characters, punctuation and spaces in a given text."""

	if text == None:
		text = input("What is the text to analyze?\n>> ")

	if not (isinstance(text, str)):
		raise AssertionError("argument is not a string")
		# print("AssertionError: argument is not a string")
		# return

	lower_count = 0
	upper_count = 0
	punct_count = 0
	space_count = 0
	total_count = len(text)

	for char in text:
		if char.islower():
			lower_count += 1
		elif char.isupper():
			upper_count += 1
		elif char in string.punctuation:
			punct_count += 1
		elif char.isspace():
			space_count += 1

	print(f"The text contains {total_count} printable character(s):")
	print(f"- {upper_count} upper letter(s)")
	print(f"- {lower_count} lower letter(s)")
	print(f"- {punct_count} punctuation mark(s)")
	print(f"- {space_count} space(s)")


if __name__ == "__main__":
	if len(sys.argv) > 2:
		print("Error: too many arguments.")
		sys.exit()

	elif len(sys.argv) == 2:
		try:
			text_analyzer(sys.argv[1])
		except AssertionError as e:
			print(e)

	else:
		text_analyzer()
