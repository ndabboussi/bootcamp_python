#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print ("Error: No arguments given, please enter at least 1 string.")

else:
    args = sys.argv[1:]
    x = " ".join(args)[::-1].swapcase()
    print(x, end="") 