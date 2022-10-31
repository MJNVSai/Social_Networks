# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:28:48 2022

@author: SHREE
"""

import numpy as np

'''
A = np.mat('1 2; 3 4')
v = np.mat('1; 1')

print(A*v)
'''

A = np.mat('1 2; 3 4')
v = np.mat('4; 11')
print(A*v)

print("#"*20)

for i in range(10):
    z = A*v
    z = z/np.linalg.norm(z) #denominator sqrt(a^2+ b^2)
    v = z
    print(z)
    
    print("*"*20)