

import sys


def cook(n, q, pasta):

    dec = 0
    pastas = []
    for pa in pasta:
        pastas.append(pa)
    pastas.sort()
    boitestouse = []
    for ind in pastas:
        if dec>=q: break
        dec = dec + ind[0]
        boitestouse.append(ind)

    if dec!= q:boitesv=len(boitestouse)-1
    else: boitesv = len(boitestouse)

    jtemps = []
    #determinons quel paquet mettre en 1er, c'est celui avec le temps de cuisson le plus long!
    for f in boitestouse:
        jtemps.append(f[1])

    jtemps.sort()
    jtemps.reverse()
    ordre = []
    for temps in jtemps:
        for pate in boitestouse:
            if pate[1]==temps:
                ordre.append(pate)


    base = ordre[0][1]
    print 'Joseph utilisera',len(boitestouse),"paquet(s) et pourra en jeter %s." % boitesv
    print 'Il doit commencer par mettre le paquet %s a cuire.' % pasta.index(ordre[0])
    ordre.pop(0)
    for pack in ordre:
        print 'Il mettra le paquet',pasta.index(pack),'au bout de',base-pack[1],'minute(s).'
    return


if __name__ == '__main__':


    n = int(raw_input())
    q = int(raw_input())
    pasta = [[int(_) for _ in raw_input().split()] for i in xrange(n)]

    cook(n, q, pasta)
