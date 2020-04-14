class Graphe(object):
	"""docstring for Graphe"""
	def __init__(self, nb_sommet, nb_arcs, list_graphe, nom_fichier, contenu_fichier, ist_graphe_adj):
		super(Graphe, self).__init__()
		self.nom_fichier = nom_fichier
		self.contenu_fichier = contenu_fichier
		self.nb_sommet = nb_sommet
		self.nb_arcs = nb_arcs
		self.list_graphe = list_graphe
		self.list_graphe_adj = list_graphe_adj
		""" le graphe est stocke dans : list_graphe = [[initial,terminale,valeur],[i,t,v],[i,t,v]] """
	
	def __str__(self):
		return "fichier Graphe de test : ",self.nom_fichier

	def menu(self):
		""" return rien, on donne juste une valeur a (type str) nom_fichier """
		pass

	def lecture_fichier(self):
		""" on uilise self.nom_fichier"""
		""" on return rien on donne juste une valeur a (type str) contenu_fichier"""
		pass

	def stockage_graphe(self):
		""" on uilise self.contenu_fichier"""
		""" return (type list) list_graphe"""
		pass

	def stockage_nb_sommet(self):
		""" on uilise self.lecture_ficher"""
		""" return rien, on donne une valeur a self.nb_sommet """
		pass

	def stockage_nb_arcs(self):
		""" on uilise self.lecture_ficher"""
		""" return rien, on donne une valeur a self.nb_arcs """
		pass

	def matrice_adjacence(self):
		""" return la liste representant la matrice d'adjacence """
		""" en paramettre nous utiliserons self.list_graphe"""
		pass

	def affichage_matrice(self):
		""" return rien, affiche le graphe donnez en parammetre sous forme d'une matrice """
		pass

