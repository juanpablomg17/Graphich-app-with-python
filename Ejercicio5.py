import numpy as np
import matplotlib.pyplot as plt

np.random.seed(19680801)

mu = 200
sigma = 25
x = np.random.normal(mu, sigma, size=100)

fig, (ax1) = plt.subplots()



# Create a histogram by providing the bin edges (unequally spaced).
bins = [100, 150, 180, 195, 205, 220, 250, 300]
ax1.hist(x, bins, density=True, histtype='bar', rwidth=0.5)
ax1.set_title('unequal bins')

fig.tight_layout()
plt.show()