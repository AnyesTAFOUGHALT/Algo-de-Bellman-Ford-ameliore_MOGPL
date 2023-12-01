import networkx as nx
import matplotlib.pyplot as plt
import random

def sont_similaires(dict1, dict2):
    # Vérifier si les clés des deux dictionnaires sont les mêmes
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # Vérifier si les valeurs associées à chaque clé sont les mêmes
    for key in dict1:
        if dict1[key] != dict2[key]:
            return False

    # Si aucune différence n'a été trouvée, les dictionnaires sont similaires
    return True
    
def draw_graph(G,titre , pos = None):
    """#Positionnement des nœuds
    if pos == None :
        pos = nx.spring_layout(G)
    plt.figure()

    # Afficher le graphe avec les poids
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_color='skyblue', edge_color='gray', arrowsize=20)

    # Ajouter les étiquettes de poids sur les arêtes
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    plt.title(titre)

    plt.show()
    return pos"""

    if pos is None:
        pos = nx.spring_layout(G, seed=42)  # Utilisation d'une graine pour la reproductibilité

    plt.figure(figsize=(10, 8))  # Ajuster la taille de la figure selon les besoins

    # Afficher le graphe avec les poids
    nx.draw(
        G,
        pos,
        with_labels=True,
        font_weight='bold',
        node_color='skyblue',
        edge_color='gray',
        arrowsize=20,
        width=2,  # Largeur des arêtes
        alpha=0.7,  # Transparence des arêtes
        connectionstyle='arc3,rad=0.1',  # Style de connexion des arêtes
    )

    # Ajouter les étiquettes de poids sur les arêtes
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    plt.title(titre)
    plt.axis('off')  # Désactiver les axes pour une meilleure présentation

    plt.show()
    return pos

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
    T = nx.DiGraph()

    for G in [G1 , G2 , G3]:
        for arete in G.edges(data=True):
            u , v , data = arete
            if not T.has_edge(u,v):
                T.add_edge(u , v)
    return T

def source(G) :
    n = G.number_of_nodes()/2
    for v in list(G.nodes) :
        if len(nx.descendants(G, v) ) >= n :
            return v
    return None