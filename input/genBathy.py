#%%

import numpy as np
import struct
import matplotlib.pyplot as plt 

Nx = 62
Ny = 62

x = np.linspace(1,Nx,Nx)
y = np.linspace(1,Ny,Ny)

L = Nx
W = Ny

H = 5000 # depth of basin
h = 500 # height of seamount

bathy = [[-(H-h*np.sin((np.pi*x[i])/L)*np.sin((np.pi*y[j])/W)) for i in range(len(x))] for j in range(len(y))]

X,Y = np.meshgrid(x,y)

#%%

plt.contourf(X,Y,bathy)
plt.colorbar()
plt.show()

np.save('bathy', bathy)

'''bathy = np.reshape(bathy, Nx*Ny, 'C')

f = open('bathy.bin','wb')
f.write(struct.pack('>'+'d'*len(bathy), *bathy))
f.close()'''

# %%
