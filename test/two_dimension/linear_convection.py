import numpy as np
import matplotlib.pyplot as pl

'''
du/dt + c du/dx + c du/dy = 0
'''

from mpl_toolkits.mplot3d import Axes3D

nx = 81
ny = 81
nt = 100
c = 1
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
sigma = 0.2
dt = sigma * dx

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

u = np.ones((ny, nx))
un = np.ones((ny, nx))

u[int(0.5 / dy):int(1 / dy + 1), int(0.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt + 1):
    un = u.copy()
        
    u[1:, 1:] = (un[1:, 1:] - (c * dt / dx * (un[1:, 1:] - un[1:, :-1])) - \
            (c * dt / dy * (un[1:, 1:] - un[:-1, 1:])))
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

X, Y = np.meshgrid(x, y)
fig = pl.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, u[:])
pl.show()
