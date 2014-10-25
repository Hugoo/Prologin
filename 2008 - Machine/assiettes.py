#!/usr/bin/python
# -*- coding: utf-8 -*-

recup = raw_input();
valeurs2 = recup.split(' ',2)
n = int(valeurs2[0])
m = int(valeurs2[1])
p = int(valeurs2[2])

def equilibre_assiettes(n, m, p):
    un = n+m
    deux = n+p
    trois = m+p

    if(un == p): return 1
    if(deux == m): return 1
    if(trois == n): return 1
    return 0
print equilibre_assiettes(n, m, p)
