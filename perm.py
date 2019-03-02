# -*-encoding:utf-8 -*-
"""
Heap's algorithm
Heap's algorithm generates all possible permutations of n objects. 
It was first proposed by B. R. Heap in 1963.[1] 

The algorithm minimizes movement: 
it generates each permutation from the previous one by interchanging 
a single pair of elements; the other n−2 elements are not disturbed. 
In a 1977 review of permutation-generating algorithms, Robert Sedgewick 
concluded that it was at that time the most effective algorithm for 
generating permutations by computer.[2]
reference:
https://en.wikipedia.org/wiki/Heap%27s_algorithm

"""
import time

def generate(l, n):
	if n == 1:
		print l
	else:
		# 输出在[0, n- 2]之间变化的数列
		for i in xrange(n - 1):
			generate(l, n - 1)
			if n % 2 == 0:
				# swap i and n-1
				l[i], l[n-1] = l[n-1], l[i]
			else:
				# swap 0 and n-1
				l[0], l[n-1] = l[n-1], l[0]
		# 输出[0, n- 2]不进行变换的排序
		generate(l, n-1)


def generate_norecursive(l, n):
	c = [0 for _ in xrange(n)]
	print l 
	i = 0
	# i 就是当前队列[0, i]的最后一个元素的坐标
	# c[i]表示当前
	while i < n:
		if c[i] < i:
			if i % 2 == 0:
				l[0], l[i] = l[i], l[0]
			else:
				l[i], l[c[i]] = l[c[i]], l[i]
			print l 
			c[i] += 1
			i = 0
		else:
			c[i] = 0
			i += 1

def generate_backtrack(l, n):
	if n == 1:
		pass #print l
	else:
		for i in xrange(0, n):
			l[i], l[n-1] = l[n-1], l[i]
			generate_backtrack(l, n-1)
			l[i], l[n-1] = l[n-1], l[i]

if __name__ == '__main__':
	looptime = 1
	n = 3
	s = range(1, n+1)
	start = time.time()
	for _ in xrange(looptime): generate(s, n)
	end = time.time()
	print "time:", end - start
	start = time.time()
	for _ in xrange(looptime): generate_backtrack(s, n)
	end = time.time()
	print "time:", end - start
	start = time.time()
	for _ in xrange(looptime): generate_norecursive(s, n)
	end = time.time()
	print "time:", end - start