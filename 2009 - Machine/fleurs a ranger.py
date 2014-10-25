import sys


def rangement(n, list):
    list.sort()
    pair = n/2
    if (n-pair)!=pair:
        pair = n - pair
    
    return list[pair-1]


if __name__ == '__main__':
    n = int(raw_input())
    list = [int(_) for _ in raw_input().split()]


    print rangement(n, list);
