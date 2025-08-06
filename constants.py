#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 15:11:07 2025

@author: bassar
"""
#0 index : acetone
#1 index : ethanol
#2 index : chloroform
#3 index : water

import sympy as sy

a_matrix = sy.Matrix([[0.0,0.5446,0.9417,1.872],[0.599,0.0,1.61,1.46],[0.674,0.501,0.0,5.91],[1.388,0.877,4.76,0.0]])

feed_composition = [0.5,0.5,0,0]
feed_flow = 20

xE1 = 0.015

xR0 = 2 * 10**(-7)