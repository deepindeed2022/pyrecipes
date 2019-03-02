#!/usr/bin/python 
# -*- coding: utf-8 -*- 

from math import floor, sqrt
'''通过获取pow的值主要是采用了分而治之的思想进行的
'''
def power(x, n):
	if n == 0: 
		return 1;
	v = power(x, n/2)
	if n % 2 == 1: 
		return x*v*v
	else:
		return v*v

def pow(x, n):
	if n < 0 : 
		return float(1)/power(x, -n)
	else:
		return power(x, n)
'''
本题目中主要通过二分查找的方式进行的，关键的地方是更新的条件，
本题目中采用x/mid与mid进行比较的方式，如果mid比较小的话，那么我们就更新left
如果mid比较大的话我们就更新rightvalue
'''
def msqrt(x):
	left = 1 
	right = x / 2
	mid = 0
	last_mid = 0
	if x < 2: return x
	while left <= right:
		mid = left + ((right - left) >> 1)
		if x / mid > mid:
			left = mid +1
			last_mid = mid
		elif x/mid < mid:
			right = mid - 1
		else:
			return mid
	return last_mid

def test_msqrt():
	assert floor(sqrt(2)) == msqrt(2)
	assert floor(sqrt(1000)) == msqrt(1000)
	assert floor(sqrt(10340)) == msqrt(10340)


def test_pow():
	assert 10000000000 == pow(10, 10)
	assert 1024 == pow(2, 10)
	assert pow(2, -1) == 0.5
	assert pow(2, -4) == 0.0625
if __name__ == '__main__':
	test_pow()
	test_msqrt()