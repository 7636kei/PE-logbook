import math

def checkprime(k):
	prime_flag = True
	for i in range(2, 1 + math.ceil(math.sqrt(k))):
		if k % i == 0:
			prime_flag = False
			break
	return prime_flag
    
def sumofprimes(targ_num):
	#find the sum of all primes up to, and excluding, 'targ_num'
	runsum = 0
	if targ_num < 2:
		runsum = 0 #no primes under 2, remember? 🤣
	elif targ_num < 3:
		runsum = 2 #nailed 2
	elif targ_num < 5:
		runsum = 2 + 3 #nailed 3 too
	else:
		runsum = 2 + 3
		seed = 0 #for any prime p > 3, p % 6 = ±1
		while seed < math.floor(targ_num/6):
			seed = seed + 1
			if(checkprime(6*seed - 1) == True):
				runsum = runsum + 6*seed -1
			if(checkprime(6*seed + 1) == True and targ_num > 6*seed + 1):
				runsum = runsum + 6*seed + 1
		return runsum
        
print(sumofprimes(2000000))