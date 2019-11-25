#!/usr/bin/python3
import sys
if len(sys.argv) != 2:
	sys.exit("Program takes one argument, N")
if not sys.argv[1].isnumeric():
	sys.exit("Argument must be unsigned integer")
N=int(sys.argv[1])
steps=0
while N != 1:
	print(N)
	steps += 1
	if N%2 == 0:
		N=N//2
	else:
		N = 3*N+1
print("steps=",steps)
