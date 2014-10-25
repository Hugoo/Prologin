import sys


def stat(n,c):
    s = []
    for i in range(0,26):
        s.append(0)

    for i in range(0,n):
        if c[i]==('a' or 'A'):
            s[0] = s[0]+1
        elif c[i]==('b' or 'B'):
            s[1] = s[1]+1
        elif c[i]==('c' or 'C'):
            s[2] = s[2]+1
        elif c[i]==('d' or 'D'):
            s[3] = s[3]+1
        elif c[i]==('e' or 'E'):
            s[4] = s[4]+1
        elif c[i]==('f' or 'F'):
            s[5] = s[5]+1
        elif c[i]==('g' or 'G'):
            s[6] = s[6]+1
        elif c[i]==('h' or 'H'):
            s[7] = s[7]+1
        elif c[i]==('i' or 'I'):
            s[8] = s[8]+1
        elif c[i]==('j' or 'J'):
            s[9] = s[9]+1
        elif c[i]==('k' or 'K'):
            s[10] = s[10]+1
        elif c[i]==('l' or 'L'):
            s[11] = s[11]+1
        elif c[i]==('m' or 'M'):
            s[12] = s[12]+1
        elif c[i]==('n' or 'N'):
            s[13] = s[13]+1
        elif c[i]==('o' or 'O'):
            s[14] = s[14]+1
        elif c[i]==('p' or 'P'):
            s[15] = s[15]+1
        elif c[i]==('q' or 'Q'):
            s[16] = s[16]+1
        elif c[i]==('r' or 'R'):
            s[17] = s[17]+1
        elif c[i]==('s' or 'S'):
            s[18] = s[18]+1
        elif c[i]==('t' or 'T'):
            s[19] = s[19]+1
        elif c[i]==('u' or 'U'):
            s[20] = s[20]+1
        elif c[i]==('v' or 'V'):
            s[21] = s[21]+1
        elif c[i]==('w' or 'W'):
            s[22] = s[22]+1
        elif c[i]==('x' or 'X'):
            s[23] = s[23]+1
        elif c[i]==('y' or 'Y'):
            s[24] = s[24]+1
        elif c[i]==('z' or 'Z'):
            s[25] = s[25]+1

    for v in s:
        print v
    return


if __name__ == '__main__':
    n = int(raw_input())
    c = raw_input()

    print stat(n,c)
