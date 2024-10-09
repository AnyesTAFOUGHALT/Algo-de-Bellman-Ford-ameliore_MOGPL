import utils as ut
import networkx as nx
import bellman_ford_algo as bf
import random
import matplotlib.pyplot as plt
import math

p = 0.5 # Probabilité de présence d'une arête 
n = 5
def generation_graphes_test(G,n):
    """Generation de N grapes avec des poids differents"""
    graphes = []
    for i in range(n):
        graphes.append(ut.ajout_poids_graphe(G))
    return graphes

def bellman_ford_liste (graphes,source):
    """on applique bellman ford sur la liste des graphe et on revoit l'union de ces plus courts chemins"""
    bfs = []
    for g in graphes:
        pcc , nb_iter = bf.bellman_ford(g , source)
        bfs.append(ut.generation_graphe_PCC( g ,pcc[nb_iter] ) )
    return bfs

def comparaison_avec_et_sans_pretraitement(iterations,n_min , n_max , p,nb_G):
    nb_iter_with_gloutonFas_ordre= []
    nb_iter_alea = []
    

    for n in range(n_min,n_max):
        iter_gloutonFas = 0
        iter_alea = 0
        print("Nombre de sommets : ", n)
        for i in range(iterations) :
            print("iteration",i)
            #génération d'un graph G
            G = None

            source = 0
            while(True):
                #G = ut.generation_graphe(n , p)
                G = ut.gen(n , p)
                exist_source = ut.source(G , source)
                if exist_source:
                    break

            G_avec_poids_diff = generation_graphes_test(G,nb_G)

            H = ut.ajout_poids_graphe(G)
            
            Gs_BFs =  bellman_ford_liste(G_avec_poids_diff,source)

            T = ut.union(Gs_BFs) 

            ordre_optimale = bf.GloutonFas(T)

            H_BF , nb_iter= bf.bellman_ford(H , source , ordre_optimale)
            iter_gloutonFas += nb_iter
            

            ordre_alea  = list(range(G.number_of_nodes()))
            random.shuffle(ordre_alea)

            H_BF_alea , nb_iter= bf.bellman_ford(H , source , ordre_alea)
            iter_alea += nb_iter
            
        nb_iter_with_gloutonFas_ordre.append(iter_gloutonFas/iterations)
        nb_iter_alea.append(iter_alea/iterations)

    nb_nodes = [i for i in range(n_min , n_max)]
    plt.plot(nb_nodes , nb_iter_with_gloutonFas_ordre, 'b', label="Nombre d'itération avec l'orde de GloutonFast")
    plt.plot(nb_nodes ,nb_iter_alea, 'r', label="Nombre d'itérations avec un ordre aléatoire")
    plt.ylabel('Nombre d\'itération')
    plt.legend()
    plt.suptitle("Analyse du nombre d'itération de l'algorithme Bellman Ford" )
    plt.tight_layout()
    plt.savefig("Analyse du nombre d'itération de l'algorithme Bellman Ford [" + str(n_min) + "," + str(n_max) + "].png")
    
    plt.show()

def comparaison_selon_nb_graphes(iterations,p,nb_G_min,nb_G_max):
    nb_sommets = [5]
    nb_iterations = [[] for i in range(len(nb_sommets))]
    plt.figure(figsize=(10, 6))

    for n in range(len(nb_sommets)) :
        print("n = ", nb_sommets[n])
        G = None
        source = 0
        while(True):
            G = ut.gen(nb_sommets[n] , p)
            exist_source = ut.source(G , source)
            if exist_source:
                break
        
        H = ut.ajout_poids_graphe(G)

        for g in range(nb_G_min , nb_G_max):
            nb_iter_g = 0
            for i in range(iterations) :
                print(n , g , i)
                G_avec_poids_diff = generation_graphes_test(G,g)

                
                Gs_BFs =  bellman_ford_liste(G_avec_poids_diff,source)

                T = ut.union(Gs_BFs) 

                ordre_optimale = bf.GloutonFas(T)

                H_BF , nb_iter= bf.bellman_ford(H , source , ordre_optimale)
                nb_iter_g += nb_iter
            nb_iterations[n].append(nb_iter_g/iterations)
        
        
        
    nb_g = [g for g in range(nb_G_min , nb_G_max)]
    plt.plot( nb_g, nb_iterations[0], 'b', label="Avec un graphe à 10 sommets")
    # plt.plot(nb_g , nb_iterations[1], 'r', label="Avec 10 sommets")
    # plt.plot(nb_g ,  nb_iterations[2], 'g', label="Avec 15 sommets")
    # plt.plot(nb_g , nb_iterations[3], 'yellow', label="Avec 20 sommets")
    plt.ylabel('Nombre d\'itération')
    plt.xlabel('Nombre de graphes utilisés dans la phase de prétraitement')
    plt.legend()
    plt.suptitle("Analyse de l\'impact du nombre de graphes employés pour apprendre l\'ordre sur le nombre d\'itérations" )
    plt.tight_layout()
    plt.savefig("Analyse de l\'impact du nombre de graphes utilisés pour apprendre l\'ordre sur le nombre d\'itérations[" + str(nb_G_min) + "," + str(nb_G_max) + "] .png")
    
    plt.show()


def main() :
    #-------------------Question 3---------------------------#

    #génération d'un graph G
    print("Question 3 :")
    G = nx.DiGraph()
    G.add_edge(0, 1 )
    G.add_edge(0, 3)
    G.add_edge(1, 2)
    G.add_edge(2, 3 )
    G.add_edge(2, 5)
    G.add_edge(3, 5 )
    G.add_edge(4, 3)
    G.add_edge(5, 4 )
    source = 0
    # while(True):
    #     G = ut.generation_graphe(n , p)
    #     exist_source = ut.source(G , source)
    #     if exist_source:
    #         break
    G1, G2, G3, H = generation_graphes_test(G,4)

    # #-------------------Question 4----------------------------#

    # Choix d'une racine qui atteint au moins |V|/2 sommets : 
    print("Question 4 :")

    print("La source designée est : ", source)

    G1_BF,G2_BF,G3_BF =  bellman_ford_liste([G1,G2,G3],source)
    #Union des plus courts chemins
    T = ut.union([ G1_BF,G2_BF,G3_BF ])

    # #-------------------Question 5----------------------------#
    print("Question 5 :")

    #On recupère l'odre optimal renvoyé par l'algo GloutonFas
    ordre_optimal = bf.GloutonFas(T)

    # Affichage des graphes :
    #G1
    #pos = ut.draw_graph(G1,"G1")
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
    print("Question 6 :")

    # On applique bellman Ford sur H avec l'odre optimal obtenu 
    H_BF , nb_iter= bf.bellman_ford(H , source , ordre_optimal)
    print("Le nombre d'itération avec l'ordre optimal : ", ordre_optimal," est : ", nb_iter)
    
    #-------------------Question 7----------------------------#

    print("Question 7 :")

    # On applique bellman Ford sur H avec un ordre aletoire obtenu 
    ordre_alea  = list(range(G.number_of_nodes()))
    random.shuffle(ordre_alea)  
    H_BF_alea , nb_iter= bf.bellman_ford(H , source , ordre_alea)
    print("Le nombre d'itération avec l'ordre aleatoire : ", ordre_alea," est : ", nb_iter)



    # # #------------------- Question 9 ---------------------------#
    # iterations = 20
    # print("Question 9 :")
    
    # comparaison_avec_et_sans_pretraitement(iterations,3 , 10 , 0.4,3)

    # #----------------- Question 10 ----------------------------#

    # #Ici on peut passer en parametres le nombre de graphe qu'on l'on souhaiterai utiliser 
    # print("Question 10 :")

    # comparaison_selon_nb_graphes(iterations,0.4,3,20)

    # #----------------- Question 11 ----------------------------#
    # print("Question 11 :")

    # nb_iter_alea = []
    # nb_iter_glouton_fast= []
    # plt.figure(figsize=(10, 6))
    # for i in range(20):
    #     print("iteration ",i)
    #     G = ut.generation_graphe_niveaux(4,2500,0.5)
    #     source = 0
    #     G1, G2, G3, H = generation_graphes_test(G,4)

    #     G1_BF,G2_BF,G3_BF =  bellman_ford_liste([G1,G2,G3],source)
    #     T = ut.union([ G1_BF,G2_BF,G3_BF ])

    #     ordre_optimal = bf.GloutonFas(T)


    #     H_BF , nb_iter= bf.bellman_ford(H , source , ordre_optimal)
    #     nb_iter_glouton_fast.append(nb_iter)

    #     ordre_alea  = list(range(G.number_of_nodes()))
    #     random.shuffle(ordre_alea)  
    #     H_BF_alea , nb_iter= bf.bellman_ford(H , source , ordre_alea)
    #     nb_iter_alea.append(nb_iter)

    # plt.plot( nb_iter_glouton_fast, 'b', label="Nombre d'itération avec l'orde de GloutonFast")
    # plt.plot(nb_iter_alea, 'r', label="Nombre d'itérations avec un ordre aléatoire")
    # plt.ylabel('Nombre d\'itération retournées par Bellman Ford')
    # plt.legend()
    # plt.suptitle("Analyse du nombre d'itération de l'algorithme Bellman Ford sur un graphe à 2500 niveaux" )
    # plt.tight_layout()
    # plt.savefig("Analyse du nombre d'itération de l'algorithme Bellman Ford sur un graphe à 2500 niveaux.png")
    
    # plt.show()

    

if __name__ == "__main__":
    main()
