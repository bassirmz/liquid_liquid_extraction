#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 17:09:44 2025

@author: bassar
"""
from utils import equations
import numpy as np
import sympy as sy

class ExtractionSystem:
    
    def __init__(self,R_stream,E_stream,a_matrix,F_stream = None):
        
        self.R = R_stream
        self.E = E_stream
        self.f = F_stream
        self.a = a_matrix
        
    def equations(self):
        
        eqs = []
        
        for i in range(4):
            
            first_term = self.R.composition[i] * self.R.flowrate + self.E.composition[i] * self.E.flowrate + self.F.composition[i] * self.F.flowrate
            second_term = self.R.composition[i+1] * self.R.flowrate + self.E.composition[i+1] * self.E.flowrate
            
            eqs.append(sy.Eq(first_term,second_term))
            
        eqs.append(sy.Eq(sum(self.R.composition[i] for i in range(4)),1))
        eqs.append(sy.Eq(sum(self.E.composition[i] for i in range(4)),1))
        
        for i in range(4):
            
            eqs.append(sy.Eq(np.exp(equations.lngamma(i, self.R.composition, self.a))/np.exp(equations.lngamma(i, self.E.composition, self.a)),self.E.composition[i]/self.R.composition[i]))
            
        return eqs
    