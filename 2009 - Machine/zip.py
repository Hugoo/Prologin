import sys


def bzip2(n, s, k):
    s2 = s #on fait une copie de s
    i = 0
    s2t = []
    s1t = []
    for i in range(0,n):
        s1t.append(s2[i])
        s2t.append(s2[i])
    s1t.sort()


    #s2t = derniere colonne, en table
    #s1t = premiere colonne, en table

    #on va former des bouts de mots
    bout = []
    for i in range(0,n):
        if i != k-1:
            bout.append(s2t[i]+s1t[i])
    #maintenant quon a chaque bout, on sait que le mot commence par:
    #s1t[k-1]! et se termine par s2t[k-1]

    d = s1t[k-1]
    f = s2t[k-1]

    i = 0
    grille = []
    for i in range(0,n):
        grille.append([s1t[i],'.','.','.','.','.','.',s2t[i]])

    print bout

    #generation de la grille originale.
    grille1 = []
    i = 0
    i2 = 0
    for i in range(0,n):
        grille1.append([])
    for i in range(0,n):
        for i2 in range(0,n):
            grille1[i].append('.')
            
    grille1[0][0] = d
    grille1[0][n-1] = f
    #on a notre grille1 avec 1ere lettre et derniere

    #on va decaler les lettres.
    i = 1
    i2 = 0
    for i in range(1,n):
        grille1[i] = decal(grille1[i-1])
    

    #affichage grille originale:
    print ''
    print "GRILLE ORI"
    for i in grille1:
        print i
    #fin affichage
    #affichage grille ordre alpha:
    print ''
    print "GRILLE ALPHA"
    for i in grille:
        print i
    #fin affichage

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
    #n = int(raw_input())
    #s = raw_input()
    #k = int(raw_input())


    n = 8
    s = 'OGOILRNP'
    k = 7
    print bzip2(n, s, k)
