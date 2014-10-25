import sys


def triangle(N):
    i = 0
    while i<N:
        i2 = 0
        ligne = "4"
        l = 1
        while i2 < i:
            if l == 0:
                ligne=ligne+"4"
                l = 1
            else:
                ligne = ligne + "2"
                l = 0
            i2 = i2 + 1
        i = i + 1
        print ligne



if __name__ == '__main__':
    N = int(raw_input())
    triangle(N);
