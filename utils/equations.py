#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 15:51:36 2025

@author: bassar
"""

def a_star(a,i,j,k):
    
    result = a[i,j] + a[j,i] + a[i,k] + a[j,k] + a[k,j]
    
    return result

def lngamma(i,x,a):
    
    term1 = (2*x[i]) * sum(x[j]*a[j,i] for j in range(3))
    
    term2 = sum((x[j]**2)*a[i,j] for j in range(3))
    
    term3 = 0
    for j in range(3):
        
        if j == i :
            continue
        
        for k in range(3):
            
            if k == i or k >= j:
                continue
            
            term3 += x[j]*x[k]*a_star(a, i, j, k)
            
    term4 = 0
    for j in range(3):
        
        for k in range(3):
            
            term4 += x[j]**2 * x[k]
            
    term4 = term4 * (-2)
    
    term5 = 0 
    
    for j in range(3):
        for k in range(3):
            for q in range(3):
                term5 += x[j]*x[k]*x[q]*a_star(a,j,k,q)
                
    term5 = term5* (-2)
    
    return term1 + term2 + term3 + term4 + term5