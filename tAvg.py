import unittest

import avg

class test(unittest.TestCase):
	inList = [1,2,3]
	length = 3
	
	#testCases
	def test_empty(self):
		self.assertFalse(inlist)

	def test_divZ(self):
		self.assertEqual(length,0)
		res=avg.avg(inList, length)

	def test_type(self):
		res=avg.avg(inList,length)
		self.assertIsinstance(res,int)
