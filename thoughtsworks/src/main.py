#! /usr/bin/env python 
# -*- coding: utf-8 -*- 
import sys
from book import book

def main():
	while 1:
		line = sys.stdin.readline().strip()
		try:
			book(line)
		except Exception as e:
			print e
if __name__ == '__main__':
	main()
	# test_1= ["Manager.book[site][hash_key]", 
	# 	"U001 2016-06-02 22:00~22:00 A", 
	# 	"U002 2017-08-01 19:00~22:00 A", 
	# 	"U003 2017-08-02 13:00~17:00 B", 
	# 	"U004 2017-08-03 15:00~16:00 C", 
	# 	"U005 2017-08-05 09:00~11:00 D",
	# 	""]
	# for i in test_1:
	# 	try:
	# 		book(i)
	# 	except Exception as e:
	# 		print e