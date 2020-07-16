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

# defining x, y, z co-ordinates for bar position
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 3, 1, 6, 5, 3, 7, 5, 3, 7]
z = np.zeros(10)

# size of bars
dx = np.ones(10)  # length along x-axis
dy = np.ones(10)  # length along y-axs
dz = [1, 3, 4, 2, 6, 7, 5, 5, 10, 9]  # height of bar

# setting color scheme
color = []
for h in dz:
    if h > 5:
        color.append('r')
    else:
        color.append('b')

    # plotting the bars
ax1.bar3d(x, y, z, dx, dy, dz, color=color)

# setting axes labels
ax1.set_xlabel('x-axis')
ax1.set_ylabel('y-axis')
ax1.set_zlabel('z-axis')

plt.show()