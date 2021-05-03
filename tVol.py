import unittest

import volume

class test(unittest.TestCase):

	#testCases
	def test_neg(self):
		result=volume.vol(-3)
		self.assertEqual(result,-27)

	def test_type(self):
		result=volume.vol(-3)
		self.assertIsInstance(result, int)

	def test_complex(self):
		z= complex(4,5)
		result=volume.vol(z)
		self.assertIsInstance(result, complex)
