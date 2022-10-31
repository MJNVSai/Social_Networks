# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:05:39 2022

Travelling Sales Man Problem

1. Modelling road network of India's cities'

@author: SHREE
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import sys

def create_network(city_set, costs, num_edges):
    # print("hola")
    G = nx.Graph() # It creates a undirected Graph
    
    for each in city_set:
        G.add_node(each)
        
    # we are going to addd 16 edges
    while(G.number_of_edges() < num_edges):
        c3 = G.nodes()
        c3 = list(c3)
        c1 = random.choice(c3)
        c2 = random.choice(c3)
        if c1!=c2 and G.has_edge(c1,c2) == 0:
            w = random.choice(costs)
            G.add_edge(c1,c2, weight = w)
            
    return G

# G = nx.DiGraph() # it creates an directed graph

city_set = ['Delhi', 'Bangalore', 'Hyderabad', 'Ahmedabad', 'Chennai', 'Kolkata', 'Surat', 'Pune', 'Jaipur']   


    
#nx.draw(G, with_labels = 1)
#plt.show()

costs = []
value = 100

while value <= 2000:
    costs.append(value)
    value = value + 100

print("Costs array : ", costs)

G = create_network(city_set, costs, 10) # 4 represents no of edges.


pos = nx.circular_layout(G)
pos1 = nx.spectral_layout(G)
pos2 = nx.spring_layout(G)

print("to check graph is connected or not : ", nx.is_connected(G))

for u in G.nodes():
    for v in G.nodes():
        print("path between cites : ", u, v, " ==> ", nx.has_path(G,u,v))

# Shortest path Functions they are in networkx module

u = 'Delhi'
v = 'Kolkata'
#print("Shortest path : ", nx.dijkstra_path(G,u,v))

nx.draw(G, pos, with_labels = 1)
#nx.draw(G, pos)
#nx.draw_networkx_edge_labels(G,pos)
plt.show()

print("Shortest path : ", nx.dijkstra_path(G,u,v))

u1 = 'Bangalore'
v1 = 'Surat'

try:
    print("Shortest path : ", nx.dijkstra_path(G,u1,v1))

    print("Path length betwen cites : ", u1, " and ", v1, nx.dijkstra_path_length(G,u1,v1))
    
except:
    print("An unknown error occured")
        


