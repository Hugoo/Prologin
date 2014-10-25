import sys
from math import *


def py(n,x,y,plan):
    plan[y][x] = 'J'
    
    for i in plan:
        print i
    

    #mettons dans un table les sorties:
    cs = []
    for i in range(0,n):
        if plan[0][i] == '.':
            cs.append([0,i])
    for i in range(1,n-1):
        if plan[i][0] == '.':
            cs.append([i,0])
        if plan[i][n-1] == '.':
            cs.append([i,n])
    for i in range(0,n):
        if plan[n-1][i] == '.':
            cs.append([n-1,i])
            
    d = 0
    dt = 0
    for i in cs:
        dt = round(sqrt((i[0]-y)*(i[0]-y)+(i[1]-x)*(i[1]-x)))
        if dt>=d:
            d=dt

    print dt
        


    return


if __name__ == '__main__':
    #n = int(raw_input())
    #x = int(raw_input())
    #y = int(raw_input())
    #plan = [list(raw_input()) for i in xrange(n)]


    n = 4
    x = 1
    y = 1
    plan = [['X','X','X','X'],['X','.','.','X'],['X','.','.','X'],['X','X','X','x']]
    py(n,x,y,plan)
