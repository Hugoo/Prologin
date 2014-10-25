import sys


def summit(n):
    t = 0
    for i in range(0,n+1):
        t = t + i
    return t


if __name__ == '__main__':
    n = int(raw_input())


    print summit(n)
