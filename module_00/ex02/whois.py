#!/usr/bin/env python3
import sys

if (len(sys.argv) != 2):
    print("Error: enter at least and only 1 number.")
    sys.exit()

arg = sys.argv[1].lstrip("+-")
if (arg.isdigit() == False):
    print("Error: your input should be an integer.")
    sys.exit()

else:
    x = int(arg)
    if x == 0:
        print("I'm Zero")
    elif x % 2 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")