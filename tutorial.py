def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			print ("not a prime")
		else:
			print ("is a prime")


