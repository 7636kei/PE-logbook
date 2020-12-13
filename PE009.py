import math

def tripletproduct(targ_sum):
	#three reserved return variables
	ret_a = 0
	ret_b = 0
	ret_c = 0
	for i in range(0, math.ceil(targ_sum/3)):
		for j in range (0, math.ceil(math.sqrt(targ_sum**2 - i**2))):
			if i**2 + j**2 == (targ_sum - i - j)**2:
				ret_a = i
				ret_b = j
				ret_c = (targ_sum - i - j)
				break
	if ret_a == 0: #nothing found
		print("No triplet found :(")
	else: #we found something
		print("Product=", ret_a * ret_b * ret_c)

tripletproduct(1000)
