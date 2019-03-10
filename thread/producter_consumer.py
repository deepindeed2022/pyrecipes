#!/usr/bin/env python2.7

from random import randint
from time import sleep
from Queue import Queue
from myThread import MyThread

def writeQueue(queue):
    print "producing object for Q...", 
    queue.put("xxx", 1)
    print "size now", queue.qsize()

def readQueue(queue):
    val = queue.get(1)
    print "consumed object from Q... size now", queue.qsize()

def writer(queue, loops):
    for i in range(loops):
        writeQueue(queue)
        sleep(randint(1, 3))
def reader(queue, loops):
    for i in range(loops):
        readQueue(queue)
        sleep(randint(2, 50))

funcs = [writer, reader]
nfuncs = range(len(funcs))
def main():
    nloops = randint(2, 40)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops),  funcs[i].__name__)
        threads.append(t)
    for i in nfuncs:
        threads[i].start()
    for i in nfuncs:
        threads[i].join()
    print "all DONE"

if __name__ == '__main__':
    main()