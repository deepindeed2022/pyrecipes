#! /usr/bin/env python2.7

import threading
from time import sleep, ctime

loops = [4, 4]
class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name 
        self.func = func
        self.args = args 
    def __call__(self):
        apply(self.func, self.args)

def loop(nloop, nsec):
    print "start loop ", nloop, "at:", ctime()
    a = 0
    for i in xrange(30000000):
        a += i
    print a
    print "loop ", nloop, "done at:", ctime()


def main_with_muilt_thread():
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop,(i, loops[i]),loop.__name__))
        threads.append(t)
    # decide return main thread
    print "starting at:", ctime()
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print "all DONE at:", ctime()
def main():
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop,(i, loops[i]),loop.__name__))
        threads.append(t)
    # decide return main thread
    print "starting at:",ctime()
    for i in nloops:
        loop(i, loops[i])
    print "all DONE at:",ctime()
if __name__ == '__main__':
    main()
    main_with_muilt_thread()
