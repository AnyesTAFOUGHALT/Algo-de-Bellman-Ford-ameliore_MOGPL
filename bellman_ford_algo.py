import networkx as nx
import math
import utils   as ut

def bellman_ford(G , source, ordre = None):
    """
    G : un graphe dérigée 
    source : la source à partir de la quelle on applique Bellman Ford
    orde : l'ordre de traitement des noeuds

    return : la matrice des distance et le nombre d'itérations
    """
    N = len(list(G.nodes))
    ordre_traitement = list(G.nodes)
    if ordre!= None :
        ordre_traitement = ordre
    plus_courts_chemins = [] 
    distance = dict.fromkeys(list(G.nodes) , [math.inf, None])
    distance [source] = [0,None]
    plus_courts_chemins.append(distance)
    nb_etapes = 0
    while(nb_etapes<=N):
        #print("nb_etapes : ", nb_etapes , ", mat : ", plus_courts_chemins )
        nb_etapes += 1
        nouveaux_plus_courts_chemins = plus_courts_chemins[nb_etapes - 1].copy()

        for sommet in ordre_traitement :
            etape_precedente = plus_courts_chemins[nb_etapes - 1]

            for v in list(G.predecessors(sommet) ):
                new_chemin =  nouveaux_plus_courts_chemins[v][0] + G.get_edge_data(v,sommet)['weight']

                if new_chemin < nouveaux_plus_courts_chemins[sommet][0]:
                    nouveaux_plus_courts_chemins[sommet] = [new_chemin,v]
        
        if ut.sont_similaires(nouveaux_plus_courts_chemins,etape_precedente):
            break
        if nb_etapes <= N :
            plus_courts_chemins.append(nouveaux_plus_courts_chemins)

    return plus_courts_chemins , nb_etapes-1



def getSources(G):
    """ Cette fonction retourne une liste de tous les noeuds de G qui n'ont pas d'arcs entrants """
    s = []
    for v in list(G.nodes):
        if len(list(G.predecessors(v))) == 0 :
            s.append(v)
    return s


def getPuits(G):
    """ Cette fonction retourne une liste de tous les noeuds de G qui n'ont pas d'arcs sortants """
    p = []
    for v in list(G.nodes):
        if len(list(G.successors(v))) == 0 :
            p.append(v)
    return p


def getMaxiDiff(G):
    """ Cette fonction retourne le noeud dont la différence entre son nombre d'arcs sortants et entrants est maximale """
    maxDiff = -math.inf 
    v_max = None
    for v in list(G.nodes):
        new_diff = len(list(G.successors(v))) - len(list(G.predecessors(v)))
        if new_diff > maxDiff :
            maxDiff = new_diff
            v_max = v

    return v_max


def GloutonFas(G):
    s1,s2 = [] ,[]
    G_copy = G.copy()
    while(list(G_copy.nodes)!=[]):
        
        sources = getSources(G_copy)
        while(sources != []):
            s1.extend(sources)
            G_copy.remove_nodes_from(sources)
            sources = getSources(G_copy)

        puits =  getPuits(G_copy)
        while(puits != []):
            s2.extend(puits)
            G_copy.remove_nodes_from(puits)
            puits = getPuits(G_copy)

        sommet_max_diff = getMaxiDiff(G_copy)
        if(sommet_max_diff != None):
            s1.append(sommet_max_diff)
            G_copy.remove_node(sommet_max_diff)

    return s1+s2 

  
           
        






















