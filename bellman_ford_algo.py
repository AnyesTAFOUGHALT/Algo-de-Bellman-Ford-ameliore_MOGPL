import networkx as nx
import math

def bellman_ford(G , source):
    """
    Ajouter le nb d'itérations
    """
    distance = dict.fromkeys(list(G.nodes) , [math.inf, None])
    distance[source] = [0 , None]
    L = [source]
    while L!=[] :
        successors = list(G.successors(L[0]))
        for v in successors :
            new_dist = distance[L[0]][0] + G.get_edge_data(L[0], v)['weight']
            if new_dist < distance[v][0] :
                distance[v] = [new_dist , L[0]]
        L.remove(L[0])
        L.extend(successors)
    new_G = nx.DiGraph()
    for v in list(G.nodes) :
        s = distance[v][1]
        if s != None :
            new_G.add_edge(s, v, G.get_edge_data(s, v)['weight'])
    return new_G
    



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
    G_copy = G.copy
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
ssss
        
            
        






















