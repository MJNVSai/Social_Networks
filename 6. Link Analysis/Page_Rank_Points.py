# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 20:02:25 2022

@author: SHREE
"""

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt

def add_edges(G, p):
    # Adding edges to the Graph.
    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                r = random.random()
                if r <= p:
                    G.add_edge(i,j)
                else:
                    continue
    return G

def initialize_points(G):
    # Giving the points to each and every Node in the directed graph
    points = [100 for i in range(G.number_of_nodes())]
    
    return points

def distribute_points(G, points):
    # Distributing the points for only one iteration 
    prev_points = points
    new_points = [0 for i in range(G.number_of_nodes())]
    
    for i in G.nodes():
        out = G.out_edges(i)
        if len(out) == 0:
            new_points[i] += prev_points[i]
        else:
            share = float(prev_points[i])/len(out)
            for each in out:
                new_points[each[1]] += share
    
    return G, new_points

def keep_distributing_points(G, points):
    # Keep calling the distribute function for convergence.
    prev_points = points
    print("Enter # to stop the Infinite loop....")
    while 1:
        G, new_points = distribute_points(G, prev_points)
        print("New points are : ", new_points)
        
        char = input("Do you want to continue or to stop : ")
        if char == '#':
            break
        prev_points = new_points
        
    return G, new_points

def handle_points_sink(G, points):
    # handling the points in each and every node in the directed graph
    for i in range(len(points)):
        points[i] = float(points[i])*0.8
        
    n = G.number_of_nodes()
    extra = float(n*100*0.2)/n
    for i in range(len(points)):
        points[i] += extra
        
    return points

def keep_update_distributing_points(G, points):
    # Keep calling the distribute function for convergence.
    prev_points = points
    print("Enter # to stop the Infinite loop....")
    while 1:
        G, new_points = distribute_points(G, prev_points)
        print("New points are : ", new_points)
        
        new_points = handle_points_sink(G, new_points)
        
        char = input("Do you want to continue or to stop : ")
        if char == '#':
            break
        prev_points = new_points
        
    return G, new_points
        
def get_nodes_sorted_by_points(points):
    # sorting the points
    points_array = np.array(points)
    nodes_sorted_by_points = np.argsort(-points_array)
    
    #return sorted(nodes_sorted_by_points)
    return nodes_sorted_by_points

def main():
    # Create/Take a Directed Graph with 'n' Nodes.
    G = nx.DiGraph()
    G.add_nodes_from([i for i in range(10)])
    G = add_edges(G, 0.3)
    
    # Assign 100 points to each node.
    points = initialize_points(G)
    print("initial nodes points : ", points)
    
    # Keep Distributing points until Convergence.
    # G, points = keep_distributing_points(G, points)
    G, points = keep_update_distributing_points(G, points)
    
    # Get nodes ranking as per the points accumulated...
    nodes_sorted_by_points = get_nodes_sorted_by_points(points)
    print("\nRanking got by Derived code Sorted nodes points are : ", nodes_sorted_by_points)
    
    # compare the ranks obtained by derived code/algorithm and inbuilt ranking function
    pr = nx.pagerank(G)
    pr_sorted = sorted(pr.items(), key = lambda x : x[1], reverse = True)
    print("Ranking got by inbuilt Method sorted nodes are : ", end = "")
    pr_final = []
    for i in pr_sorted:
        print(i[0], end = " ")
        pr_final.append(i[0])
        
    # Generating the Comparision Graph
    plt.plot(nodes_sorted_by_points, pr_final, 'b-')
    plt.xlabel("Ranked By Derived Code Method")
    plt.ylabel("ranked By Inbuilt Method")
    plt.title("Page Rank Distribution")
    plt.show()
    
    
    
# calling the main function
main()
    