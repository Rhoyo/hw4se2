import unittest

import fName

class test(unittest.TestCase):
	first="bob"
	last="2"

	#testCases
	def test_first(self):
		res=fName.full(first,last)
		res=res.split()
		self.assertNotEqual(res[0]," ")

	def test_last(self):
		res=fName.full(first,last)
		res=res.split()
		self.assertNotEqual(res[1]," ")

	def test_total(self):
		res=fName.full(first,last)
		self.assertIsInstance(res, str)


			
