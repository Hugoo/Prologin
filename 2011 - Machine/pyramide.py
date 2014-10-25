import sys


def pyramide(n):
    for i in range(n):
        n = 0
        s="*"
        while n<i:
            s+="*"
            n+=1
        print s
    return


if __name__ == '__main__':
    n = int(raw_input())

    pyramide(n)
