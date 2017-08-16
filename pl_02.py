#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 11:51:31 2017

@author: palazzom
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

def f1(x):
    return (-1.5)*x+1200
def f2(x):
    return 0*x+800
def f3(x):
    return -100000*x+10000
def f0(x):
    return 0*x+0

def Z(x,z):
    return (-5/2)*x+0.5*z



################################# PLOT RESTRICTIONS ##################################
################################# PLOT RESTRICTIONS ##################################
################################# PLOT RESTRICTIONS ##################################
################################# PLOT RESTRICTIONS ##################################

x = Symbol('x')
x0  = 0
x1, =  solve(f1(x)-f2(x))
x2 =  600
x3 =  600


y0 = f2(0)
y1 = f1(x1)
y2 = f1(x2)
y3 = 0

y2

plt.plot(0,0,'go',markersize=10)
plt.plot(0,y0,'go',markersize=10)
plt.plot(x1,y1,'go',markersize=10)
plt.plot(x2,y2,'go',markersize=10)
plt.plot(x3,y3,'go',markersize=10)

plt.fill([x0,x0,x1,x2,x3],[0,y0,y1,y2,y3],'yellow',alpha=0.5)


xr = np.linspace(-10,650,100)
y1r = f1(xr)
y2r = f2(xr)
y3r = f3(xr)
#zr0 =Z(np.linspace(-20,20,100),0)
#zr1 = Z(np.linspace(-20,350,100),1600)
#zr2 = Z(np.linspace(-10,650,100),2930)
zr3 = Z(np.linspace(-10,800,100),3600)
#zr4 = Z(np.linspace(-10,160,100),175)

plt.plot(xr,y1r,'k--')
plt.plot(xr,y2r,'k--')
#plt.plot(xr,y3r,'k--')
#plt.plot(xr,y3r,'k--')
#plt.plot(np.linspace(-20,20,100),zr0)
#plt.plot(np.linspace(-20,350,100),zr1)
#plt.plot(np.linspace(-10,650,100),zr2)
plt.plot(np.linspace(-10,800,100),zr3)
#plt.plot(np.linspace(-10,160,100),zr4)

plt.show()




