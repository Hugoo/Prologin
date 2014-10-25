import sys


def chocolats(n, tab):
    tot = 0
    n = 0
    for i in tab:
        if i%2==0:
            tot+=i
            n+=1
    if n!=0:
        return tot/n
    else:
        return 0


if __name__ == '__main__':
    n = int(raw_input())
    tab = [int(_) for _ in raw_input().split()]

    print chocolats(n, tab)
