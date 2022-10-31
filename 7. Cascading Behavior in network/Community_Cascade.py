# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 21:07:36 2022

@author: SHREE
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

def create_first_community(G):
    for i in range(0,10):
        G.add_node(i)
    
    for i in range(0,10):
        for j in range(0,10):
            if i < j:
                r = random.uniform(0, 1)
                if r < 0.5:
                    G.add_edge(i,j)
                    
def create_second_community(G):
    for i in range(11,20):
        G.add_node(i)
    
    for i in range(11,20):
        for j in range(11,20):
            if i < j:
                r = random.uniform(0, 1)
                if r < 0.5:
                    G.add_edge(i,j)
                    

def set_all_B(G):
    for each in G.nodes():
        G.nodes[each]['action'] = 'B'

def set_A(G, list1):
    for each in list1:
        G.nodes[each]['action'] = 'A'

def get_colors(G):
    list1 = []
    for each in G.nodes():
        if G.nodes[each]['action'] == 'B':
            list1.append('red')
        else:
            list1.append('green')
    return list1

def find_neigh(each, c, G):
    num = 0
    for each1 in list(G.neighbors(each)):
        if G.nodes[each1]['action'] == c:
            num = num + 1
    return num

def recalculate_options(G):
    dict1 = {}
    # payoff (A) = a = 4
    # payoff (B) = b = 3
    
    a = 9
    b = 5
    for each in G.nodes():
        num_A = find_neigh(each, 'A', G)
        num_B = find_neigh(each, 'B', G)
        payoff_A = a*num_A
        payoff_B = b*num_B
        
        if payoff_A >= payoff_B:
            dict1[each] = 'A'
        else:
            dict1[each] = 'B'
            
    return dict1

def reset_node_attributes(G, action_dict):
    for each in action_dict:
        G.nodes[each]['action'] = action_dict[each]

def terminate_1(c, G):
    f = 1
    for each in G.nodes():
        if G.nodes[each]['action'] != c:
            f = 0
            break
    return f

def terminate(G, count):
    flag1 = terminate_1('A', G)
    flag2 = terminate_1('B', G)
    if flag1 == 1 or flag2 == 1 or count >= 100:
        return 1
    else:
        return 0
                    
G = nx.Graph()
create_first_community(G)
create_second_community(G)
G.add_edge(5,15)

#nx.write_gml(G, 'random_graph_community.gml')

for u in G.nodes():
    for v in G.nodes():
        if u < v:
            print("values of U & V are : ", u, " ", v)
            list1 = []
            list1.append(u)
            list1.append(v)

            set_all_B(G)

            #list1 = [4,1]
            set_A(G, list1)

            colors = get_colors(G)
            #nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
            #plt.show()

            #action_dict = recalculate_options(G)
            #reset_node_attributes(G, action_dict)


            flag = 0
            count = 0
            while 1:
                flag = terminate(G, count)
                if flag == 1:
                    break
                
                count = count + 1
                action_dict = recalculate_options(G)
                
                reset_node_attributes(G, action_dict)
    
            c = terminate_1('A', G)
            if c == 1:
                print("Cascade is complete")
            else:
                print("Cascade is Incomplete")
            print()


            colors = get_colors(G)
            nx.draw(G, node_color = colors, node_size = 800, with_labels = True)
            plt.show()