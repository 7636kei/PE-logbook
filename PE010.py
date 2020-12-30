def digitsum(targ_num):
	num_string = str(targ_num)
	run_sum = 0
	for i in range(0, len(num_string)):
		run_sum = run_sum + int(num_string[i])
	return run_sum
	
print(digitsum(2**1000))