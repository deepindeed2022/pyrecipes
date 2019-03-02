#!/usr/bin/env python
#!-*- encoding:=utf8 -*-
"""
A TEST FOR PYTHON DECORTE WRAPPER.decorator 
author: clython
date: 2016-09-16
"""
from time import ctime, sleep

def timestamp(func):
	"""NO PARAMETER DECORTOR FOR SET TIMESTAMP FOR FUNCTION RUNNING.
	"""
	def wapper(*argv, **kwgs):
		print "[%s] %s() called" % (ctime(), func.__name__)
		func(*argv, **kwgs)
	return wapper

def logger(_type):
	"""DECORTOR FOR FUNCTION TO SET RUNNING TIME LOG WITH PATAMETER 
	"""
	def decorator(func):
		def wapper(*argv,**kwgs):
			print "[%s] logger(%s)(%s()) called" % (ctime(),_type, func.__name__)
			func(*argv,**kwgs)	
		return wapper
	return decorator


@timestamp
def foo(a ,b):
	print '%d + %d = %d' %(a, b, a + b)

@logger("TEST_DEBUG")
def test(a, b):
	print '%d + %d = %d' %(a, b, a + b)

foo(1, 3)
test(1,2)