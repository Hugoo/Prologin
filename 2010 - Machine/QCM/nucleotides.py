import sys


def nucleotide(N, s):
    f = [0,0,0,0]
    i = 0
    while i<N:
        if (s[i] == 'A'):
            f[0] = f[0] + 1
        if (s[i] == 'T'):
            f[1] = f[1] + 1
        if (s[i] == 'G'):
            f[2] = f[2] + 1
        if (s[i] == 'C'):
            f[3] = f[3] + 1
        i = i + 1
    a = f[0]
    t = f[1]
    g = f[2]
    c = f[3]
    f.sort()
    f.reverse()
    if (f[0] == a):
        r = 'A'
    elif (f[0] == c):
        r = 'C'
    elif (f[0] == g):
        r = 'G'
    else:
        r = 'T'
        
    return r


if __name__ == '__main__':
    N = int(raw_input())
    s = raw_input()

    print nucleotide(N, s)
