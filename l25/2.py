import numpy as np
import matplotlib.pyplot as plt

# generate random values
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

# build a scatter plot
plt.scatter(x, y, s=area, c=colors, alpha=0.5)

# plot y versus x as lines
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

# Adjust x limits if needed
plt.xlim(x.min()*1.1, x.max()*1.1)

plt.show()