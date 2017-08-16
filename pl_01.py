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
    return (-1/3)*x+(200/3)
def f2(x):
    return (-1)*x+150
def f3(x):
    return 0*x+60
def f0(x):
    return 0

def Z(x,z):
    return -0.5*x+0.5*z



################################# PLOT RESTRICTIONS ##################################
################################# PLOT RESTRICTIONS ##################################
################################# PLOT RESTRICTIONS ##################################
################################# PLOT RESTRICTIONS ##################################

x = Symbol('x')
x0  = 0
x1, =  solve(f1(x)-f3(x))
x2, =  solve(f1(x)-f2(x))
x3, =  solve(f2(x)-f0(x))


y0 = f3(0)
y1 = f1(x1)
y2 = f2(x2)
y3 = f2(x3)

plt.plot(0,0,'go',markersize=10)
plt.plot(0,f3(0),'go',markersize=10)
plt.plot(x1,f1(x1),'go',markersize=10)
plt.plot(x2,f1(x2),'go',markersize=10)
plt.plot(x3,f2(x3),'go',markersize=10)

plt.fill([x0,x0,x1,x2,x3],[0,y0,y1,y2,y3],'yellow',alpha=0.5)


xr = np.linspace(-10,150,100)
y1r = f1(xr)
y2r = f2(xr)
y3r = f3(xr)
zr0 =Z(np.linspace(-10,10,100),0)
zr1 = Z(np.linspace(-10,130,100),120)
zr2 = Z(np.linspace(-10,150,100),140)
zr3 = Z(np.linspace(-10,160,100),150)
zr4 = Z(np.linspace(-10,160,100),175)

plt.plot(xr,y1r,'k--')
plt.plot(xr,y2r,'k--')
plt.plot(xr,y3r,'k--')
plt.plot(np.linspace(-10,10,100),zr0)
plt.plot(np.linspace(-10,130,100),zr1)
plt.plot(np.linspace(-10,150,100),zr2)
plt.plot(np.linspace(-10,160,100),zr3)
plt.plot(np.linspace(-10,160,100),zr4)

plt.show()



