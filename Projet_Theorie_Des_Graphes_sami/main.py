# -*- coding: utf-8 -*-
from graphe import *


def main():
	graph_file = ['L3-F3-graphe1.txt',"L3-F3-graphe2.txt", "L3-F3-graphe3.txt", "L3-F3-graphe4.txt","L3-F3-graphe5.txt", "L3-F3-graphe6.txt", "L3-F3-graphe7.txt","L3-F3-graphe8.txt", "L3-F3-graphe9.txt", "L3-F3-graphe10.txt", "L3-F3-graphe11.txt","L3-F3-graphe12.txt","L3-F3-graphe13.txt"]
	number = 0
	while True:

		while  True:
			
			print("Veuillez choisir le graphe a traiter: \n")
			for i, g in enumerate(graph_file):
				print(i, ": ", g)
			try:

				number = int(input("\nQuel fichier souhaitez vous utiliser ? :"))
				if(number<0 or number>=len(graph_file)):
					print("Merci de rentrer un nombre compris entre 0 et " , len(graph_file)-1)
				else:
					break;
			except:
				print("Merci de rentre un nombre")


		a = Graphe(graph_file[number])
		a.lecture_fichier()


		a.stockage_nb_sommet()
		a.stockage_nb_arcs()
		a.stockage_graphe()
		a.affiche_graphe()
		#getcircuit = a.exist_circuit()
		#if(!getcircuit):
		
		if(a.exist_circuit()):
			print("Il existe un circuit dans le graphe ", graph_file[number])
		else:
			print("Il n'y a pas de circuit dans le graphe ", graph_file[number])
			print("Verification que le graphe est d'ordonnancement correct :")
			isc = a.iscorrect()
			if(isc):
				print("Le graphe est d'ordonnancement correct")
			else:
				print("Le graphe n'est pas d'ordonnancement correct")
		print("\n\n")
		
if __name__ == '__main__':
	main()


