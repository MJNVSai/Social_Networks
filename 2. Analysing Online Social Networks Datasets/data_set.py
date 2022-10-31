# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
import matplotlib.pyplot as plt

def plot_deg_dist(G):
    ''' Graph Plot Distribution '''
    all_degrees = dict(nx.degree(G)).values()
    ad = list(dict(nx.degree(G)).values())
    Unique_degrees = list(set(all_degrees))
    
    count_of_degrees = []
    
    for i in Unique_degrees:
        #x = all_degrees.count(i)
        x = ad.count(i)
        count_of_degrees.append(x)
        
    #plt.plot(Unique_degrees, count_of_degrees, 'y*-')
    plt.loglog(Unique_degrees, count_of_degrees, 'y*-')
    plt.xlabel('Degrees')
    plt.ylabel('No of Nodes')
    plt.title('Degree Distribution of Karate Network')
    plt.show()
    



G = nx.read_edgelist('facebook_combined.txt/facebook_combined.txt')

print("Facebook info : \n", nx.info(G))
print("No of Nodes : ", nx.number_of_nodes(G))
print("No of Edges : ", nx.number_of_edges(G))
print("Directed graph or not Directed : ", nx.is_directed(G))

print()
print()

P = nx.read_pajek('football.net')
print("Football info : \n", nx.info(P))
print("No of Nodes : ", nx.number_of_nodes(P))
print("No of Edges : ", nx.number_of_edges(P))
print("Directed graph or not Directed : ", nx.is_directed(P))

print()
print()

P1 = nx.read_pajek('karate.paj')
print("Karate info : \n", nx.info(P1))
print("No of Nodes : ", nx.number_of_nodes(P1))
print("No of Edges : ", nx.number_of_edges(P1))
print("Directed graph or not Directed : ", nx.is_directed(P1))
print("Degree at each node: ", nx.degree(P1)) 
us = list(set(dict(nx.degree(P1)).values()))
print("Unique value degree : ", us)
print("values at degree at each node : \n", dict(nx.degree(P1)).values())

print()
print()

#P2 = nx.read_gml('karate.gml')
#print("Karate2 info : \n", nx.info(P2))
#print("No of Nodes : ", nx.number_of_nodes(P2))
#print("No of Edges : ", nx.number_of_edges(P2))
#print("Directed graph or not Directed : ", nx.is_directed(P2))

#W = nx.read_graphml(str('wiki.graphml'))
#print("Wikipedia info : \n", nx.info(W))
#print("No of Nodes : ", nx.number_of_nodes(W))
#print("No of Edges : ", nx.number_of_edges(W))
#print("Directed graph or not Directed : ", nx.is_directed(W))

print()
print()

#G1 = nx.read_gexf('eurosis.gexf/EuroSiS Generale Pays.gexf')
#print("Eurosis info : \n", nx.info(G1))
#print("No of Nodes : ", nx.number_of_nodes(G1))
#print("No of Edges : ", nx.number_of_edges(G1))
#print("Directed graph or not Directed : ", nx.is_directed(G1))

plot_deg_dist(P1)

print("Densites of the Complete Graph : ")
cg = nx.complete_graph(100)
print("Density : ", nx.density(cg))

print("Clustering value at each node : ")
cv = nx.clustering(G)
#print("values are :", cv)

for i in cv.items():
    print("Clustering at a node : ", i)
    
print("Average clustering value : ", nx.average_clustering(G))

print("Diameter of the graph is : ", nx.diameter(G))


print("Graph Visulization : ")
nx.draw_circular(P1) # use G also
plt.show()