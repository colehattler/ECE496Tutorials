import unittest
import code

class TestCases(unittest.TestCase):

	def test_sanity(self):
		self.assertEqual(1, 1)


	'''
	Add your own test cases here
	function name must start with test_
	'''
	
	def test_no_op(self):
		self.asserEqual(2, no_op())
		self.assertEqual(9, no_op(3,3))
		
if __name__ == "__main__":
	unittest.main()
