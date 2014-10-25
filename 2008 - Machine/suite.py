import sys


def suite(n,s):
    p = -1
    fin = ''
    c = 0
    for i in range(0,n+1):
        if i == n:
            if s[i-1]==p:

                fin = fin+str(c)+str(p)
            else:
                fin = fin+str(c)+str(p)
                p = s[i]
                c = 1
            break
        if p == -1:
            p = s[i]
            c = 1
        else:
            if s[i]==p:
                c = c+1
            else:
                fin = fin+str(c)+str(p)
                p = s[i]
                c = 1
    print fin
    return


if __name__ == '__main__':
    n = int(raw_input())
    s = raw_input()


    suite(n,s)
