import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as ticker

n_groups = 6

#-----------------------------------------PRODUCTO 1 Y 2------------------------------------------------
producto1 = (46.8,67.49,44.40, 69.13, 53.14,32.96)
producto2 = (53.14,32.50,55.59, 30.86,46.86,67.04)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

p1  = plt.bar(index, producto1, bar_width, color='g',label='Producto1')
p2  = plt.bar(index, producto2, bar_width,bottom=producto1,label='Producto2')
plt.xticks(index, ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo','Junio'))


#-----------------------------------------PORCENTAJES EN EL Y------------------------------------------------
ax.yaxis.set_major_locator(ticker.MultipleLocator(10.00))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.25))
ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=100))


names = plt.legend((p1[0], p2[0]), ('Producto 1', 'Producto 2'))


plt.tight_layout()
plt.show()