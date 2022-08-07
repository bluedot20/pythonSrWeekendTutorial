def isPrime(num):
    if num>1:
    	if num ==2:
    		return True
    	else:
        	for i in range(2, num):
            	if num%i==0:
                	return False
        	return True



assert(isPrime(11)==True)
assert(isPrime(13)==True)
assert(isPrime(12)==False)