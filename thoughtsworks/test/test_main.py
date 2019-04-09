#! /usr/bin/env python 
# -*- coding: utf-8 -*- 
import sys
sys.path.append('..')
import unittest
from src.book import book




class TestBook(unittest.TestCase):
	def test_book(self):
		test_1= ["Manager.book[site][hash_key]", 
				"U001 2016-06-02 22:00~22:00 A", 
				"U002 2017-08-01 19:00~22:00 A", 
				"U003 2017-08-02 13:00~17:00 B", 
				"U004 2017-08-03 15:00~16:00 C", 
				"U005 2017-08-05 09:00~11:00 D",
				""]
		self.assertRaises(Exception, book, test_1[0])
		self.assertRaises(Exception, book, test_1[1])
		book(test_1[2])
		book(test_1[3])
		book(test_1[4])
		book(test_1[5])
		book(test_1[6])



if __name__ == '__main__':
    unittest.main()
