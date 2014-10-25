def decal(ligne):
    l = len(ligne)
    i = 0
    ligner = []
    for i in range(0,l):
        if i==0: ligner.append(ligne[l-1])
        ligner.append(ligne[i-1])
    ligner.pop(0)
    return ligner

if __name__ == '__main__':
    ligne = ['P','R','O','L','O','G','I','N','o']
    print decal(ligne)
