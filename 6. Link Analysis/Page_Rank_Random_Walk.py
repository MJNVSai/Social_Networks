# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 16:57:56 2022

@author: SHREE
"""

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

def add_edges(G, p):
    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                r = random.random()
                if r == p:
                    G.add_edge(i, j)
                else:
                    continue
                
    return G

def get_nodes_sorted_by_RW(points):
    points_array = np.array(points)
    nodes_sorted_by_RW = np.argsort(-points_array)
    
    return sorted(nodes_sorted_by_RW)

def random_walk(G):
    # Walking through random
    nodes = list(G.nodes())
    RW_points = [0 for i in range(G.number_of_nodes())]
    r = random.choice(nodes)
    RW_points[r] += 1
    out = G.out_edges(r)
    
    c = 0
    while c != 100000:
        if len(out) == 0:
            focus = random.choice(nodes)
        else:
            r1 = random.choice(out)
            focus = r1[1]
        RW_points[focus] += 1
        out = G.out_edges(focus)
        c += 1
        
    return RW_points

def main():
    # create a Directed graph
    G = nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    G = add_edges(G, 0.3)
    
    # Perform Random Walk
    RW_points = random_walk(G)
    
    # Get sorted nodes as per points accumulated during random walk
    nodes_sorted_by_RW = get_nodes_sorted_by_RW(RW_points)
    print("Sorted Nodes ranked on by random walk method : ", nodes_sorted_by_RW)
    
    # compare the ranks obtained by derived code/algorithm and inbuilt ranking function
    pr = nx.pagerank(G)
    pr_sorted = sorted(pr.items(), key = lambda x : x[1], reverse = True)
    print("Ranking got by inbuilt Method sorted nodes are : ", end = "")
    pr_final = []
    for i in pr_sorted:
        print(i[0], end = " ")
        pr_final.append(i[0])
        
    # Generating the Comparision Graph
    plt.plot(nodes_sorted_by_RW, pr_final, 'b-')
    plt.xlabel("Ranked By Derived Code Method")
    plt.ylabel("ranked By Inbuilt Method")
    plt.title("Page Rank Distribution")
    plt.show()
    
    
# calling the main function
main()

