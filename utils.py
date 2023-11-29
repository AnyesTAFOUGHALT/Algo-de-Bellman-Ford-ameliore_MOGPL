import networkx as nx
import matplotlib.pyplot as plt
import random

def draw_graph(G):
    #Positionnement des nœuds
    pos = nx.spring_layout(G)

    # Afficher le graphe avec les poids
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', edge_color='gray', arrowsize=20)

    # Ajouter les étiquettes de poids sur les arêtes
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

def has_negative_cycle(graph , source):
    try:
        # Utiliser l'algorithme de détection de cycle négatif
        cycle = nx.find_negative_cycle(graph,source, weight='weight')
        return True
    except nx.NetworkXError :
        return False
      
def genrartion_de_graphes(G):
    G_poid = G.copy()
    while True:
        for arete in list(G_poid.edges()): 
            G_poid[arete[0]][arete[1]]['weight'] = random.randint(-10, 10)

        possede_cycle = False
        for v in list(G.nodes):
            if has_negative_cycle(G_poid , v) :
                possede_cycle = True
                break
        if not possede_cycle : 
            return G_poid

def union(G1 , G2 , G3):
    for v in list(G1.nodes):
        print(G1.edges(data=True))
        print(G2.edges(data=True))
        print(G3.edges(data=True))