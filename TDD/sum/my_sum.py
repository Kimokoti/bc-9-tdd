def my_sum(x,y):
	"""
	Takes in two numbers and returns their sum
	"""
	if type(x) == str or type(y) == dict or type(y) == str or type(y) == dict:
		raise TypeError
	else:
		return x + y
	 
