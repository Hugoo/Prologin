# -*- coding: utf-8 -*-
import sys
from math import *


def tower_defense(rows, cols, theMap):

    
    coordTours = []
    i = int(0)
    i2 = int(0)
    for i in range(0,len(theMap)):
        for i2 in range(0,len(theMap[i])):
                try:
                    int(theMap[i][i2]) #si cest un nombre, int
                    coordTours.append([i,i2,theMap[i][i2]])
                except ValueError:
                    i=i
    ##-METTRE DANS UN TABLEAU, LES COORD DES ENNEMIS
    coordEnnemis = []
    i = int(0)
    i2 = int(0)
    for i in range(0,len(theMap)):
        for i2 in range(0,len(theMap[i])):
                if(theMap[i][i2]=="E"): #si cest un nombre, int
                    coordEnnemis.append([i,i2])
    porteeTours = []
    i = 0
    i2 = 0
    touche = 0
    for i in range(0,len(coordTours)):
        i2 = 0
        while i2<len(coordEnnemis):
            xen = coordEnnemis[i2][0]
            yen = coordEnnemis[i2][1]
            xtour = coordTours[i][0]
            ytour = coordTours[i][1]
            distance = int(round(sqrt((xen-xtour)*(xen-xtour)+(yen-ytour)*(yen-ytour))))
            if distance<=int(coordTours[i][2]):
                coordEnnemis.pop(i2)
            else:
                i2 = i2 + 1

    if len(coordEnnemis)==0:
        return False
    else:
        return True


if __name__ == '__main__':

    rows = int(raw_input())
    cols = int(raw_input())
    theMap = [list(raw_input()) for i in xrange(rows)]
   
    rows = rows - 1
    cols = cols - 1
    if tower_defense(rows, cols, theMap):
        print "1"
    else:
        print "0"
