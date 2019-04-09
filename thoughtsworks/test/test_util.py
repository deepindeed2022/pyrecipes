import sys
import unittest
sys.path.append('..')
from src.util import isvalid_book_time, isvalid_date

class TestUtil(unittest.TestCase):
	def test_isvalid_book_time(self):
		testcase = ['10:00~11:00', '11:00~10:00', '11:00~12:10', '8:00~10:00', '12:00~22:00']
		except_value = [(10, 11), False, False, False, (12,22)]
		test_n = len(testcase)
		for i in xrange(test_n):
			result = isvalid_book_time(testcase[i])
			self.assertEquals(except_value[i], result)

	def test_isvalid_date(self):
		testcase = ['2017-06-02', '2012-11-32', '2312-11-29']
		except_value = [True, False, True]
		test_n = len(testcase)
		for i in xrange(test_n):
			result = isvalid_date(testcase[i])
			self.assertEquals(except_value[i], result)
	

if __name__ == '__main__':
    unittest.main()