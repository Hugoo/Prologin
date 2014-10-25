import sys
#FONCTIONNE MAIS TROP LONG !!

def sous_sequence(N, L, s):
    seq = []
    seq_comp = []
    n = 0

    for i in range(0,N-L+1):
        seq.append(s[n:n+L])
        n = n + 1
    n = 0
    seq_comp = list(set(seq))
    seq_comp.sort()
        
    precedent = 0
    
    while n<len(seq_comp)-1:
        if (seq.count(seq_comp[precedent])>=seq.count(seq_comp[n+1])):
            ret = seq_comp[precedent]
        else:
            ret = seq_comp[n+1]
            precedent = n+1
        n = n + 1
    return ret

if __name__ == '__main__':

    N = int(raw_input())
    L = int(raw_input())
    s = raw_input()
    print sous_sequence(N, L, s)
