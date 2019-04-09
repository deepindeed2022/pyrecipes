#!-*-encoding:utf-8-*-
import time
import sys
from collections import defaultdict

from util import isvalid_date,get_weekday,isvalid_book_time
from util import workday_price, weekend_price


def get_payment(date, start, end, isCancel):
	weekday = int(get_weekday(date))


	if weekday % 6 == 0:
		payment = 0
		for i in xrange(start, end):
			payment += weekend_price[i]
		return payment*0.5 if isCancel else payment
	else:
		payment = 0
		for i in xrange(start, end):
			payment += workday_price[i]
		return payment*0.25 if isCancel else payment

def format_time(i):
	return '0%d:00' % i if i < 10 else '%d:00' % i


class Record(object):
	def __init__(self, _uid, _site, _date, _start, _end, _isCancel=0):
		self.uid = _uid
		self.site = _site
		self.date = _date
		self.start = _start
		self.end = _end
		self.isCancel = _isCancel
		self.payment = get_payment(self.date, self.start, self.end, self.isCancel)


	def cancel(self):
		self.isCancel = 1
		self.payment = get_payment(self.date, self.start, self.end, self.isCancel)

	def __str__(self):
		if self.isCancel:
			return "%s %s~%s 违约金 %d元" % (self.date, format_time(self.start),
											format_time(self.end), self.payment)
		else:
			return "%s %s~%s %d元" % (self.date, format_time(self.start),
											format_time(self.end), self.payment)

class Manager(object):
	sites = ['A', 'B', 'C', 'D']
	_map = {}
	_init_label = list([1,1,1,1,1,1,1,1,
				  1,0,0,0,0,0,0,0,
				  0,0,0,0,0,0,1,1])
	book = dict()

	def __init__(self):
		for site in Manager.sites:
			Manager._map[site] = dict()
			Manager.book[site] = dict()

	def book_site(self, uid, site, date, start, end):
		hash_key = hash('#'.join([uid, site, date, str(start), str(end)]))
		Manager._map[site].setdefault(date, Manager._init_label[:])

		l = Manager._map[site][date]
		if any(l[start:end]) == 1:
			raise Exception("Error:the booking conflicts with existing bookings!")

		if hash_key in Manager.book[site] and Manager.book[site][hash_key].isCancel:
				raise Exception("Error:You have no right to booking this, you could book another time or site!")

		for i in xrange(start, end):
			l[i] = 1

		Manager.book[site][hash_key] = Record(uid, site, date, start, end)


	def cancel_site(self, uid, site, date, start, end):
		try:
			hash_key = '#'.join([uid, site, date, str(start), str(end)])
			Manager.book[site][hash(hash_key)].cancel()
			for i in xrange(start, end):
				Manager._map[site][date][i] = 0
		except KeyError as e:
			raise e

	def _is_site(self, label):
		return label in sites
	
	def _is_book(self, uid, site, date, start, end):
		hash_key = '#'.join([uid, site, date, str(start), str(end)])
		return hash(hash_key) in book[site]

	def show_income(self):
		total_income = 0
		print "收入汇总"
		print "---"

		for site in Manager.sites:
			print "场地:%s" % site
			income = 0
			for record in Manager.book[site].values():
				print record
				income += record.payment
			print "小计:%d元" % income
			total_income += income
			print 
		print"---"
		print "总计:%d" % total_income

mgr = Manager()
def book(line):
	data = line.split()
	isCancel = False
	try:
		if len(line) == 0:
			mgr.show_income()
		elif len(data) == 5:
			if data[4].strip() == "C":
				isCancel = True
			else:
				raise Exception("Error:the booking is invalid!")
			[uid, date, t_interval, site] = data[:4]
			result = isvalid_book_time(t_interval)
			if (not result) or (not isvalid_date(date)):
				raise Exception("Error:the booking is invalid!")
			else:
				(start, end) = result
				mgr.cancel_site(uid, site, date, start, end)
				print "Success:the booking is cancelled does not exists!"
				
		elif len(data) == 4:
			[uid, date, t_interval, site] = data
			result = isvalid_book_time(t_interval)
			if (not result) or (not isvalid_date(date)):
				raise Exception("Error:the booking is invalid!")
			else:
				(start, end) = result
				mgr.book_site(uid, site, date, start, end)
				print "Success:the booking is accepted!"
		else:
			raise Exception("Error:the booking is invalid!")
	except Exception as e:
		raise e