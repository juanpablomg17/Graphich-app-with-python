import matplotlib.pyplot as plt
import numpy as np


np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

producto1= (1954,2143,2826,2036,2827,1945)
producto2 = (2747,3030,4164,4178,3425,2228)


# Example data
paises = ('Argentina', 'Chile', 'Colombia', 'España', 'México','Perú')
y_pos = np.arange(len(paises))

p1 = ax.barh(y_pos, producto1,label="Producto 1")
p2 = ax.barh(y_pos, producto2,left = producto1,label="Producto 2")




ax.set_yticks(y_pos)
ax.set_yticklabels(paises)
names = plt.legend((p1[0], p2[0]), ('Producto 1', 'Producto 2'))
ax.set_xlabel("CANTIDADES EN PESOS $")

plt.show()