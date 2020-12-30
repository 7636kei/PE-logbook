import math

def gridpath(length, width):
	# We can do this WLOG, since (W+L)C(W) = (W+L)C(L)
	return math.comb(length + width, length)

print(gridpath(20, 20))