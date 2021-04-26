import os, sys 
if not ("AvancesSS/base" in sys.path[0][-13:]):
	sys.path.insert(0, os.path.abspath('../base'))

import numpy as np 

from geo.line import Line 
from fvm.sDiffusion import sDiffusion1D
from fvm.pde import PDE 
from utils.displayInfo import printInfo
import vis.flowix as flx 

longitud = 0.1 #metros
PA = 5. # Atm
PB = 2. # Atm
k = 1. # Darcys
N = 21

barra = Line(longitud)
barra.boundaryConditions(dirichlet = {'LEFT':PA, 'RIGHT':PB})

malla = barra.constructMesh(N)
ivx, _, _ = malla.bounds(bi = 1, ei = N-1)
nx = malla.nx
nvx = malla.vx
delta = malla.dx

P = np.zeros(nvx+2)
P[0] = PA 
P[-1] = PB

printInfo(Longitud = longitud,
		  Temperatura_A = PA,
		  Temperatura_B = PB,
		  Conductividad = k,
		  Nodos = nx,
		  Volúmenes = nvx,
		  Delta = delta)

S = np.zeros(ivx)

dif_scheme = sDiffusion1D(malla, S, k)

laplace = PDE(barra, P)

laplace.setNumericalScheme(dif_scheme)
laplace.solve()
print(P)

x, _, _ = malla.coordinatesMeshFVM()
m = (PB-PA)/(longitud)
Pa = m * x + PA

axis_par = [{'title':'Numérica', 'xlabel':'x [m]', 'ylabel':'Pressure[atm]'},
            {'title':'Exacta', 'xlabel':'x [m]', 'ylabel':'Pressure[atm]'},
            {'title':'Malla 1D'}]

v = flx.Plotter(3,1,axis_par)

v.plot(1,x,P, {'marker':'o', 'ls':'-', 'label':'Numérica'})

v.plot(2,x,Pa, {'marker':'s', 'ls':'-', 'color':'orange', 'label':'Exacta'})

v.plot_mesh(3, malla, label = True)

v.legend([1,2,3], par = {'ncol':2})

v.show()




