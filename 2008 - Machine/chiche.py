import sys


def chiche(n,table):
    x = -1
    y = -1
    xv = -1
    yv = -1
    ok = 0
    for i in table:
        print i
        
    for i in table:
        if ok==1:break
        xv = xv + 1
        yv = -1
        
        for i2 in range(0,len(i)):
            yv = yv + 1
            try:
                if i[i2] == 'C':
                    if i[i2+1] == 'H':
                        if i[i2+2] == 'I':
                            if i[i2+3] == 'C':
                                if i[i2+4] == 'H':
                                    if i[i2+5] == 'E':
                                        ok = 1
                                        x = xv
                                        y = yv
                                        break
                                        
            except:
                i = i

    f = (x, y)
    print f
    return


if __name__ == '__main__':
    n = int(raw_input())
    table = [list(raw_input()) for i in xrange(n)]

    chiche(n,table)
