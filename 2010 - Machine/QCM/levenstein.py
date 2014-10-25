#!/usr/bin/env python
import sys


def edition(n,m,a,b):
    "Calculates the Levenshtein distance between a and b."
    if a==b: return 0
    if n > m:
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]

if __name__=="__main__":
    N1 = int(raw_input())
    N2 = int(raw_input())
    s1 = raw_input()
    s2 = raw_input()


    print edition(N1, N2, s1,s2)