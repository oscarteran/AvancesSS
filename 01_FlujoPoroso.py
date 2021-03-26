# PATH para clases 
import os, sys
if not("Documentacion_Pynoxtli/base" in sys.path[0][-13:]):
    sys.path.insert(0, os.path.abspath('../../base'))

import numpy as np
#
# Importar módulos de pynoxtli
#
from geo.line import Line
from fvm.tDiffusion import tDiffusion1D
from fvm.pde import PDE
from utils.displayInfo import printInfo
import vis.flowix as flx

#
# Función que ejecuta FuncAnimation() en cada paso de tiempo
#
def solver(i, ax, dt):
    laplace.solve()
    line.set_ydata(T)
    
    time_step = i * dt
    title_graf = 'Sol. Numérica :  Step = {:>3d} Time = {:>6.5f}'.format(i, time_step)
    ax.set_title(title_graf)

# Datos que utilizamos
Lx = 100 #[cm]
Ly = 10
Lz = 10
phi = 0.2
mu = 1. #[cp]
k = 1. #[Darcy´s]
Ct = 10e-4 #[Atm^-1]
Rhoa = 2.0 #[Atm]
Rhob = 1. #[Atm]
Rho0 = 1. #[Atm]
Tmax = 0.8 #[s]
N = 6
# Relación de Nodos en x y y
# Nx = 10(2^m)+1
# Ny = 2^m+1
#
# Definición del dominio y condiciones de frontera
#
rod = Line(Lx)
#rod.boundaryConditions(dirichlet = {'RIGHT':TB, 'LEFT':TA})
malla     = rod.constructMesh(N)
ivx, _, _ = malla.bounds(bi = 1, ei = N-1)
nx        = malla.nx    # Número de nodos
nvx       = malla.vx    # Número de volúmenes
delta     = malla.dx    # Tamaño de los volúmenes








print('#UNAMNoPaga')