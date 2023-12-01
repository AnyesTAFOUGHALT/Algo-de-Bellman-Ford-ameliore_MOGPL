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
N = 7
p = 0.4

def main() :
    #-------------------Question 3 & 4 ----------------------------
    #génération d'un graph G
    # G = nx.erdos_renyi_graph(N, p, directed=True)

    # G1 = ut.genrartion_de_graphes(G)
    # print("ff")
    # G2 = ut.genrartion_de_graphes(G)
    # print("ff")

    # G3 = ut.genrartion_de_graphes(G)
    # print("ff")
    
    # H = ut.genrartion_de_graphes(G)
    # print("ff")
    
    # source =  ut.source(G)
    # print("ff")

    # #------------------- Question 4 ----------------------------
    # G1_BF = bf.bellman_ford(G1 , source)[0]  
    # print("ff")

    # G2_BF = bf.bellman_ford(G2 , source)[0] 
    # print("ff")

    # G3_BF = bf.bellman_ford(G3 , source)[0]  

    # print("source", source)

    # pos = ut.draw_graph(G1,"G1")

    # ut.draw_graph(G1_BF,"G1_BF" , pos)
    # ut.draw_graph(G2,"G2", pos)       
    # ut.draw_graph(G2_BF,"G2_BF" , pos)
    # ut.draw_graph(G3,"G3", pos)
    # ut.draw_graph(G3_BF,"G3_BF" , pos)

    # T = ut.union(G1_BF , G2_BF , G3_BF) 

    # ut.draw_graph(T,"T",pos)

    # #----------------- Question 5 -------------------------------
    # ordre = bf.GloutonFas(T)

    # #----------------- Question 6 -------------------------------
    # H_BF , nb_iter= bf.bellman_ford(H , source , ordre)
    # print("Le nombre d'itération avec l'ordre ", ordre," est : ", nb_iter)
    # ut.draw_graph(H_BF,"H_BF" , pos)

    # #----------------- Question 7 -------------------------------
    # ordre_alea  = list(range(G.number_of_nodes()))
    # random.shuffle(ordre_alea)

    # H_BF_alea , nb_iter= bf.bellman_ford(H , source , ordre_alea)
    # print("Le nombre d'itération avec l'ordre ", ordre_alea," est : ", nb_iter)
    # ut.draw_graph(H_BF_alea,"H_BF" , pos)


    #----------------- Question 9 -------------------------------
    iterations = 15
    nb_iter_with_gloutonFas_ordre= []
    nb_iter_alea = []
    for i in range(iterations) :
        print("iteration",i)
        #génération d'un graph G
        G = nx.erdos_renyi_graph(N, p, directed=True)

        G1 = ut.genrartion_de_graphes(G)
        
        G2 = ut.genrartion_de_graphes(G)
        

        G3 = ut.genrartion_de_graphes(G)
        

        H = ut.genrartion_de_graphes(G)
        

        source =  ut.source(G)
        

        #------------------- Question 4 ----------------------------
        G1_BF = bf.bellman_ford(G1 , source)[0]  
        

        G2_BF = bf.bellman_ford(G2 , source)[0] 
        

        G3_BF = bf.bellman_ford(G3 , source)[0]  

        print("source", source)



        T = ut.union(G1_BF , G2_BF , G3_BF) 


        #----------------- Question 5 -------------------------------
        ordre = bf.GloutonFas(T)

        #----------------- Question 6 -------------------------------
        H_BF , nb_iter= bf.bellman_ford(H , source , ordre)
        print("Le nombre d'itération avec l'ordre ", ordre," est : ", nb_iter)
        nb_iter_with_gloutonFas_ordre.append(nb_iter)

        #----------------- Question 7 -------------------------------
        ordre_alea  = list(range(G.number_of_nodes()))
        random.shuffle(ordre_alea)

        H_BF_alea , nb_iter= bf.bellman_ford(H , source , ordre_alea)
        print("Le nombre d'itération avec l'ordre ", ordre_alea," est : ", nb_iter)
        nb_iter_alea.append(nb_iter)

    plt.plot( nb_iter_with_gloutonFas_ordre, 'b', label="Nombre d'itération avec l'orde de GloutonFast")
    plt.plot(nb_iter_alea, 'r', label="Nombre d'itérations avec un ordre aléatoire")
    plt.ylabel('Nombre d\'itération')
    plt.legend()
    plt.suptitle("Analyse du nombre d'itération de l'algorithme Bellman Ford" )
    plt.tight_layout()
    plt.savefig("Plots/Analyse du nombre d'itération de l'algorithme Bellman Ford.png")
    
    plt.show()


if __name__ == "__main__":
    main()
