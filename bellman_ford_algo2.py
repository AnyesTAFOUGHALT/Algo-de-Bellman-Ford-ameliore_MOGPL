import networkx as nx
import math
import utils   as ut

# def bellman_ford(G , source, ordre = None):
#     """
#     Ajouter le nb d'itérations
#     """

#     ordre_traitement = list(G.nodes)
#     if ordre!= None :
#         ordre_traitement = ordre
#     plus_courts_chemins = [] 
#     distance = dict.fromkeys(list(G.nodes) , [math.inf, None])
#     distance [source] = [0,None]
#     plus_courts_chemins.append(distance)
#     nb_etapes = 1

#     while(True): 
#         nouveaux_plus_courts_chemins = plus_courts_chemins[nb_etapes-1].copy()
#         for sommet in ordre_traitement :
#             etape_precedente = plus_courts_chemins[nb_etapes-1]
#             for v in list(G.predecessors(sommet) ):
#                 new_chemin =  etape_precedente[v][0] + G.get_edge_data(v,sommet)['weight']

#                 if new_chemin < nouveaux_plus_courts_chemins[sommet][0]:
#                     nouveaux_plus_courts_chemins[sommet] = [new_chemin,v]
                
            

#         if ut.sont_similaires(nouveaux_plus_courts_chemins,plus_courts_chemins[nb_etapes-1]):
#             plus_courts_chemins.append(nouveaux_plus_courts_chemins)
#             new_G = nx.DiGraph()
#             distance = plus_courts_chemins[nb_etapes-1]
#             for v in list(G.nodes) :
#                 s = distance[v][1]
#                 if s != None :
#                     new_G.add_edge(s, v, weight=G.get_edge_data(s, v)['weight'])
#             return new_G , nb_etapes-1
#         else : 
#             nb_etapes += 1
#             plus_courts_chemins.append(nouveaux_plus_courts_chemins)


# def bellman_ford_2(G , source, ordre = None):
#     """
#     Ajouter le nb d'itérations
#     """
#     N = len(list(G.nodes))
#     ordre_traitement = list(G.nodes)
#     if ordre!= None :
#         ordre_traitement = ordre
#     plus_courts_chemins = [] 
#     distance = dict.fromkeys(list(G.nodes) , [math.inf, None])
#     distance [source] = [0,None]
#     plus_courts_chemins.append(distance)
#     nb_etapes = 0
#     print("ordre de traitement est ",ordre_traitement)
#     while(nb_etapes<N):
#         nb_etapes += 1
#         nouveaux_plus_courts_chemins = plus_courts_chemins[nb_etapes - 1].copy()
#         for sommet in ordre_traitement :
#             etape_precedente = plus_courts_chemins[nb_etapes - 1]
#             for v in list(G.predecessors(sommet) ):
#                 new_chemin =  nouveaux_plus_courts_chemins[v][0] + G.get_edge_data(v,sommet)['weight']

#                 if new_chemin < nouveaux_plus_courts_chemins[sommet][0]:
#                     nouveaux_plus_courts_chemins[sommet] = [new_chemin,v]
        
#         if ut.sont_similaires(nouveaux_plus_courts_chemins,etape_precedente):
#             break
#         plus_courts_chemins.append(nouveaux_plus_courts_chemins)
        
#     new_G = nx.DiGraph()
#     distance = plus_courts_chemins[nb_etapes -1]
#     print(plus_courts_chemins )
#     for v in list(G.nodes) :
#         s = distance[v][1]
#         if s != None :
#             new_G.add_edge(s, v, weight=G.get_edge_data(s, v)['weight'])
#     return new_G , nb_etapes-1

def bellman_ford_3(G , source, ordre = None):
    """
    Ajouter le nb d'itérations
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
    #print("ordre de traitement est ",ordre_traitement)
    while(nb_etapes<=N):
        nb_etapes += 1
        nouveaux_plus_courts_chemins = plus_courts_chemins[nb_etapes - 1].copy()
        for sommet in ordre_traitement :
            etape_precedente = plus_courts_chemins[nb_etapes - 1]
            for v in list(G.predecessors(sommet) ):
                #print("v",v,"sommet",sommet)
                new_chemin =  nouveaux_plus_courts_chemins[v][0] + G.get_edge_data(v,sommet)['weight']
                if new_chemin < nouveaux_plus_courts_chemins[sommet][0]:
                    nouveaux_plus_courts_chemins[sommet] = [new_chemin,v]
        
        if ut.sont_similaires(nouveaux_plus_courts_chemins,etape_precedente):
            break
        if(nb_etapes <= N):
            plus_courts_chemins.append(nouveaux_plus_courts_chemins)

    # if nb_etapes>N  :
    #     return plus_courts_chemins[nb_etapes] ,nb_etapes
      
    # new_G = nx.DiGraph()
    # distance = plus_courts_chemins[nb_etapes - 1]
    # print(plus_courts_chemins )
    # for v in list(G.nodes) :
    #     s = distance[v][1]
    #     if s != None :
    #         new_G.add_edge(s, v, weight=G.get_edge_data(s, v)['weight'])
    return plus_courts_chemins , nb_etapes-1



def getSources(G):
    s = []
    for v in list(G.nodes):
        if len(list(G.predecessors(v))) == 0 :
            s.append(v)
    return s


def getPuits(G):
    p = []
    for v in list(G.nodes):
        if len(list(G.successors(v))) == 0 :
            p.append(v)
    return p


def getMaxiDiff(G):
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

  
           
        






















