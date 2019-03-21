"""
You can verify that the program works using the following Python script, 
assuming a program name of sort1mb.exe. 
See if you can find any inputs which break it!
"""
from subprocess import *
import random

sequence = [random.randint(0, 99999999) for i in xrange(1000000)]

sorter = Popen('sort1mb.exe', stdin=PIPE, stdout=PIPE)
for value in sequence:
    sorter.stdin.write('%08d\n' % value)
sorter.stdin.close()

result = [int(line) for line in sorter.stdout]
print('OK!' if result == sorted(sequence) else 'Error!')