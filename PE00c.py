import math

def erathostenes(k):
	#Objective: find all primes no more than k
	sieve = list(range (0, k+1))
	sieveres = math.floor(math.sqrt(k))
	for i in range(1, sieveres + 1):
		if sieve[i] != 0:
			if i == 1:
				sieve[i] = 0
			else:
				for j in range (2, math.floor(k/i) + 1):
					sieve[i*j] = 0
	for i in range(k, -1, -1):
		if sieve[i] == 0:
			del sieve[i]
		continue
	return sieve
	
def factorcount(k):
	base_list = erathostenes(math.floor(math.sqrt(k)))
	exponent_list = [0] * (1 + len(base_list))
	running_dividend = k
	for i in range(0, len(base_list)):
		while running_dividend % base_list[i] == 0:
			running_dividend = running_dividend / base_list[i]
			exponent_list[i] = exponent_list[i] + 1
	if running_dividend > math.sqrt(k):
		exponent_list[len(base_list)] = exponent_list[len(base_list)] + 1
	running_factorcount = 1
	for j in range(0, len(exponent_list)):
		running_factorcount = running_factorcount * (1 + exponent_list[j])
	return running_factorcount
	
def huntriangle(k):
	seedling = 1
	targnum = 1
	while factorcount(targnum) <= k:
		seedling = seedling + 1
		targnum = targnum + seedling
	print(targnum)
    
huntriangle(500)