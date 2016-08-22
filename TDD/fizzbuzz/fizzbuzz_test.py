import unittest
from fizzbuzz import fizz_buzz

class FizzBuzzTests(unittest.TestCase):

	"""
	Test Cases fro FizzBuzz
	"""
	def test_fizz(self):
		"""
		Test if n is divisible by 3 (Output "Fizz")
		"""
		self.assertEqual(fizz_buzz(6), "Fizz", msg="Failed 'Fizz' test i.e Not Divisible by 3")

	def test_buzz(self):
		"""
		Test if n is divisible by 3 (Output "Fizz")
		"""
		self.assertEqual(fizz_buzz(6), "Fizz", msg="Failed 'Fizz' test i.e Not Divisible by 3")


	def test_fizzbuzz(self):
		"""
		Test if n is divisible by bth 3 and 5
		"""
		self.assertEqual(fizz_buzz(15), "FizzBuzz", msg="Not Divisible by both 3 and 5")

	def test_fizzbuzz_string(self):
		"""
		Test if input is string
		"""
		with self.assertRaises(TypeError):
			fizz_buzz("kim")

if __name__== "__main__":
	unittest.main()