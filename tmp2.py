from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

# setting a custom style to use
style.use('ggplot')

# create a new figure for plotting
fig = plt.figure()

# create a new subplot on our figure
ax1 = fig.add_subplot(111, projection='3d')

# get points for a mesh grid
u, v = np.mgrid[0:2 * np.pi:200j, 0:np.pi:100j]

# setting x, y, z co-ordinates
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)

# plotting the curve
ax1.plot_wireframe(x, y, z, rstride=5, cstride=5, linewidth=1)

plt.show()