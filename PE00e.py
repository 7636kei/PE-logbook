def collatz(k):
	if k % 2 == 0:
		return int(k/2)
	else:
		return 3*k + 1

def collatzsieve(ceil_value):
	flaglist = [0] * ceil_value
	def collatzchain(init_value, flag_to_watch=len(flaglist)):
		# initialise a flaglist first, OUTSIDE of this function definition!!
		run_step = 0
		run_value = init_value
		flaglist[run_value - 1] = 1
		while run_value != 1:
			run_value = collatz(run_value)
			run_step = run_step + 1
			if run_value <= flag_to_watch:
				flaglist[run_value - 1] = 1
		return run_step
	
	running_peakroot = 0
	running_peaklength = 0
	running_checklength = 0
	for i in range(0, ceil_value):
		if flaglist[i] == 0:
			running_checklength = collatzchain(i + 1)
			if running_checklength > running_peaklength:
				running_peakroot = i + 1
				running_peaklength = running_checklength
	print (running_peakroot, running_peaklength)
	
collatzsieve(1000000)
	
	