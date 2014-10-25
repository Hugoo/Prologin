import sys


def su(n):
    l = len(n)
    t = 0
    for i in range(0,l):
        if n[i]=='4':
            for i2 in range(i,l):
                if n[i2]=='2':
                    t = t+1



    return t


if __name__ == '__main__':
    n = raw_input()

    print su(n)
