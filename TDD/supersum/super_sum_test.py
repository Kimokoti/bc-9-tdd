import unittest
from super_sum import super_sum

class SuperSumTests(unittest.TestCase):
	"""
	Tests for function super_sum(*args)
	"""

	def test_equal(self):
		"""
		Test if some of digits is equal to 20
		"""
		self.assertEqual(super_sum(1, 2, 3, 4) ,10 , msg = "Sum not Equal to 10")

	def test_is_not_instance(self):
		"""
		Test if result is Instance of list
		"""
		self.assertIsInstance(super_sum(4, 5, 6), int , msg="Result not Instance of  Integer")

	def test_result_in(self):
		"""
		Test if result is in a list
		"""
		self.assertIn(super_sum(4, 5 , 6), [15, 3, 7, 8],msg = "Result not in List")

	def test_if_none(self):
		"""
		Test if result is Not Equal to None
		"""
		self.assertIsNotNone(super_sum(4, 5, 6), msg = "Result is not Equal to None")

	def test_result_type(self):
		"""
		Test if result is of type int
		"""
		self.assertIs(type(super_sum([2, 4, 5])), int, msg = "Result is Not An Integer")

	def test_equalB(self):
		"""
		Test if some of digits is equal to 30
		"""
		self.assertEqual(super_sum(10, 5, 6, 9),30, msg = "Sum not Equal to 30")

	def test_equalC(self):
		"""
		Test if some of digits is equal to 20
		"""
		self.assertEqual(super_sum([10, 5], 5), 20, msg = "Sum not Equal to 20")

	def test_equalD(self):
		"""
		Test if some of digits is equal to 20
		"""
		self.assertEqual(super_sum([5, 6], [4, 5], 10), 30, msg = "Sum not Equal to 30")

	def test_for_type_error(self):
		"""
		Test if function throws type Error
		"""
		with self.assertRaises(TypeError):
			super_sum("gfgfg", 5, [5, 6, "string"])


if __name__ == "__main__":
	unittest.main()