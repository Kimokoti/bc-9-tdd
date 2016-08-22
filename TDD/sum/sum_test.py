import unittest
from my_sum import my_sum

class MySumTests(unittest.TestCase):

	def setUp(self):
		"""
		Setting up
		"""

	def test_sum_of_digits(self):
		"""
		Test sum of digits/numbers
		"""
		self.assertEqual(my_sum(5, 10) , 15 , msg = "Wrong Summation")


	def test_if_string(self):
		"""
		Test if Result type is int
		"""
		with self.assertRaises(TypeError):
			my_sum("gfgfg", "string")

	def test_almost_equal(self):
		"""
		Test if result is almost equal
		"""
		self.assertAlmostEqual(my_sum(12,13.5), 25.5,msg="Result Not almost Equal")


	def test_none_result(self):
		"""
			Test if result is None
		"""
		self.assertIsNotNone(my_sum(11, 14),  msg = "Test if result is None")

	def test_sum_greater(self):
		"""
		Test if summation is Greater than 15
		"""
		self.assertGreater(my_sum(10, 15) ,15, msg = "Test if result is greater than 15")

	def test_sum_is(self):
		"""
		Test if summation is  20
		"""
		self.assertIs(type(my_sum(10,15)), int ,msg = "Result is not 20")



if __name__=="__main__":
	unittest.main()


