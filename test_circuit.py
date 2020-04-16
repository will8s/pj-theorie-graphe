def test_circuit(self):
	#on utilise la matrice de d'adjacence pour savoir si il y a un circuit
	#definition circuit :
	#un circuit n'a pas de point d'entré : pas de noeuds qui sont seulement des etats initiaux
	#un circuit n'a pas de point d'sorti : pas de noeuds qui sont seulement des états finaux

http://www.momirandum.com/graphes/algorithmes-generaux/CircuitRosalindMarimond.html
https://www.myefrei.fr/moodle/pluginfile.php/139023/mod_resource/content/2/TG-Exercices%202019-20%20solutions.pdf

#la page 11 t'explique comment detecter un circuit par suppression de point d'entrée/initial

"""
determiner les entrées du graphe et les sorties

determiner les element precedent et suivant d'un element(stocké)


if on regarde si chaque element est un etat inital et un etat terminal d'un arc si oui :
	un circuit
else
	 on supprime de self.list_graphe_adja les elements qui sont seulement initiaux (ayant la valeur 1 et 0)
	 on supprime de self.list_graphe_adja les elements qui sont seulement terminaux (ayant la valeur 1 et 0)
"""


pour résumer si l'élément (de valeur 1) dans la matrice d'adjacence n'a pas d'élément avant lui tu le supprimes 
et il n'a pas d'élément apres lui tu le supprime

donc si il y reste aucun element c'est pas un circuit sinon si il reste des elements qui forme une boucle c'est un circuit