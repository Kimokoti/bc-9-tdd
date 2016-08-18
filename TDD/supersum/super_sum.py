def super_sum(*args):

	"""
	Takes in variable number of arguments and finds sum of elements
	"""
	total=0
	for x in args:
		if type(x) == list:
			for i in x:
				if type(i) == str or type(i) == dict:
					raise TypeError
				else:
					total =total+i
		elif type(x) == str or type(x) == dict:
			raise TypeError
		else:
			total=total+x
	return total
