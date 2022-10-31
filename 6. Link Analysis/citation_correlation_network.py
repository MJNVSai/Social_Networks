# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 17:36:06 2022

@author: SHREE
"""

import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = nx.read_edgelist('citation.txt', create_using = nx.DiGraph())
    
    deg = G.in_degree()
    print(deg)
    
    deg = dict(deg)
    pr = nx.pagerank(G)
    
    pr_values = []
    for i in deg.keys():
        pr_values.append(pr[i])
        
    plt.plot(deg.values(), pr_values, 'ro', markersize = 3)
    plt.xlabel('Degrees of nodes')
    plt.ylabel('Page Rank values of the nodes')
    
    plt.show()

#calling the main function    
main()