#!-*-coding:utf-8-*-
import sys
import time
workday_price = {9:30,
				10:30,
				11:30,
				12:50,
				13:50,
				14:50,
				15:50,
				16:50,
				17:50,
				18:80,
				19:80,
				20:60,
				21:60}

weekend_price = {9:40,
				 10:40,
				 11:40,
				 12:50,
				 13:50,
				 14:50,
				 15:50,
				 16:50,
				 17:50,
				 18:60,
				 19:60,
				 20:60,
				 21:60}


def isvalid_date(date):
    try:
    	time.strptime(date[:], "%Y-%m-%d")
        return True
    except:
        return False

def get_weekday(date):
	'''星期日 星期一 星期二 星期三 星期四 星期五 星期六
	     0     1      2     3     4      5      6 
	'''
	return time.strftime("%w", time.strptime(date, "%Y-%m-%d"))


def isvalid_book_time(input):
	try:
		start, end = map(lambda x: map(int, x.split(':', 2)), input.strip().split('~', 2))
		assert start[1] == 0 and end[1] == 0
		assert end[0] > start[0]
		assert start[0] >= 9 and start[0] <= 21
		assert end[0] >= 10 and end[0] <= 22
		return (start[0], end[0])
	except AssertionError as e:
		return False
	except Exception as e:
		return False


