# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 17:36:56 2021
@author: hsauro
"""
import tellurium as te
import roadrunner
import matplotlib.pyplot as plt
r = te.loada("""
      J1: A -> AP; Vm1*A/(Km1 + A)
      J2: AP -> A; Vm2*AP/(Km2 + AP)
      Vm1 =15; Vm2 = 12
      Km1 = 20.5; Km2 = 0.01
      A = 10
""")
r.conservedMoietyAnalysis = True

def computeAPResponse (Km1, Km2, n):
    r.Vm1 = 0.1
    x = []; y = []
    r.Km1 = Km1; r.Km2 = Km2
    for i in range (n):
        r.steadyState()
        x.append (r.Vm1)
        y.append (r.AP)
        r.Vm1 = r.Vm1 + 0.1
    return x, y

def computeCCResponse (Km1, Km2, n):
    r.Vm1 = 0.1
    x = []; y = []
    r.Km1 = Km1; r.Km2 = Km2
    for i in range (n):
        r.steadyState()
        x.append (r.Vm1)
        y.append (r.getCC ('AP', 'Vm1'))
        r.Vm1 = r.Vm1 + 0.1
    return x, y

plt.subplots(2,4, figsize=(11,6))
x, y = computeAPResponse (20, 20, 1000)
plt.subplot (2, 4, 1)
plt.plot (x, y)
x, y = computeAPResponse (20, 0.02, 1000)
plt.subplot (2, 4, 2)
plt.plot (x, y)
x, y = computeAPResponse (0.5, 0.5, 200)
plt.subplot (2, 4, 3)
plt.plot (x, y)
x, y = computeAPResponse (0.5, 20, 200)
plt.subplot (2, 4, 4)
plt.plot (x, y)
# ---------------------------------------------------
x, y = computeCCResponse (20, 20, 1000)
plt.subplot (2, 4, 5)
plt.plot (x, y)
x, y = computeCCResponse (20, 0.1, 1000)
plt.subplot (2, 4, 6)
plt.plot (x, y)
x, y = computeCCResponse (0.5, 0.05, 200)
plt.subplot (2, 4, 7)
plt.plot (x, y)
x, y = computeCCResponse (0.5, 20, 200)
plt.subplot (2, 4, 8)
plt.plot (x, y) 