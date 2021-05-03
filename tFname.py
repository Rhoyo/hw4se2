import unittest

import fName

class test(unittest.TestCase):
	first="bob"
	last=" "

	#testCases
	def test_first(self):
		res=fName.full(first,last)
		res=res.split()
		self.assertNotEqual(res[0],first)

	def test_length(self):
		res=fName.full(first,last)
		res=res.split()
		self.assertGreater(len(res),1)

	def test_total(self):
		res=fName.full(first,last)
		self.assertIsInstance(res, str)


			
