from __future__ import division
import math

def var(vec):
	l = len(vec)
	mean = sum(vec)/l
	for i in xrange(l):
		vec[i] = (vec[i] - mean)**2
	return sum(vec)/(l-1)

def std(vec):
	return math.sqrt(var(vec))

def cov(vec1, vec2):
	l = len(vec1)
	assert l == len(vec2)
	mean1 = sum(vec1)/l 
	mean2 = sum(vec2)/l 
	result = [0.0 for i in xrange(l)]
	for i in xrange(l):
		result[i] = (vec1[i] - mean1)*(vec2[i] - mean2)
	return sum(result)/(l-1)
	
def cor(user1,user2):
	return cov(user1,user2)/(std(user1)*std(user2))

if __name__ == '__main__':
	user1 = [5.0, 3.0, 2.5]
	user2 = [1.0, 3.0, 2.0]
	print cov(user1, user2)
	print cor(user1, user2)