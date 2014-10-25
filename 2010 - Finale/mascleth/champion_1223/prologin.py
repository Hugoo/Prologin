# -*- coding: iso-8859-1 -*-
# This file has been generated, if you wish to
# modify it in a permanent way, please refer
# to the script file : gen/generator_python.rb

from api import *
from math import *

try:
    import psyco
    psyco.full()
except:
    pass
    
# Fonction appellée au début de la partie.
def init_game():
	print "====DEBUT DU JEU====="

def distance(toon1,toon2):
	
	diffx = abs(toon1.x-toon2.x)
	diffy = abs(toon1.y-toon2.y)
	
	if(diffx==diffy):
		return diffx
	else:
		dist = sqrt((toon1.x-toon2.x)**2+(toon1.y-toon2.y)**2)
		dist = int(ceil(dist))-1
		return dist

def par_ou(attaquant,cible):

	print attaquant
	print cible

	if(attaquant.x<cible.x and attaquant.y<cible.y):
		print "L'attaquant se trouve en haut a gauche de la cible"
		if(afficher_erreur(deplacer(attaquant,position(x=cible.x,y=cible.y-1)))==CASE_OCCUPEE):
			afficher_erreur(deplacer(attaquant,position(x=cible.x-1,y=cible.y)))
		
		
	if(attaquant.x>cible.x and attaquant.y<cible.y):
		print "L'attaquant se trouve en haut a droite de la cible"
		if(afficher_erreur(deplacer(attaquant,position(x=cible.x,y=cible.y-1)))==CASE_OCCUPEE):
			afficher_erreur(deplacer(attaquant,position(x=cible.x+1,y=cible.y)))
		
	if(attaquant.x<cible.x and attaquant.y>cible.y):
		print "L'attaquant se trouve en bas a gauche de la cible"
		if(afficher_erreur(deplacer(attaquant,position(x=cible.x,y=cible.y-1)))==CASE_OCCUPEE):
			afficher_erreur(deplacer(attaquant,position(x=cible.x+1,y=cible.y)))
		
	if(attaquant.x>cible.x and attaquant.y>cible.y):
		print "L'attaquant se trouve en bas a droite de la cible"
		if(afficher_erreur(deplacer(attaquant,position(x=cible.x,y=cible.y-1)))==CASE_OCCUPEE):
			afficher_erreur(deplacer(attaquant,position(x=cible.x-1,y=cible.y)))
		
		
	if(attaquant.x==cible.x):
		if(attaquant.y<cible.y):
			print "attaquand meme ligne, a dgauche de ennemi"
		else:
			print "attaquant meme ligne, a droite de ennemi"
	if(attaquant.y==cible.y):
		if(attaquant.x<cible.x):
			print "attaquand meme colonne, au dessus de ennemi"
		else:
			print "attaquant meme colonne, en dessous de ennemi"
	return 0


# Fonction appellée pour la phase de retrait de KO.
def retirer_ko():
	ko_actuel = -2
	coord_choisies = ""
    #on va redonner de la vie aux unites qui en sont le plus KO
    #pour eviter qu'elles ne reviennent trop vite
    
   
    
	for u in unites():
		if u.ennemi==True: #on s interresse qu'aux ennemis
			print u
			print ko_actuel
			if u.ko>ko_actuel:
				ko_actuel=u.ko
				coord_choisies = u.pos
				
	if coord_choisies!="":
		return coord_choisies


# Fonction appellée pour la phase de jeu.
def jouer():
	
	
	print "================"
	print "="
	print "=    NEW TURN  ="
	print "="
	print "= TOUR ACTUEL ",tour_actuel()
	print "================"
	
	#premierement je determine quelle est ma position(haut ou bas de map?):
	sens = -1
	if(pos_renfort(False)==position(x=9,y=3)):
		print "POSITION: HAUT"
		sens = 1
	#ainsi, je peux dynamiquement faire avancer mes units en haut ou en bas en multipliant par sens
	
	coord_parot=""
	#AVANT TOUT, puis-je anneantir le P ennemi?
	#Etape 1, trouver les coord du parot ennemi
	for u in unites():
		if (u.ennemi==True and u.vrai_type_unite==PERROQUET): #si u == le parot ennemi
			coord_parot = u.pos
			
	coord_mparot=""
	for u in unites():
		if (u.ennemi==False and u.vrai_type_unite==PERROQUET): #si u == le parot ennemi
			coord_mparot = u.pos
	
	for u in unites():
		if (u.ennemi==False and u.vrai_type_unite==KANGOUROU):
			if(distance(coord_parot,u.pos)<=6):
				print "INVOQUE CARTE BANZAI"
				banzai(u.pos)
				break
	
	for u in unites():
		if (u.ennemi==False and u.vrai_type_unite==KANGOUROU):
			if(u.ko == 0):
				print "RELEVER KANGO"
				relever(u.pos)
				break
	#au debut de chaque tour, je verif si je peux exploser le kangoo:
	for u in unites():
		if (u.ennemi==False and u.vrai_type_unite==KANGOUROU):
			if(distance(u.pos,coord_parot)<=3):
				print "verif debut de tour"
				print "PA kangoo = ",u.pa
				afficher_erreur(attaquer(u.pos,u.pos))
	
	#je mets mes singes en defensive
	
	#prevoir les possibles mouvements ennemis
	for u in unites():
		if (u.ennemi==False and u.vrai_type_unite==SINGE):
			for u2 in unites():
				if (u2.ennemi==True):
					if(distance(u.pos,u2.pos)==4 or distance(u.pos,u2.pos)==5):
						print "MOOV UN SINGE POUR ATRTAQUER"
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x-sens,y=u.pos.y)))
						afficher_erreur(attaquer(u.pos,u2.pos))
						print ""
					else:
						attaquer(u.pos,u2.pos)
	
	#je regarde si on ennemi n'est pas trop pres de mon parot
	for u in unites():
		if (u.ennemi==True and u.ko==-1):
			
			portee1 = caracteristiques(u.vrai_type_unite).portee
			print ""
			print "ATTENTION ATTENTION"
			print "coord parot ",coord_parot
			print "unite ennemie de coord:",u.pos
			print "sa portee est:",portee1
			print "la distance est: ",distance(coord_mparot,u.pos)
			print ""
			if (distance(coord_mparot,u.pos)<=portee1+u.pa):
				print "Une unite peut me tuer au tour suivant!"
				print "ses coord: ",u.pos
				
				#On deplace le Parot
				#On deplace Chat et attaque
				#On deplace Singe et attaque
				#On attend
				
				#je suggere de determiner l'angle d'attaque.
				#demander a mon chat de le buter?
				for u3 in unites():
					if (u3.ennemi==False and u3.ko==-1 and u3.vrai_type_unite==CHAT):
						if (distance(u3.pos,u.pos)<=5):
							deplac = par_ou(u3.pos,u.pos)
							afficher_erreur(attaquer(u3.pos,u.pos))
					else:
					#on move le parot
						print ""
	
	
	#si par malheur mon kangoo est mort, je le restaure
	for u in unites():
		if(u.ennemi==False and u.vrai_type_unite==KANGOUROU and u.ko!=-1):
			print "mon kangou est KO, je le restore"
			potion(u.pos)
	
	
	
			
	
	if tour_actuel()==1:
		#1) bouger le parot
		deplacer(pos_renfort(False),position(x=pos_renfort(False).x+1,y=pos_renfort(False).y+(-1*sens)))
		#2) creer un kangou
		renfort(KANGOUROU)
	elif tour_actuel()==2:
		#1) bouger le kangou
		deplacer(pos_renfort(False),position(x=pos_renfort(False).x+(1*sens),y=pos_renfort(False).y+(3*sens)))
		#2) creer un singe
		renfort(SINGE)
	elif tour_actuel()==3:
		#1) bouger encore le kangou
		deguisement(position(x=pos_renfort(False).x+(1*sens),y=pos_renfort(False).y+(3*sens)),CHAT)
		deplacer(position(x=pos_renfort(False).x+(1*sens),y=pos_renfort(False).y+(3*sens)),position(x=pos_renfort(False).x+(2*sens),y=pos_renfort(False).y+(8*sens)))
		
		#2) bouger le singe
		deplacer(pos_renfort(False),position(x=pos_renfort(False).x+1,y=pos_renfort(False).y))
		
		#3)creer un chat
		renfort(CHAT)
	elif tour_actuel()==4:
		#1) bouger le chat
		deplacer(pos_renfort(False),position(x=pos_renfort(False).x+2,y=pos_renfort(False).y))
		#2) creer un autre singe
		renfort(SINGE)
	elif tour_actuel()==5:
		#1)bouger le singe
		deplacer(pos_renfort(False),position(x=pos_renfort(False).x,y=pos_renfort(False).y+(-1*sens)))
		renfort(CHAT)
	elif tour_actuel()==6:
		deplacer(pos_renfort(False),position(x=pos_renfort(False).x+2,y=pos_renfort(False).y+(5*sens)))
		renfort(SINGE)
	
	
	
	coord_parot=""
	for u in unites():
		if (u.ennemi==True and u.vrai_type_unite==PERROQUET): #si u == le parot ennemi
			coord_parot = u.pos
			
	#a partir de l'etape 3, les mouv deviennent un peu plus aleatoires
	if tour_actuel()>3:
		for u in unites():
			if (u.ennemi==False and u.ko==-1 and u.vrai_type_unite==KANGOUROU):
				print "je replace mon kangou"
				#dans quelle direction se rapprocher?
				if(u.pos.x==coord_parot.x+1 or u.pos.x==coord_parot.x-1): #si pas loin
					if(distance(coord_parot,u.pos)<=6 and distance(coord_parot,u.pos)>=4):
						print "une colonne decart, tente lapproche + bombe"
						print u
						if(coord_parot.y>u.pos.y):
							var = 3
						else:
							var = -3
						if(deplacer(u.pos,position(x=u.pos.x,y=u.pos.y+var))==OK):
							print "attaque?",afficher_erreur(attaquer(u.pos,u.pos))
				elif(u.pos.y==coord_parot.y+1 or u.pos.y==coord_parot.y-1): #si pas loin
					if(distance(coord_parot,u.pos)<=6):
						print "une ligne decart, tente lapproche + bombe"
						print u
						if(coord_parot.x>u.pos.x):
							var = 3
						else:
							var = -3
						if(deplacer(u.pos,position(x=u.pos.x+var,y=u.pos.y))==OK):
							print "attaque?",afficher_erreur(attaquer(u.pos,u.pos))
				
				
				if(u.pos.x>coord_parot.x): #si je suis plus vers la droite
					print "plus vers la droite"
					if(u.pos.y==coord_parot.y): #si je suis sur la meme colonne
						if(deplacer(u.pos,position(x=u.pos.x-3,y=u.pos.y))==CASE_OCCUPEE):
							afficher_erreur(deplacer(u.pos,position(x=u.pos.x-2,y=u.pos.y)))
					elif(u.pos.y<coord_parot.y):
						if(deplacer(u.pos,position(x=u.pos.x-3,y=u.pos.y+3))==CASE_OCCUPEE):
							afficher_erreur(deplacer(u.pos,position(x=u.pos.x-2,y=u.pos.y+2)))
					elif(u.pos.y>coord_parot.y):
						if(deplacer(u.pos,position(x=u.pos.x-3,y=u.pos.y-3))==CASE_OCCUPEE):
							afficher_erreur(deplacer(u.pos,position(x=u.pos.x-2,y=u.pos.y+2)))
				elif(u.pos.x<coord_parot.x): #si je suis plus vers la gauche
					print "plus vers la gauche"
					if(u.pos.y==coord_parot.y): #si je suis sur la meme colonne
						if(deplacer(u.pos,position(x=u.pos.x+3,y=u.pos.y))==CASE_OCCUPEE):
							afficher_erreur(deplacer(u.pos,position(x=u.pos.x+2,y=u.pos.y)))
					elif(u.pos.y<coord_parot.y):
						if(deplacer(u.pos,position(x=u.pos.x+3,y=u.pos.y+3))==CASE_OCCUPEE):
							afficher_erreur(deplacer(u.pos,position(x=u.pos.x+2,y=u.pos.y+2)))
					elif(u.pos.y>coord_parot.y):
						if(deplacer(u.pos,position(x=u.pos.x+3,y=u.pos.y-3))==CASE_OCCUPEE):
							afficher_erreur(deplacer(u.pos,position(x=u.pos.x+2,y=u.pos.y+2)))
				elif(u.pos.x==coord_parot.x): 
					if(u.pos.y<coord_parot.y):
						if(deplacer(u.pos,position(x=u.pos.x,y=u.pos.y+3))==CASE_OCCUPEE):
							afficher_erreur(deplacer(u.pos,position(x=u.pos.x,y=u.pos.y+2)))
					elif(u.pos.y>coord_parot.y):
						if(deplacer(u.pos,position(x=u.pos.x,y=u.pos.y-2))==CASE_OCCUPEE):
							afficher_erreur(deplacer(u.pos,position(x=u.pos.x,y=u.pos.y-1)))
				elif(u.pos.y==coord_parot.y): 
					if(u.pos.x<coord_parot.x):
						if(deplacer(u.pos,position(x=u.pos.x+3,y=u.pos.y))==CASE_OCCUPEE):
							afficher_erreur(deplacer(u.pos,position(x=u.pos.x+2,y=u.pos.y)))
					elif(u.pos.x>coord_parot.x):
						if(deplacer(u.pos,position(x=u.pos.x-3,y=u.pos.y))==CASE_OCCUPEE):
							afficher_erreur(deplacer(u.pos,position(x=u.pos.x-2,y=u.pos.y)))
				if(distance(u.pos,coord_parot)<=3):
					print "le kangoo se trouve a 3 ou moins du parot"
					print "PA kangoo = ",u.pa
					afficher_erreur(attaquer(u.pos,u.pos))
				break
	
	
	
	coord_chat = position(x=0,y=0)
	for u in unites():
		if (u.ennemi==False and u.vrai_type_unite==KANGOUROU):
			coord_chat = u.pos
	
	afficher_erreur(attaquer(coord_chat,coord_parot))
	if tour_actuel()>=2:
		for u in unites():
			if (u.ennemi==False and u.ko==-1 and u.vrai_type_unite==CHAT):
				print "je replace mon kangou"
				#dans quelle direction se rapprocher?
				if(u.pos.x>coord_parot.x): #si je suis plus vers la droite
					if(u.pos.y==coord_parot.y): #si je suis sur la meme colonne
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x-2,y=u.pos.y)))
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x-1,y=u.pos.y)))
					elif(u.pos.y<coord_parot.y):
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x-2,y=u.pos.y+2)))
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x-1,y=u.pos.y+1)))
					elif(u.pos.y>coord_parot.y):
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x-2,y=u.pos.y-2)))
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x-1,y=u.pos.y+1)))
				elif(u.pos.x<coord_parot.x): #si je suis plus vers la droite
					if(u.pos.y==coord_parot.y): #si je suis sur la meme colonne
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x+2,y=u.pos.y)))
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x+1,y=u.pos.y)))
					elif(u.pos.y<coord_parot.y):
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x+2,y=u.pos.y+2)))
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x+1,y=u.pos.y+1)))
					elif(u.pos.y>coord_parot.y):
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x+2,y=u.pos.y-2)))
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x+1,y=u.pos.y+1)))
				elif(u.pos.x==coord_parot.x): 
					if(u.pos.y<coord_parot.y):
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x,y=u.pos.y+2)))
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x,y=u.pos.y+1)))
					elif(u.pos.y>coord_parot.y):
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x,y=u.pos.y-2)))
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x,y=u.pos.y-1)))
				elif(u.pos.y==coord_parot.y): 
					if(u.pos.x<coord_parot.x):
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x+2,y=u.pos.y)))
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x+1,y=u.pos.y)))
					elif(u.pos.x>coord_parot.x):
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x-2,y=u.pos.y)))
						afficher_erreur(deplacer(u.pos,position(x=u.pos.x-1,y=u.pos.y)))
				afficher_erreur(attaquer(coord_chat,coord_parot))
				break
		
		renfort(SINGE)
		print "apres tout cela, il me reste: ",nombre_pc()
		
	
	
	if ((tour_actuel()+1)%5==0):
		for u in unites():
			if (u.ennemi==False and u.vrai_type_unite==PERROQUET):
				print "parrot au bord"
				if u.pos.x == taille_terrain_actuelle().min_coord: #si jai ",u.type_unite_actuel," sur le bord gauche
					print "jai ",u.type_unite_actuel," sur le bord gauche, la deplace vers la droite"
					
				elif u.pos.x == taille_terrain_actuelle().max_coord: #si jai ",u.type_unite_actuel," sur le bord droit
					print "jai ",u.type_unite_actuel," sur le bord droit, la deplace vers la gauche"
					
				elif u.pos.y == taille_terrain_actuelle().min_coord: #si jai ",u.type_unite_actuel," en haut
					print "jai ",u.type_unite_actuel," en haut, la deplace vers le bas"
					deplacer(u.pos,position(x=u.pos.x,y=u.pos.y+1))
					
				elif u.pos.y == taille_terrain_actuelle().max_coord: #si jai ",u.type_unite_actuel," en bas
					print "jai ",u.type_unite_actuel," en bas, la deplace vers le haut"
					deplacer(u.pos,position(x=u.pos.x,y=u.pos.y-1))
	
	#jexecute deux fois la meme dfonction, la permiere concerne le Parot, il est prioritaire
	
	if ((tour_actuel()+1)%5==0):
		for u in unites():
			if u.ennemi==False:
				if u.pos.x == taille_terrain_actuelle().min_coord: #si jai ",u.type_unite_actuel," sur le bord gauche
					if u.pos.y == taille_terrain_actuelle().min_coord: #si en plus detre a gauche, elle est en haut:
						print "une unite est dans le coin HAUT-GAUCHE"
						deplacer(u.pos,position(x=u.pos.x+1,y=u.pos.y+1))
						
					elif u.pos.y == taille_terrain_actuelle().max_coord: #si en plus detre a gauche, elle est en bas:
						print "une unite est dans le coin BAS-GAUCHE"
						deplacer(u.pos,position(x=u.pos.x+1,y=u.pos.y-1))
					
					else:
						print "jai ",u.type_unite_actuel," sur le bord gauche, la deplace vers la droite"
					
				elif u.pos.x == taille_terrain_actuelle().max_coord: #si jai ",u.type_unite_actuel," sur le bord droit
					if u.pos.y == taille_terrain_actuelle().min_coord: #si en plus detre a gauche, elle est en haut:
						print "une unite est dans le coin HAUT-DROITE"
						deplacer(u.pos,position(x=u.pos.x-1,y=u.pos.y+1))
						
					elif u.pos.y == taille_terrain_actuelle().max_coord: #si en plus detre a gauche, elle est en bas:
						print "une unite est dans le coin BAS-DROITE"
						deplacer(u.pos,position(x=u.pos.x-1,y=u.pos.y-1))
					
					else:
						print "jai ",u.type_unite_actuel," sur le bord droit, la deplace vers la gauche"
					
				elif u.pos.y == taille_terrain_actuelle().min_coord: #si jai ",u.type_unite_actuel," en haut
					print "jai ",u.type_unite_actuel," en haut, la deplace vers le bas"
					if(deplacer(u.pos,position(x=u.pos.x+1,y=u.pos.y+1))==CASE_OCCUPEE):
						deplacer(position(x=u.pos.x+1,y=u.pos.y+1),position(x=u.pos.x+2,y=u.pos.y+2))
						deplacer(u.pos,position(x=u.pos.x+1,y=u.pos.y+1))
					
				elif u.pos.y == taille_terrain_actuelle().max_coord: #si jai ",u.type_unite_actuel," en bas
					print "jai ",u.type_unite_actuel," en bas, la deplace vers le haut"
					if(deplacer(u.pos,position(x=u.pos.x-1,y=u.pos.y-1))==CASE_OCCUPEE):
						deplacer(position(x=u.pos.x-1,y=u.pos.y-1),position(x=u.pos.x-2,y=u.pos.y-2))
						deplacer(u.pos,position(x=u.pos.x-1,y=u.pos.y-1))
	
	
	#### FIN MOUVEMENT MAP





	

def pmon_parot():
	for u in unites():
		if (u.ennemi==True and u.vrai_type_unite==PERROQUET): #si u == le parot ennemi
			coord_parot = u.pos
			print "Parot ennemi trouve, coord = ", coord_parot
			return coord_parot

def mon_parot():
	for u in unites():
		if (u.ennemi==False and u.vrai_type_unite==PERROQUET): #si u == le parot ennemi
			coord_parot = u.pos
			print "Parot a moi trouve, coord = ", coord_parot
			return coord_parot



# Fonction appellée à la fin de la partie.
def end_game():
    pass # Place ton code ici

