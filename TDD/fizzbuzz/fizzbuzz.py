def fizz_buzz(n):
	if type(n) not in [int, float]:
		return TypeError
	elif n % 3 == 0 and n % 5 == 0:
		return "FizzBuzz"
	elif n % 3 == 0:
		return "Fizz"
	elif n % 5 == 0:
		return "Buzz"
	else:
		return n

