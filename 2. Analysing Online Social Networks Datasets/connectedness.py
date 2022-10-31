# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 12:04:35 2022

@author: SHREE
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

# Add n number of nodes in  the graph and return it.
def add_nodes(n):
    ''' ..... '''
    G = nx.Graph()
    G.add_nodes_from(range(n))
    return G

# add one random edge 
def add_random_edge(G):
    ''' .... '''
    v1 = random.choice(list(G.nodes()))
    v2 = random.choice(list(G.nodes()))
    
    if v1 != v2:
        G.add_edge(v1,v2)
    return G

# it add random edges in graph until it becomes connected
def add_till_connectivity(G):
    ''' .... '''
    while nx.is_connected(G) == False:
        G = add_random_edge(G)
        
    return G

# creates an instance od entire process. it takes as input number of nodes and 
# returns the number of edges for connectivity.

def create_instance(n):
    ''' ..... '''
    G = add_nodes(n)
    G = add_till_connectivity(G)
    
    return G.number_of_edges()

# Average it over 100 instances
def create_avg_instance(n):
    ''' .... '''
    list1 = []
    for i in range(0,100):
        list1.append(create_instance(n))
        
    return np.average(list1)

# plot the desired for different number of edges

def plot_connectivity():
    ''' ..... '''
    x = []
    y = []
    i = 10 # it tells no of nodes
    
    while i <= 400:
        x.append(i)
        y.append(create_avg_instance(i))
        i = i + 10
     
    plt.xlabel("Number of Nodes")
    plt.ylabel("Number of edges required to connect the graph")
    plt.title("Emergence of Connectivity")
    plt.plot(x,y)
    
    x1 = []
    y1 = []
    i1 = 10
    
    while i1 <= 400:
        x1.append(i1)
        y1.append(i1*np.log(i1))
        # y1.append(i1*float(np.log(i1))//2)
        i1 = i1 + 10
        
    plt.plot(x1, y1)
    
    plt.show()


g = add_nodes(10)
print("No of nodes : ", g.number_of_nodes())
print("Connected or not : ", nx.is_connected(g))

g1 = add_random_edge(g)
print("new edge added : ", g1.edges())

g2 = add_till_connectivity(g1)
print("Total edges in a g2 : ", g2.edges())
print("Total no of edges : ", g2.number_of_edges())
print("Connected or not : ", nx.is_connected(g2))

d = create_instance(10)
print("No of edges required for connectivity : ", d)

plot_connectivity()

 