# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 19:46:30 2022

@author: SHREE
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import itertools

def communites_brute(G):
    ''' .... '''
    nodes = G.nodes()
    n = G.number_of_nodes()
    
    first_community = []
    for i in range(1, n//2 + 1):
        comb = [tuple(x) for x in itertools.combinations(nodes, i)]
        first_community.extend(comb)

    second_community = []
    for i in range(len(first_community)):
        l = list(set(nodes) - set(first_community))
        second_community.append(l)

    # Which division is the best one ?
    num_intra_edges1 = []
    num_intra_edges2 = []
    num_inter_edges = []
    ratio = [] # ratio of number of intra / number of inter community edges

    for i in range(len(first_community)):
        sg = G.subgraph(first_community[i]).number_of_edges()
        num_intra_edges1.append(sg) 
        
    for i in range(len(second_community)):
        sg1 = G.subgraph(second_community[i]).number_of_edges()
        num_intra_edges2.append(sg1) 
        
    e = G.number_of_edges()
    for i in range(len(first_community)):
        te = e - num_intra_edges1[i] - num_intra_edges2[i]
        num_inter_edges.append(te)
        
    # Finding the ratio
    for i in range(len(first_community)):
        if num_inter_edges[i] != 0:
            r = (num_intra_edges1[i] + num_intra_edges2[i])/num_inter_edges[i]
            ratio.append((float(r)))
    
    max_value = max(ratio)
    max_index = ratio.index(max_value)
    
    fc = first_community[max_index]
    sc = second_community[max_index]
    
    print('(', fc, ')', '(', sc, ')')
    
                     
    
s = itertools.combinations([1,2,3,4], 2)

for i in s:
    print("i value : ", list(i))
    
    
G1 = nx.barbell_graph(10, 0)

communites_brute(G1)

nx.draw(G1)
plt.show()
    