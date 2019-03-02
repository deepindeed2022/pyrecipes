#!/usr/bin/env python

while True:
    try:
        (x, y) = (int(x) for x in raw_input().split())
        print x + y
    except EOFError:
        break