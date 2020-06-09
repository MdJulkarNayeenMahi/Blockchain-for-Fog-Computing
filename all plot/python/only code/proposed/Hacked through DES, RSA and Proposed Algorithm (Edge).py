import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px



DataX_Y_1D = np.loadtxt("Hacked through DES, RSA and Proposed Algorithm (Edge).csv", delimiter=",")

# create 2d x,y grid (both X and Y will be 2d)
X, Y = np.meshgrid(DataX_Y_1D[:,0], DataX_Y_1D[:,2])
X1, Y1 = np.meshgrid(DataX_Y_1D[:,1], DataX_Y_1D[:,3])

# get 2D z data
#Z = np.loadtxt("fog.csv", delimiter=",")

Z = np.tile(DataX_Y_1D[:,5], (len(DataX_Y_1D[:,5]), 1))
Z1 = np.tile(DataX_Y_1D[:,4], (len(DataX_Y_1D[:,4]), 1))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#px.line_3d(X, Y, Z)
ax.plot_surface(X, Y, Z,cmap='viridis', linestyles='dashed')
ax.plot_surface(X1, Y1, Z1,cmap='ocean', linestyles='dashed')

plt.xlabel('DES Alogorithm')
plt.ylabel('RSA Algorithm')
ax.set_zlabel('Proposed Algorithm')
plt.title('Hacked through DES, RSA and Proposed Algorithm (Edge)')



plt.show()
