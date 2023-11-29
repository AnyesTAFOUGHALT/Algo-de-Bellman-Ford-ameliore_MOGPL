import utils as ut
import networkx as nx
import bellman_ford_algo as bf
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

G= nx.DiGraph()
G.add_edge(1, 2 , weight=2)
G.add_edge(1, 3 , weight=1)
G.add_edge(3, 2 , weight=1)
G.add_edge(2, 4 , weight=1)
G.add_edge(3, 4 , weight=3)
G.add_edge(1, 4 , weight=5)
# ut.draw_graph(G)
# ut.draw_graph(bf.bellman_ford(G,1))

ut.draw_graph(ut.genrartion_de_graphes(G))"""

N = 4
p = 0.6

def main() :
    G = nx.erdos_renyi_graph(N, p, directed=True)

    G1 = ut.genrartion_de_graphes(G)
    G2 = ut.genrartion_de_graphes(G)
    G3 = ut.genrartion_de_graphes(G)
    ut.draw_graph(G1)
    source = 1

    G1_BF = bf.bellman_ford(G1 , source)   
    G2_BF = bf.bellman_ford(G2 , source)    
    G3_BF = bf.bellman_ford(G3 , source)    

    T = ut.union(G1_BF , G2_BF , G3_BF) 
    
if __name__ == "__main__":
    main()