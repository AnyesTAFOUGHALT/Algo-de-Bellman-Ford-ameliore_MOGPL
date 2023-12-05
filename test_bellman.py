import utils as ut
import networkx as nx
import bellman_ford_algo as bf
import random
import matplotlib.pyplot as plt
"""
G = nx.DiGraph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(4, 7)
G.add_edge(5, 7)
G.add_edge(6, 5)
G.add_edge(6, 8)
G.add_edge(7, 1)
G.add_edge(8, 3)
G.add_edge(8, 2)

ut.draw_graph(G)
print(bf.GloutonFas(G))

"""

# G = nx.DiGraph()
# G.add_edge(1, 2 , weight=2)
# G.add_edge(1, 3 , weight=1)
# G.add_edge(3, 2 , weight=1)
# G.add_edge(2, 4 , weight=1)
# G.add_edge(3, 4 , weight=3)
# G.add_edge(1, 4 , weight=5)
# ut.draw_graph(G)
# new_G , iter = bf.bellman_ford(G,1)
# print(iter)
# ut.draw_graph(new_G)


#ut.draw_graph(ut.genrartion_de_graphes(G))
N = 5 # Nombre de noeuds
p = 0.4 # Probabilité de présence d'une arête 

def generation_graphes_test(G,n):
    """Generation de N grapes avec des poids differents"""
    graphes = []
    for i in range(n):
        graphes.append(ut.genrartion_de_graphes(G))
    return graphes

def bellman_ford_liste (graphes,source):
    """on applique bellman ford sur la liste des graphe et on revoit l'union de ces plus courts chemins"""
    bfs = []
    for g in graphes:
        bfs.append(bf.bellman_ford(g , source)[0] )
    return bfs


def comparaison_avec_et_sans_pretraitement(iterations,n,p,nb_G):
    nb_iter_with_gloutonFas_ordre= []
    nb_iter_alea = []

    for i in range(iterations) :
        print("iteration",i)
        #génération d'un graph G
        G = None

        source = None
        while(True):
            G = nx.erdos_renyi_graph(n, p, directed=True)
            source = ut.source(G)
            if source != None :
                break

        G_avec_poids_diff = generation_graphes_test(G,nb_G)

        H = ut.genrartion_de_graphes(G)
        
        Gs_BFs =  bellman_ford_liste(G_avec_poids_diff,source)

        T = ut.union(Gs_BFs) 

        ordre_optimale = bf.GloutonFas(T)

        H_BF , nb_iter= bf.bellman_ford(H , source , ordre_optimale)
        print("Le nombre d'itération avec l'ordre optimale : ", ordre_optimale," est : ", nb_iter)
        nb_iter_with_gloutonFas_ordre.append(nb_iter)

        ordre_alea  = list(range(G.number_of_nodes()))
        random.shuffle(ordre_alea)

        H_BF_alea , nb_iter= bf.bellman_ford(H , source , ordre_alea)
        print("Le nombre d'itération avec l'ordre aleatoire : ", ordre_alea," est : ", nb_iter)
        nb_iter_alea.append(nb_iter)

    plt.plot( nb_iter_with_gloutonFas_ordre, 'b', label="Nombre d'itération avec l'orde de GloutonFast")
    plt.plot(nb_iter_alea, 'r', label="Nombre d'itérations avec un ordre aléatoire")
    plt.ylabel('Nombre d\'itération')
    plt.legend()
    plt.suptitle("Analyse du nombre d'itération de l'algorithme Bellman Ford" )
    plt.tight_layout()
    plt.savefig("Analyse du nombre d'itération de l'algorithme Bellman Ford.png")
    
    plt.show()


def comparaison_selon_nb_graphes(iterations,n,p,nb_G1,nb_G2):
    nb_iter_with_gloutonFas_ordre_1= []
    nb_iter_with_gloutonFas_ordre_2 = []

    for i in range(iterations) :
        print("iteration",i)
        #génération d'un graph G
        G = None

        source = None
        while(True):
            G = nx.erdos_renyi_graph(n, p, directed=True)
            source = ut.source(G)
            if source != None :
                break

        G_avec_poids_diff_1 = generation_graphes_test(G,nb_G1)
        G_avec_poids_diff_2 = generation_graphes_test(G,nb_G2)

        H = ut.genrartion_de_graphes(G)
        
        Gs_BFs_1 =  bellman_ford_liste(G_avec_poids_diff_1,source)
        Gs_BFs_2 =  bellman_ford_liste(G_avec_poids_diff_2,source)

        T1 = ut.union(Gs_BFs_1) 
        T2 = ut.union(Gs_BFs_2) 

        ordre_optimale_1 = bf.GloutonFas(T1)
        ordre_optimale_2 = bf.GloutonFas(T2)

        H_BF , nb_iter= bf.bellman_ford(H , source , ordre_optimale_1)
        print("Le nombre d'itération avec l'ordre optimale : ", ordre_optimale_1," est : ", nb_iter)
        nb_iter_with_gloutonFas_ordre_1.append(nb_iter)

        H_BF_alea , nb_iter= bf.bellman_ford(H , source , ordre_optimale_2)
        print("Le nombre d'itération avec l'ordre aleatoire : ", ordre_optimale_2," est : ", nb_iter)
        nb_iter_with_gloutonFas_ordre_2.append(nb_iter)

    plt.plot( nb_iter_with_gloutonFas_ordre_1, 'b', label="Nombre d'itération avec l'orde de GloutonFast 1")
    plt.plot(nb_iter_with_gloutonFas_ordre_2, 'r', label="Nombre d'itération avec l'orde de GloutonFast 2")
    plt.ylabel('Nombre d\'itération')
    plt.legend()
    plt.suptitle("Analyse du nombre d'itération de l'algorithme Bellman Ford" )
    plt.tight_layout()
    plt.savefig("Analyse du nombre d'itération de l'algorithme Bellman Ford.png")
    
    plt.show()


def main() :
    #-------------------Question 3---------------------------#

    # #génération d'un graph G
    # G = nx.erdos_renyi_graph(N, p, directed=True)
    # G1, G2, G3, H = generation_graphes_test(G,4)

    # #-------------------Question 4----------------------------#

    # # Choix d'une racine qui atteint au moins |V|/2 sommets : 
    # source =  ut.source(G)
    # print("La source designée est : ", source)

    # G1_BF,G2_BF,G3_BF =  bellman_ford_liste([G1,G2,G3],source)
    # #Union des plus courts chemins
    # T = ut.union([ G1_BF,G1_BF,G1_BF ])

    # #-------------------Question 5----------------------------#

    # #On recupère l'odre optimal renvoyé par l'algo GloutonFas
    # ordre_optimal = bf.GloutonFas(T)

    # # Affichage des graphes :
    # #G1
    # pos = ut.draw_graph(G1,"G1")
    # ut.draw_graph(G1_BF,"G1_BF" , pos)
    # #G2
    # ut.draw_graph(G2,"G2", pos)       
    # ut.draw_graph(G2_BF,"G2_BF" , pos)
    # #G3
    # ut.draw_graph(G3,"G3", pos)
    # ut.draw_graph(G3_BF,"G3_BF" , pos)
    # #T
    # ut.draw_graph(T,"T",pos)

    # #-------------------Question 6----------------------------#

    # # On applique bellman Ford sur H avec l'odre optimal obtenu 
    # H_BF , nb_iter= bf.bellman_ford(H , source , ordre_optimal)
    # print("Le nombre d'itération avec l'ordre optimal : ", ordre_optimal," est : ", nb_iter)
    
    # #Affichage : 
    # ut.draw_graph(H_BF,"H_BF" , pos)
    # #-------------------Question 7----------------------------#

    # # On applique bellman Ford sur H avec un ordre aletoire obtenu 
    # ordre_alea  = list(range(G.number_of_nodes()))
    # random.shuffle(ordre_alea)  
    # H_BF_alea , nb_iter= bf.bellman_ford(H , source , ordre_alea)
    # print("Le nombre d'itération avec l'ordre aleatoire : ", ordre_alea," est : ", nb_iter)
    
    # #Affichage :
    # ut.draw_graph(H_BF_alea,"H_BF" , pos)



    # #------------------- Question 9 ---------------------------#
    # iterations = 100
    # comparaison_avec_et_sans_pretraitement(iterations,N,p,3)


    #----------------- Question 10 ----------------------------#

    #Ici on peut passer en parametres le nombre de graphe qu'on l'on souhaiterai utiliser 
    comparaison_selon_nb_graphes(100,N,p,3,5)

if __name__ == "__main__":
    main()
