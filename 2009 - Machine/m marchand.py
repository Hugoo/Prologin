#!/usr/bin/python
# -*- coding: utf-8 -*-

def codes_joseph():
    a = 0
    b = 0
    c = 0
    for a in range(0, 8):
        b=a+1
        for b in range(b,9):
            c = b + 1
            for c in range (c,10):
                print '%d%d%d' % (a,b,c) 

    return

if __name__ == '__main__':
    codes_joseph()

