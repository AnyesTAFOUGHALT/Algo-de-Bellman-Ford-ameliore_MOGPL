import networkx as nx
import matplotlib.pyplot as plt
import random
import bellman_ford_algo2 as bf

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
      
def genrartion_de_graphes2(G):
    G_poid = G.copy()
    while True:
        for arete in list(G_poid.edges()): 
            G_poid[arete[0]][arete[1]]['weight'] = random.randint(-10, 10)

        possede_cycle = False
        for v in list(G.nodes):
            if has_negative_cycle(G_poid , v) :
                possede_cycle = True
                break
        if not possede_cycle  : 
            return G_poid
def genrartion_de_graphes(G):#racha
    G_poid = G.copy()
    for arete in list(G_poid.edges()): 
        G_poid[arete[0]][arete[1]]['weight'] = random.randint(-10, 10)
    while True:
        cycle = False
        cout = 0
        for v in list(G.nodes):
            pcc , nb_iter = bf.bellman_ford_3(G_poid , v)
            # print(pcc)
            cout = pcc[nb_iter][v][0]
            # print("cout:",cout,"nbiter",nb_iter)
            if cout<0:
                cycle = True
                G_poid[pcc[nb_iter][v][1]][v]['weight'] = -cout
        if not cycle:
            return G_poid

#-------------------------------------
#-------------Modiff Ajouter ----------
#--------------------------------------------
def generation_graphe(nb_sommets , p) : #La fonction que j'ai ajouter pour la génération de graphe
    G = nx.DiGraph()
    for source in range(nb_sommets) :
        for dist in range(nb_sommets) :
            if source!=dist :
                n = random.random()
                if n<p :
                    G.add_edge(source, dist)
    return G

        
def ajout_poids_graphe(G):
    G_poid = G.copy()
    N = len(list(G.nodes))
    for arete in list(G_poid.edges()): 
        G_poid[arete[0]][arete[1]]['weight'] = random.randint(-10, 10)

    for v in list(G.nodes):
        plus_court_chemin_mat , nb_iter = bf.bellman_ford_3(G_poid , v)
        if nb_iter > N-1: #il existe un cycle négatif
            cycle , cout = find_negatif_cycle(G_poid , plus_court_chemin_mat)
            #éléminer un cycle négatif
            G_poid[cycle[0][0]][cycle[0][1]]['weight'] += (1 - cout)
    return G_poid
        
def generation_graphe_niveaux_2(nb_sommets_par_niv , nb_niveaux , p) :
    G = nx.DiGraph()
    for n in range(nb_niveaux - 1) :
        for source in range(nb_sommets_par_niv) :
            for dist in range(nb_sommets_par_niv) :
                n = random.random()
                if n<p :
                    G.add_edge(source + nb_sommets_par_niv * n, dist + nb_sommets_par_niv * (n+1))
    return G

def generation_graphe_niveaux(nb_sommets_par_niv , nb_niveaux , p) :#racha
    G = nx.DiGraph()
    suiv = [i for i in range(nb_sommets_par_niv)]
    if nb_niveaux == 1 :
        for i in suiv :
                G.add_node(i)
    else :
        for n in range(nb_niveaux-1) :
            l=[]
            for source in range(nb_sommets_par_niv) :
                for dist in range(nb_sommets_par_niv) :
                    f = 1 #random.random()
                    G.add_node(suiv[source])
                    G.add_node(dist + nb_sommets_par_niv * (n+1))
                    if f>p :
                        G.add_edge(suiv[source], dist + nb_sommets_par_niv * (n+1))
                l.append(source + nb_sommets_par_niv * (n+1))

            suiv = l
                    
    return G
def generation_graphe_PCC( G , plus_courts_chemins) :
    new_G = nx.DiGraph()
    for v in list(G.nodes) :
        s = plus_courts_chemins[v][1]
        if s != None :
            new_G.add_edge(s, v, weight=G.get_edge_data(s, v)['weight'])
    return new_G

def find_negatif_cycle(G , plus_courts_chemins_Mat) :
    length = len(plus_courts_chemins_Mat)
    N = plus_courts_chemins_Mat[length-1]
    N_1 = plus_courts_chemins_Mat[length-2]

    s = None
    for v in list(G.nodes) :
        if N[v][0] < N_1[v][0] :
            s = v
            break
    dist = s
    source = N[dist][1]
    cycle = []
    cout = 0
    while(source != s) :
        cycle.append((source , dist))
        cout += G.get_edge_data(source, dist)['weight']
        dist = source
        source = N[dist][1]
    cycle.append((source , dist))
    cout += G.get_edge_data(source, dist)['weight']
    return cycle , cout




#------------------Fin Modiff-------------------
def union(listG):
    T = nx.DiGraph()

    for G in listG:
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