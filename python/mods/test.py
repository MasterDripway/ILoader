
def genPrimes():
	prime = 0
	while True:
		isprime = True
		for i in range(2,prime):
			if prime % i == 0:
				isprime = False
				break
		if isprime:
			yield prime
		prime += 1
