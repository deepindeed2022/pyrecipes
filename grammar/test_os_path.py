import os.path
import os

def test_ospath():
	path = "./testcase/folder2/1.txt"
	assert os.path.exists(os.path.abspath(path))
	assert not os.path.exists(path+"hhhh")

if __name__ == '__main__':
	print os.sep
	print os.name

#	print os.uname()
	test_ospath()