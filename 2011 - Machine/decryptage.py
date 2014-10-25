import sys


def decryptage(n, s1, m, s2):
    if s1.find(s2)!=-1:
        return 1
    return 0


if __name__ == '__main__':
    n = int(raw_input())
    s1 = raw_input()
    m = int(raw_input())
    s2 = raw_input()

    print decryptage(n, s1, m, s2)
