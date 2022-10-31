# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)

print("Show all Nodes : ", G.nodes())

G.add_node(10)
G.add_node(11)
G.add_node(12)

G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,4)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(2,5)
G.add_edge(4,6)
G.add_edge(5,4)
G.add_edge(2,12)

print("Show all edges : ", G.edges())

# H = nx.Graph()

# nx.draw(G)
# plt.show()

# nx.draw(G, with_labels = 1)
# plt.show()


z = nx.complete_graph(10)
print("Nodes in complete graph : ", z.nodes())
print("Edges in complete Graph : ", z.edges())
print("No of Nodes in the Complete Graph : ", z.order())
print("No.of edges in the complete graph : ", z.size())

# nx.draw(z, with_labels = 1)
# plt.show()

H = nx.complete_graph(100)
print("Nodes in complete graph : ", H.nodes())
print("Edges in complete Graph : ", H.edges())
print("No of Nodes in the Complete Graph : ", H.order())
print("No.of edges in the complete graph : ", H.size())

nx.draw(H, with_labels = 1)
plt.show()

g = nx.gnp_random_graph(20, 0.5) # 20 is no of nodes and 0.5 is the probability of edges
nx.draw(g, with_labels = 1)
plt.show()















