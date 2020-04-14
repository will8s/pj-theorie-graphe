import os,sys

path = os.path.dirname(sys.argv[0])+"/graphe-de-test/"

class Graphe(object):
	"""docstring for Graphe"""
	def __init__(self):
		super(Graphe, self).__init__()
		self.nom_fichier = ""
		self.contenu_fichier = []
		self.nb_sommet = ""
		self.nb_arcs = ""
		self.list_graphe = [[]]
		self.list_graphe_adj = [[]]
		""" le graphe est stocke dans : list_graphe = [[initial,terminale,valeur],[i,t,v],[i,t,v]] """
	
	def __str__(self):
		return "fichier Graphe de test : ",self.nom_fichier

	def menu(self):
		""" return rien, on donne juste une valeur a (type str) nom_fichier """
		pass

	def lecture_fichier(self):
		""" on uilise self.nom_fichier"""
		""" on return rien on donne juste une valeur a (type str) contenu_fichier"""
		with open(path+"L3-F3-graphe9.txt", "r") as mon_fichier:
			self.contenu_fichier = (mon_fichier.read()).split("\n")
		print self.contenu_fichier

	def stockage_graphe(self):
		""" on uilise self.contenu_fichier"""
		""" return (type list) list_graphe"""
		for x in self.contenu_fichier[2:]:
			self.list_graphe.append(x.split(" "))
		self.list_graphe = self.list_graphe[1:]
		print self.list_graphe

	def stockage_nb_sommet(self):
		""" on uilise self.lecture_ficher"""
		""" return rien, on donne une valeur a self.nb_sommet """
		self.nb_sommet = self.contenu_fichier[0]
		print self.nb_sommet
		
	def stockage_nb_arcs(self):
		""" on uilise self.lecture_ficher"""
		""" return rien, on donne une valeur a self.nb_arcs """
		self.nb_arcs = self.contenu_fichier[1]
		print self.nb_arcs
		
	def matrice_adjacence(self):
		""" return la liste representant la matrice d'adjacence """
		""" en paramettre nous utiliserons self.list_graphe"""
		pass

	def affichage_matrice(self):
		""" return rien, affiche le graphe donnez en parammetre sous forme d'une matrice """
		pass

