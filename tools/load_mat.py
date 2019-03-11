#!/usr/bin/python2.7
#-*-encoding:utf-8-*-
__doc__ = """
加载matlab的数据类型
"""
from scipy import io as matio

def load_matlab_data(name):
	data = matio.loadmat(name)
	verbose = False
	result = dict()
	keys = filter(lambda x: not x.startswith("__"), data.keys())
	for key in keys:
		result[key] = data[key][0]
	return result


if __name__ == '__main__':
	data = load_matlab_data("setid.mat")
	for k, v in data.iteritems():
		print k, v
	with open("labels_names.txt") as fd:
		labels = map(lambda x: x.strip().split(","), fd.readlines())
		for flower in labels:
			print flower[0], flower[1]
		