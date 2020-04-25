import os,sys
import copy

path = os.path.dirname(sys.argv[0])+"/"

class Graphe(object):
    """docstring for Graphe"""
    def __init__(self, filename):
        self.nom_fichier = filename
        self.graph_dictionnary_value = dict()
        self.nb_sommet = 0
        self.nb_arcs = 0
        self.contenu_fichier = []
        self.rangd = None
        self.rangm = 0

        
        """ le graphe est stocke dans : list_graphe = [[initial,terminale,valeur],[i,t,v],[i,t,v]] """
    
    def __str__(self):
        return "fichier Graphe de test : ",self.nom_fichier
    
    def menu(self):
        """ return rien, on donne juste une valeur a (type str) nom_fichier """
        pass

    def lecture_fichier(self):
        """ on uilise self.nom_fichier"""
        """ on return rien on donne juste une valeur a (type str) contenu_fichier"""
        maxlength = 0
        with open(path+self.nom_fichier, "r") as mon_fichier:
            self.contenu_fichier = (mon_fichier.read()).split("\n")


        

    def affiche_graphe(self):
        matrice1 = [["*" for i in range(self.nb_sommet)] for j in range(self.nb_sommet) ]
        matrice2 = [["F" for i in range(self.nb_sommet)] for j in range(self.nb_sommet) ]
        print("\n_________AFFICHAGE GRAPHE______________\n")
       # print("  ", end = '')
        #for num in range(self.nb_sommet): print(str(num), " ", end='') 
        
        #for num in range(self.nb_sommet): print(str(num), " ", end='') 

        
        for x in range(self.nb_sommet):
           

            for tup1, tup2 in self.graph_dictionnary_value[str(x)].items():
                matrice1[x][int(tup1)] = tup2
                matrice2[x][int(tup1)] = "V"
        
        print("    ", end = '')
        for i in range(self.nb_sommet):
            print(i, " " ,end= '')
        print("")
        for index, li in enumerate(matrice1):
            print(index,"  ", end= '')
            print("  ".join(li))
        
        print(" \n\n\n")
        print("    ", end = '')
        for i in range(self.nb_sommet):
            print(i, " " ,end= '')
        print("")
        for index, li in enumerate(matrice2):
            print(index,"  ", end= '')
            print("  ".join(li))
        
    def exist_circuitbis(self, graphbis):
        sortie = []
        for key, v in graphbis.items() :
            if(len(v) == 0):
                sortie.append(str(key))
        
        if(len(sortie) == 0 and len(graphbis) == 0):
            
            return False
        elif(len(sortie) == 0 and len(graphbis) != 0 ):
           
            return True
        else:
            print("\nSuppression des points de sorties:")
            for s in sortie:
                print(s)
                del graphbis[s]
            for key, v in graphbis.items():
                for item in sortie:
                    v.pop(item, None)
            print("Sommets restants :")
            for key in graphbis.keys():
                print(key, " ", end='')

            return Graphe.exist_circuitbis(self, graphbis)

    def exist_circuit(self):
        
        gb = copy.deepcopy(self.graph_dictionnary_value)

        #pour ne pas écraser le self.graph_dictionnary_value
        return Graphe.exist_circuitbis(self, gb)
        
    


    def rec_rangs(self, current_node): #current node est au moins égale à 1 vu que l'on a fais un tri au préalable
        list_pred = list();
        for k, val in self.graph_dictionnary_value.items():
            if(val.get(current_node, "None") != "None" and k != current_node):
                list_pred.append(Graphe.rec_rangs(self, k))

        if(len(list_pred) ==0):
            return 0
        else:
            return max(list_pred)+1

    def iscorrect(self):
        #on traite la sortie
        sortie_graphe = 0
        entre = [True for i in range(self.nb_sommet)]
        nbentree = 0
        index_entree = 0
        for k, v in self.graph_dictionnary_value.items():
            
            if(len(v) == 0):
                sortie_graphe += 1
        if(sortie_graphe != 1):
            print("Le graphe n'est pas correct car il y'a ", sortie_graphe, " point de sortie")
            return False

        for val in self.graph_dictionnary_value.values():
            for k in val.keys():
                entre[int(k)] = False
        for i in range(len(entre)):
            if(entre[i]):
                index_entree = i 
                nbentree+=1
        if(nbentree != 1):
            print("Le graphe n'est pas correct car il y'a ", nbentree, " point d'entrée")
            return False
        #Le graphe ne contient pas de circuit car on l'a vérifié precedement


        for value in self.graph_dictionnary_value[str(index_entree)].values():
            
            if(int(value) != 0):
                print("arcs incidents vers l’extérieur au point d’entrée de valeur non nulle")
                return False
        for node in self.contenu_fichier[2:]:
            n = node.split(" ")
            if(int(n[2]) < 0):
                print("Il existe un arc a valeur négatif")
                return False
        
        #On verifie la valeur des chaque arc :
       
        for v in self.graph_dictionnary_value.values():
            
            if(len(v) != 0 and len(v) != 1):
                tmp = ""
                for p in v.values():
                    if(tmp == ""):
                        tmp = p
                    else:
                        if(tmp != p):
                            print("2 arcs ont des poids différents")
                            return False
        


        return True

    def rang(self):
        print("--Rangs")
        rangs= [0 for i in range(self.nb_sommet)]
        
        for val in self.graph_dictionnary_value.values():
            for v in val.keys():
                rangs[int(v)] += 1
        for i in range(len(rangs)):
            if(rangs[i] != 0):
                rangs[i] = Graphe.rec_rangs(self, str(i))
        rangsmax = 0
        for i in range(len(rangs)):
            print(i, " rang :", rangs[i])
            if(rangs[i] > rangsmax):
                rangsmax = rangs[i]

        rangs_dict = {str(j):[] for j in range(rangsmax+1)}
        for i in range(len(rangs)):
            rangs_dict[str(rangs[i])].append([i, 0]) #tuple[1] correspondant a la date au plus tot du sommets
        

        self.rangd = rangs_dict
        self.rangm = rangsmax
        

        

    def pluslongcheminsommet(self, num_sommet, graphe_by_predecesseur):

        
        maxtab = []
        for i, v in graphe_by_predecesseur[str(num_sommet)].items():
            p = int(v) + Graphe.pluslongcheminsommet(self, int(i), graphe_by_predecesseur)
            maxtab.append(p)
        if(len(maxtab) ==0):
            return 0
        else:
            return max(maxtab)
    def pluscourtcheminsommet(self, num_sommet, graphe_by_predecesseur):

        
        mintab = []
        for i, v in graphe_by_predecesseur[str(num_sommet)].items():
            p = int(v) + Graphe.pluscourtcheminsommet(self, int(i), graphe_by_predecesseur)
            mintab.append(p)

        if(len(mintab) == 0):
            return 0
        else:
            return max(mintab)

    def CalendrierAuPlusTOT(self):
        
        dict_rang = copy.deepcopy(self.rangd)
        rangmax = self.rangm
        graphe_by_predecesseur ={str(j):dict() for j in range(self.nb_sommet)}
        for node in self.contenu_fichier[2:]:
            n = node.split(" ")
            graphe_by_predecesseur[str(n[1])][n[0]] = n[2]
        date_max_au_plus_tot = 0
        for i in range(0, rangmax+1):
            v = dict_rang[str(i)]
            print("rang ", i, ":")
            

            for tup in v:
                tup[1] = Graphe.pluslongcheminsommet(self, tup[0], graphe_by_predecesseur)
                print("\tsommet :", str(tup[0]), "date au plus tot", str(tup[1]))
            if( i == rangmax):
                date_max_au_plus_tot = int(v[0][1])
            print("\n")
        return date_max_au_plus_tot, dict_rang
    

    def CalendrierAuPlusTard(self, dateMaxAuPlusTot):
        dict_rang = copy.deepcopy(self.rangd)
        rangmax = self.rangm
       
        for i in range(rangmax, -1, -1):
            v = dict_rang[str(i)]
            print("rang ", i, ":")
            for tup in v:
                tup[1] = Graphe.pluscourtcheminsommet(self, tup[0], self.graph_dictionnary_value)
                tup[1] = dateMaxAuPlusTot- tup[1]
                print("\tsommet :", str(tup[0]), "date au plus tot", tup[1])
            print("\n")
        return dict_rang

    def marge(sef, calPlusTot, calPlusTard):
        print("MARGE CALENDRIER")
       
        for i in range(len(calPlusTot)):
            pTot = calPlusTot[str(i)]
            pTard = calPlusTard[str(i)]
            print("rang ", i, ":")

            for j in range(len(pTot)):
                print("\tSommet :", str(pTot[j][0]))
                mar = pTard[j][1] - pTot[j][1]
                print("\t \t marge : ", mar)

    def affiche_calendrier(self):
        print("CALENDRIER AU PLUS TOT")
        ret = Graphe.CalendrierAuPlusTOT(self)
        dmt = ret[0]
        graph_plus_tot = ret[1]
        
        print("CALENDRIER AU PLUS TARD")
        graph_plus_tard = Graphe.CalendrierAuPlusTard(self, dmt)
        Graphe.marge(self, graph_plus_tot, graph_plus_tard)


    def stockage_graphe(self):
        """ on uilise self.contenu_fichier"""
        """ return (type list) list_graphe"""
        """ On créer un dictionnaire avec pour key le noeud"""
        self.graph_dictionnary_value = {str(j):dict() for j in range(self.nb_sommet)}
        for node in self.contenu_fichier[2:]:
            n = node.split(" ")
            self.graph_dictionnary_value[str(n[0])][n[1]] = n[2]
            print(str(n[0]), " -> ", n[1], "=", n[2])

    def stockage_nb_sommet(self):
        """ on uilise self.lecture_ficher"""
        """ return rien, on donne une valeur a self.nb_sommet """
        self.nb_sommet = int(self.contenu_fichier[0])
        print(self.nb_sommet, " Sommets")
        
    def stockage_nb_arcs(self):
        """ on uilise self.lecture_ficher"""
        """ return rien, on donne une valeur a self.nb_arcs """
        self.nb_arcs = int(self.contenu_fichier[1])
        print(self.nb_arcs, " Arcs")
        
    def matrice_adjacence(self):
        """ return la liste representant la matrice d'adjacence """
        """ en paramettre nous utiliserons self.list_graphe"""
        pass

    def affichage_matrice(self):
        """ return rien, affiche le graphe donnez en parammetre sous forme d'une matrice """
        pass

