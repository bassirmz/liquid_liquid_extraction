#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 15:24:23 2025

@author: bassar
"""

class Stream:
    
    def __init__(self,name,flowrate,composition):
        
        self.name = name
        self.flowrate = flowrate
        self.composition = composition
        
    def __str__(self):
        
        return f"{self.name} stream\nflowrate = {self.flowrate} lb moles/hr"