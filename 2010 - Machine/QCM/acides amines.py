import sys

def traduction(N, M, table_traduction, s):
    n_div = N/3
    s_liste = []
    decr = ''
    q = 0
    for i in range(0,n_div):
        for v in table_traduction:
            if (s[q:q+3] == v[0]):
                if (decr == ''):
                    decr = v[1]
                else:
                    decr = decr + ' ' + v[1]
        q = q + 3
    print decr
    return

if __name__ == '__main__':
    N = int(raw_input())
    M = int(raw_input())
    table_traduction = [raw_input().split() for i in range(0,M)]
    s = raw_input()

    traduction(N, M, table_traduction, s)
