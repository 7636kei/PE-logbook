import math

def lettercount(num_ceil):
	#count_U20/count_tens have their first 1/2 (resp) indices padded with zeroes!
	#counting capacity: 19999, I guess?
	count_U20 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
	count_tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
	count_hundreds = 7
	count_thousands = 8
	
	run_count = 0
	#sample number: 1984 (one thousand nine hundred and eighty-four)
	for i in range(1, num_ceil + 1):
		if (i % 100 >= 20): #eighty-four
			run_count = run_count + count_tens[math.floor((i%100)/10)] + count_U20[i%10]
		else:
			run_count = run_count + count_U20[i%100]
		if ((i % 100) > 0 and i > 100): #and ...
			run_count = run_count + 3
		if (i % 1000 >= 100): #nine hundred ...
			run_count = run_count + count_hundreds + count_U20[math.floor((i%1000)/100)]
		if (i >= 1000): # one thousand ...
			run_count = run_count + count_thousands + count_U20[math.floor(i/1000)]
	return run_count
	
print(lettercount(1000))
